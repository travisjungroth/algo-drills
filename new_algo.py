#!/usr/bin/env python3
"""
Takes the name of a new algo to create. Makes an empty template in user_algorithms and adds to whitelist.
"""

import sys
from uuid import uuid4

name = sys.argv[1]
uuid = uuid4()
text = f'''"""
ID: {uuid}
"""


def {name}():
    pass
'''

with open(f'user_algorithms/{name}.py', 'x') as f:
    f.write(text)

with open('data/allowed.csv', 'a') as f:
    f.write(str(uuid) + '\n')
