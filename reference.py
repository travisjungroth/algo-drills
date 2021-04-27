#!/usr/bin/env python3
"""Takes a book name and prints the algos in the book not in your allowed list."""
import re
import sys

from src import Algo

ref = sys.argv[1]
x = []
allowed = Algo.allowed()
for algo in Algo.all():
    if algo in allowed:
        continue
    m = re.search(fr'{ref}, Page (\d+)', algo.text())
    if m is not None:
        x.append((m.group(1), algo))
x.sort()
for page, algo in x:
    print(f'{algo}, Page {page}')
