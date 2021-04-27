from __future__ import annotations

from datetime import timedelta

from src import Algo, Completion, minutes_seconds, start_timer, stop_timer, Workspace


def practice() -> None:
    workspace = Workspace()
    algo = workspace.algo()
    if workspace.matches(algo):
        Completion(algo).append_to_file()
        completion_time = stop_timer()
        if completion_time < timedelta(minutes=15):
            print(minutes_seconds(completion_time))
        if Algo.done_today().issuperset(Algo.allowed()):
            print('*')
    if algo is None or workspace.matches(algo):
        new_algo = workspace.advance()
        start_timer()
        print(f'Try {new_algo}')
    else:
        print(algo.diff(workspace))


if __name__ == '__main__':
    practice()
