import pytest


@pytest.auto_parametrize([
    pytest.mark.xfail((3, 3, 7)),
    (2, 2, 4),
    (1, 1, 1),
])
def test_multiple_arguments(a, b, c):
    assert a * b == c


@pytest.auto_parametrize([1, 2, 3])
def test_single_argument(x):
    assert x in (1, 2, 3)


@pytest.auto_parametrize([pytest.mark.xfail('zero'), 'one', 'two'])
def test_single_string_argument(x):
    assert x in ('one', 'two')
