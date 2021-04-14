from __future__ import annotations

from lib import Completion, Workspace


def practice() -> None:
    workspace = Workspace()
    algo = workspace.algo()
    if algo is None or workspace.matches(algo):
        if algo is not None:
            Completion(algo).append_to_file()
        new_algo = workspace.advance()
        print(f'Try {new_algo}')
    else:
        print(algo.diff(workspace))


if __name__ == '__main__':
    practice()
