import csv
import os


def test_names_match():
    with open('algos.csv') as f:
        csv_names = {d['name'] for d in csv.DictReader(f)}
    file_names = {f[:-3] for f in os.listdir('algorithms') if not f.startswith('_')}
    assert file_names == csv_names
    for name in file_names:
        with open(f'algorithms/{name}.py') as f:
            assert f'def {name}(' in f.read()
