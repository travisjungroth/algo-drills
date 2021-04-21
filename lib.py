from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence
import csv
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from difflib import ndiff
import io
import re
from time import time
import tokenize
from typing import Final, Iterable, Optional

ALGO_DIR = 'algorithms'


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
        return (m.group(1) + m.group(2)).rstrip().splitlines()

    def diff(self, other: Code) -> str:
        return '\n'.join(ndiff(self.diff_ready(), other.diff_ready()))

    def matches(self, other: Code) -> bool:
        return isinstance(other, Code) and self.diff_ready() == other.diff_ready()


@dataclass(frozen=True)
class Algo(Code):
    id: int
    name: str

    def __str__(self) -> str:
        return self.name

    def text(self) -> str:
        with open(f'{ALGO_DIR}/{self.name}.py') as f:
            return f.read()

    def workspace_ready(self) -> str:
        s = re.search(r'.*?\ndef.*?:\n {4}(?:""".*?""")?', self.cleaned(), re.DOTALL).group(0)
        if s[-1] != '"':
            s += 'pass'
        s += '\n'
        return s


with open('algos.csv') as _algos_fp:
    ALGOS_DICT: Final[dict[int, Algo]] = {int(d['id']): Algo(int(d['id']), d['name'])
                                          for d in csv.DictReader(_algos_fp)}


@dataclass(frozen=True)
class Workspace(Code):
    file_name: str = 'workspace.py'

    def text(self) -> str:
        with open(self.file_name) as f:
            return f.read()

    def algo(self) -> Optional[Algo]:
        """Grab the algo from the function name"""
        m = re.search(r'def (\w+)\(', self.text())
        if not m:
            return None
        algo_name = m.group(1)
        for algo in ALGOS_DICT.values():
            if algo_name == algo.name:
                return algo
        raise ValueError(f'No algo found called "{algo_name}. Looking based on def in workspace.py.')

    def write_algo(self, algo: Algo) -> None:
        with open(self.file_name, 'w') as f:
            f.write(algo.workspace_ready())

    def advance(self) -> Algo:
        with open('allowed.csv') as f:
            allowed = [ALGOS_DICT[int(i)] for i, in csv.reader(f)]
        algo = choose_algo(Completion.history(), allowed)
        self.write_algo(algo)
        return algo


@dataclass(frozen=True)
class Completion:
    algo: Algo
    datetime: datetime = field(default_factory=datetime.utcnow)
    file_name: str = 'history.csv'

    @classmethod
    def history(cls) -> list[Completion]:
        with open(cls.file_name) as f:
            return [
                       cls(ALGOS_DICT[int(d['id'])], datetime.fromisoformat(d['datetime']))
                       for d in csv.DictReader(f)
                   ][::-1]

    def append_to_file(self) -> None:
        with open(self.file_name, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([self.datetime.isoformat(' ', 'seconds'), self.algo.id])


def choose_algo(history: Sequence[Completion], algos: Iterable[Algo]) -> Algo:
    history = [completion.algo for completion in history]
    if not history:
        return next(iter(algos))
    last = history[0]
    count = history.count(last)
    reps = max(1, 3 - (count // 12))
    if len(history) < reps:
        return last
    if not all(last == h for h in history[1:reps]):
        return last
    return max(algos, key=lambda x: history.index(x) if x in history else len(history))


def start_timer() -> None:
    with open('start_time.txt', 'w') as f:
        f.write(str(int(time())))


def stop_timer() -> Optional[timedelta]:
    now = int(time())
    with open('start_time.txt', 'r+') as f:
        txt = f.read()
        if not txt:
            return None
        start = int(txt)
        f.write('')
    return timedelta(seconds=now - start)


def minutes_seconds(td: timedelta) -> str:
    m, s = divmod(int(td.total_seconds()), 60)
    return f'{m}:{s:02}'
