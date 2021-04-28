from datetime import timedelta

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
