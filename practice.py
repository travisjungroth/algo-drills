from __future__ import annotations

from datetime import datetime, timedelta

from lib import ALLOWED, Completion, minutes_seconds, start_timer, stop_timer, Workspace


def practice() -> None:
    workspace = Workspace()
    algo = workspace.algo()
    if algo is None or workspace.matches(algo):
        if algo is not None:  # success
            Completion(algo).append_to_file()
            completion_time = stop_timer()
            if completion_time < timedelta(minutes=30):
                print(minutes_seconds(completion_time))
            now = datetime.utcnow()
            recent = {c.algo for c in Completion.history() if now - c.datetime < timedelta(hours=16)}
            if recent.issuperset(ALLOWED):
                print('*')
        new_algo = workspace.advance()
        start_timer()
        print(f'Try {new_algo}')
    else:
        print(algo.diff(workspace))


if __name__ == '__main__':
    practice()
