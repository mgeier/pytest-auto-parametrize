import pytest


@pytest.auto_parametrize([
    pytest.mark.xfail((3, 3, 7)),
    (2, 2, 4),
    (1, 1, 1),
])
def test_multiple_arguments(a, b, c):
    assert a * b == c


@pytest.fixture
def myfixture():
    return 42


@pytest.auto_parametrize([
    (7, 50, 99),
    (0, 0, 42),
    (58, -100, 0),
])
def test_multiple_arguments_plus_fixture(x, y, z, myfixture):
    assert x + y + myfixture == z


@pytest.auto_parametrize([1, 2, 3])
def test_single_argument(x):
    assert x in (1, 2, 3)


@pytest.auto_parametrize([pytest.mark.xfail('zero'), 'one', 'two'])
def test_single_string_argument(x):
    assert x in ('one', 'two')


@pytest.mark.parametrize('x', [0, 1, 2])
@pytest.auto_parametrize([
    (3, 4),
    (5, 6),
])
@pytest.mark.parametrize('y', [7, 8, 9])
def test_parametrize_mixed_with_auto_parametrize(a, b, x, y):
    assert a in (3, 5)
    assert b in (4, 6)
    assert x in (0, 1, 2)
    assert y in (7, 8, 9)
