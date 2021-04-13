from collections.abc import Sequence
from difflib import ndiff
import io
from os import listdir
import re
import tokenize

ALGO_DIR = 'algorithms'


# ALGO_DIR = 'test_algorithms'


def choose_algo(history: Sequence[str], algos: Sequence[str]) -> str:
    repeats = 2
    if not history:
        return algos[0]
    if len(history) <= repeats:
        return history[0]
    if not all(history[0] == h for h in history[1:repeats + 1]):
        return history[0]
    return max(algos, key=lambda x: history.index(x) if x in history else len(history))


def remove_comments(source):
    io_obj = io.StringIO(source)
    out = ""
    last_lineno = -1
    last_col = 0
    skip_line = False
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        if token_type in [tokenize.NEWLINE, tokenize.NL] and skip_line:
            skip_line = False
            out = out.rstrip(' ')
            continue
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        if token_type == tokenize.COMMENT:
            skip_line = tok.line.strip() == tok.string.strip()
        elif token_type == tokenize.STRING:
            if start_col == 0:
                skip_line = True
            else:
                out += token_string
        else:
            out += token_string
        last_col = end_col
        last_lineno = end_line
    out = '\n'.join(l.rstrip() if l.rstrip() else l for l in out.splitlines()) + '\n'
    return out


if __name__ == '__main__':
    name = ''
    success = False
    with open('workspace.py') as f:
        workspace = f.read()
        lines = workspace.splitlines()
    if lines:
        line = [line for line in lines if line.startswith('def ')][0]
        name = line[4:line.index('(')]
        try:
            with open(f'{ALGO_DIR}/{name}.py') as f:
                correct = remove_comments(f.read())
        except FileNotFoundError:
            overwrite = True
        else:
            if correct == workspace:
                overwrite = True
                success = True
            else:
                stuff = []
                for x in [correct, workspace]:
                    m = re.search(r'(def.*?:\n)(?: {4}""".*?"""\n)?(.*)', x, re.DOTALL)
                    stuff.append(m.group(1) + m.group(2))
                diff = ndiff(*[x.splitlines() for x in stuff])
                print('\n'.join(diff))
                overwrite = False
    else:
        overwrite = True

    if success:
        with open('history.txt', 'a') as f:
            f.write(name + '\n')

    if overwrite:
        with open('history.txt') as history_file:
            history = [line.strip() for line in history_file.readlines()][::-1]
        # Find the file that hasn't been used in the longest
        algos = [x[:-3] for x in listdir(f'{ALGO_DIR}') if not x.startswith('_')]
        algo = choose_algo(history, algos)
        with open('workspace.py', 'w') as f1, open(f'{ALGO_DIR}/{algo}.py') as f2:
            new = []
            algo_code = remove_comments(f2.read())
            s = re.search(r'.*?\ndef.*?:\n {4}(?:""".*?""")?', algo_code, re.DOTALL).group(0)
            if s[-1] != '"':
                s += 'pass'
            s += '\n'
            f1.write(s)
        print(f'Try {algo}')
