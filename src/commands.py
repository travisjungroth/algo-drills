from datetime import timedelta
from pathlib import Path
import re
from uuid import uuid4

from src import Algo, Completion, minutes_seconds, start_timer, stop_timer, Workspace


def practice(args) -> str:
    out: list[str] = []
    workspace = Workspace()
    algo = workspace.algo()
    if workspace.matches(algo):
        Completion(algo).append_to_file()
        completion_time = stop_timer()
        if completion_time < timedelta(minutes=15):
            out.append(minutes_seconds(completion_time))
        if Algo.done_today().issuperset(Algo.allowed()):
            out.append('Did every algo today')
    if algo is None or workspace.matches(algo):
        requested_algo = Algo.from_id_or_name(args.algo)
        new_algo = workspace.advance(requested_algo)
        start_timer()
        out.append(f'Try {new_algo}')
    else:
        out.append(algo.diff(workspace))
    return '\n'.join(out)


def search_reference(args) -> str:
    out = []
    pages_and_algos = []
    allowed = Algo.allowed()
    for algo in Algo.all():
        if args.new and algo in allowed:
            continue
        m = re.search(fr'{args.reference}, Page (\d+)', algo.text())
        if m is not None:
            pages_and_algos.append((m.group(1), algo))
    pages_and_algos.sort(key=lambda x: (int(x[0]), x[1].name))
    for page, algo in pages_and_algos:
        out.append(f'{algo}, Page {page}')
    return '\n'.join(out)


def new_algo(args) -> str:
    uuid = uuid4()
    text = f'''"""
ID: {uuid}
"""


def {args.name}():
    pass
'''

    Path('user_algorithms').mkdir(exist_ok=True)
    with open(f'user_algorithms/{args.name}.py', 'x') as f:
        f.write(text)
    if not args.skip_allow:
        with open('user_data/allowed.csv', 'a+') as f:
            f.write(str(uuid) + '\n')
    return f'Created {args.name}.py in user_algorithms.'
