from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence
import csv
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from difflib import ndiff
import io
from itertools import groupby
import os
from pathlib import Path
import random
import re
from time import time
import tokenize
from typing import Any, ClassVar, Iterable, Optional

random.seed(0)


class Code(ABC):
    @abstractmethod
    def text(self) -> str:
        pass

    def cleaned(self) -> str:
        """Comments, module docstring, and trailing spaces removed"""
        io_obj = io.StringIO(self.text())
        out = ""
        last_lineno = -1
        last_col = 0
        skip_line = False
        for tok in tokenize.generate_tokens(io_obj.readline):
            token_type = tok[0]
            token_string = tok[1]
            start_line, start_col = tok[2]
            end_line, end_col = tok[3]
            if token_type in [tokenize.NEWLINE, tokenize.NL] and skip_line:
                skip_line = False
                out = out.rstrip(' ')
                continue
            if start_line > last_lineno:
                last_col = 0
            if start_col > last_col:
                out += (" " * (start_col - last_col))
            if token_type == tokenize.COMMENT:
                skip_line = tok.line.strip() == tok.string.strip()
            elif token_type == tokenize.STRING:
                if start_col == 0:
                    skip_line = True
                else:
                    out += token_string
            else:
                out += token_string
            last_col = end_col
            last_lineno = end_line
        out = '\n'.join(line.rstrip() if line.rstrip() else line for line in out.splitlines()).lstrip()
        return out

    def diff_ready(self) -> list[str]:
        """From cleaned to remove imports, function docstring, and trailing newlines"""
        m = re.search(r'(def.*?:\n)(?: {4}""".*?"""\n)?(.*)', self.cleaned(), re.DOTALL)
        if m is None:
            return self.cleaned().splitlines()
        return (m.group(1) + m.group(2)).rstrip().splitlines()

    def diff(self, other: Code) -> str:
        return '\n'.join(ndiff(self.diff_ready(), other.diff_ready()))

    def matches(self, other: Any) -> bool:
        return isinstance(other, Code) and self.diff_ready() == other.diff_ready()


@dataclass(frozen=True)
class Algo(Code):
    name: str
    dir: str

    def __str__(self) -> str:
        return self.name

    @classmethod
    def all(cls) -> Iterable[Algo]:
        Path('user_algorithms').mkdir(exist_ok=True)
        for directory in ['algorithms', 'user_algorithms']:
            for name in os.listdir(directory):
                if not name.startswith('_') and name.endswith('.py'):
                    yield cls(name[:-len('.py')], directory)

    @classmethod
    def id_dict(cls) -> dict[str, Algo]:
        return {a.uuid(): a for a in cls.all()}

    @classmethod
    def from_id_or_name(cls, s: str) -> Algo:
        for algo in cls.all():
            if algo.uuid() == s or algo.name == s:
                return algo
        raise ValueError(f"Couldn't find algo with name or id {s}.")

    @classmethod
    def allowed(cls) -> list[Algo]:
        file = Path('user_data/allowed.csv')
        if not file.exists():
            with file.open('w+') as f:
                f.write('d5c1e52d-602a-4c27-a39f-2b53caff987d\n')  # bisect_search
        with open('user_data/allowed.csv') as f:
            allowed_ids = set(f.read().splitlines())
            allowed_ids.discard('')
        return [x for x in cls.all() if x.uuid() in allowed_ids]

    @classmethod
    def done_today(cls) -> set[Algo]:
        return {c.algo for c in Completion.history() if c.datetime.date() == datetime.today().date()}

    def text(self) -> str:
        with open(f'{self.dir}/{self.name}.py') as f:
            return f.read()

    def uuid(self):
        return self.text().splitlines(keepends=False)[1][4:]

    def workspace_ready(self) -> str:
        s = re.search(r'.*?def.*?:\n {4}(?:""".*?""")?', self.cleaned(), re.DOTALL).group(0)
        if s[-1] != '"':
            s += 'pass'
        s += '\n'
        return s


@dataclass(frozen=True)
class Workspace(Code):
    file_name: str = 'workspace.py'

    def text(self) -> str:
        try:
            with open(self.file_name) as f:
                return f.read()
        except FileNotFoundError:
            open(self.file_name, 'a').close()
            return ''

    def algo(self) -> Optional[Algo]:
        """Grab the algo from the function name"""
        m = re.search(r'def (\w+)\(', self.text())
        if not m:
            return None
        algo_name = m.group(1)
        for algo in Algo.all():
            if algo_name == algo.name:
                return algo
        raise ValueError(f'No algo found called "{algo_name}. Looking based on def in workspace.py.')

    def write_algo(self, algo: Algo) -> None:
        with open(self.file_name, 'w') as f:
            f.write(algo.workspace_ready())

    def advance(self, algo: Optional[Algo] = None) -> Algo:
        if algo is None:
            algo = choose_algo(Completion.history(), Algo.allowed())
        self.write_algo(algo)
        return algo


@dataclass(frozen=True)
class Completion:
    algo: Algo
    datetime: datetime = field(default_factory=lambda: datetime.now().astimezone())
    history_path: ClassVar[Path] = Path('user_data/history.csv')

    @classmethod
    def history(cls) -> list[Completion]:
        cls.history_path.touch()
        with cls.history_path.open() as f:
            algos_dict = Algo.id_dict()
            out = []
            for dt, uuid in csv.reader(f):
                if uuid in algos_dict:
                    out.append(cls(algos_dict[uuid], datetime.fromisoformat(dt)))
        return out[::-1]

    def append_to_file(self) -> None:
        with self.history_path.open('a+') as f:
            writer = csv.writer(f)
            writer.writerow([self.datetime.isoformat(' ', 'seconds'), self.algo.uuid()])
        self.update_display_history()

    @classmethod
    def update_display_history(cls) -> None:
        with open('user_data/history.txt', 'w+') as f:
            for date, completions in groupby(cls.history(), lambda x: x.datetime.date()):
                f.write(f'{date.strftime(f"%A, %B {date.day}, %Y")}\n')
                for completion in completions:
                    f.write(f'  {completion.datetime.strftime("%I:%M%p")} {completion.algo}\n')


def choose_algo(history: Sequence[Completion], algos: Sequence[Algo]) -> Algo:
    history = [completion.algo for completion in history]
    if not history:  # if nothing, grab the first
        return next(iter(algos))
    last = history[0]
    count = history.count(last)
    rep_scheme = [3] * 3 * 3 + [2] * 2 * 3  # [reps] * reps * sets
    reps = rep_scheme[count] if count < len(rep_scheme) else 1
    if len(history) < reps or not all(last == h for h in history[1:reps]):  # not enough reps
        return last
    for algo in algos:
        if algo not in history:  # something new
            return algo
    arranged = sorted(algos, key=history.index)
    if len(algos) > 5:  # if it's long, let's maybe swap things to change it up
        repeats_removed = [k for k, g in groupby(history)]
        if set(repeats_removed[:len(algos)]) == set(algos) and random.choice([True, False]):
            return arranged[-2]
    return arranged[-1]  # oldest one


def start_timer() -> None:
    with open('user_data/start_time.txt', 'w+') as f:
        f.write(str(int(time())))


def stop_timer() -> Optional[timedelta]:
    now = int(time())
    with open('user_data/start_time.txt', 'r+') as f:
        txt = f.read()
        if not txt:
            return None
        start = int(txt)
        f.write('')
    return timedelta(seconds=now - start)


def minutes_seconds(td: timedelta) -> str:
    m, s = divmod(int(td.total_seconds()), 60)
    return f'{m}:{s:02}'
