from collections.abc import Sequence

from hints import T


def valid_nesting_single(items: Sequence[T], opener: T, closer: T) -> bool:
    depth = 0
    for item in items:
        if item == opener:
            depth += 1
        elif item == closer:
            depth -= 1
            if depth < 0:
                return False
    return not depth
