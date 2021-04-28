#!/usr/bin/env python3
"""Optionally takes the uuid or name of the algorithm you want."""
from datetime import timedelta
import sys

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
            print('Did every algo today')
    if algo is None or workspace.matches(algo):
        if len(sys.argv) > 1:
            requested_algo = Algo.from_id_or_name(sys.argv[1])
        else:
            requested_algo = None
        new_algo = workspace.advance(requested_algo)
        start_timer()
        print(f'Try {new_algo}')
    else:
        print(algo.diff(workspace))


if __name__ == '__main__':
    practice()
