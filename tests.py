import re

algo_code = '''from itertools import product
from typing import TypeVar, Iterable
T = TypeVar('T')


def documented(a: Iterable[T], b: Iterable[T]) -> Iterable[tuple[T, T]]:
    """Single line docstring"""
    args = [a, b]
    return product(*args)
'''
m = re.search(r'.*?\ndef.*?:\n {4}(?:""".*?"""\n {4})?', algo_code, re.DOTALL)
print(m.group(0))
g = {
    'S': set('AB'),
    'A': set('SBF'),
    'B': set('SAF'),
    'F': set('ABF'),
    'C': set('D'),
    'D': set('C'),
}

g2 = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
m = [
    [1, 0, 0],
    [0, 1, 1],
    [0, 1, 1],
]

# s = list(range(1000))
# for _ in range(1):
#     graph = {c: {} for c in s}
#     for c in s:
#         for _ in range(100):
#             graph[c][choice(s)] = randrange(1, 101)
#     a = time()
#     d1 = dijkstras_distances(graph, s[0])
#     b = time()
#     d2 = dijkstras_distances2(graph, s[0])
#     c = time()
#     print(b-a)
#     print(c-b)
#     for c in s:
#         assert d1[c] == d2[c], (d1[c], d2[c])
#     assert d1 == d2


dag = {
    'A': 'BF',
    'B': 'CDF',
    'C': 'D',
    'D': 'EF',
    'E': 'F',
    'F': '',
}

# n = 10
# m = [[randrange(2) for _ in range(n)] for _ in range(n)]
# for row in m:
#     row[5] = 1
# m[5] = [0] * n
#
# d = {}
# for r, row in enumerate(m):
#     d[r] = set()
#     for c, n in enumerate(row):
#         if n:
#             d[r].add(c)