#!/usr/bin/env python3
"""Takes a book name and prints the algos in the book not in your allowed list."""
import re
import sys

from src import Algo

ref = sys.argv[1]
pages_and_algos = []
allowed = Algo.allowed()
for algo in Algo.all():
    if algo in allowed:
        continue
    m = re.search(fr'{ref}, Page (\d+)', algo.text())
    if m is not None:
        pages_and_algos.append((m.group(1), algo))
pages_and_algos.sort(key=lambda x: (int(x[0]), x[1].name))
for page, algo in pages_and_algos:
    print(f'{algo}, Page {page}')
