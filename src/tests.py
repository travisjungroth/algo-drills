from src import Algo


def test_names_match():
    for algo in Algo.all():
        assert f'def {algo.name}(' in algo.text()
