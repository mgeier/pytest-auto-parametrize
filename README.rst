`pytest` plugin: avoid repeating arguments in `parametrize`
===========================================================

This is an alternative to the rejected pull request
`#780 <https://github.com/pytest-dev/pytest/pull/780>`__ of
`pytest <http://docs.pytest.org/>`__.

Installation
------------

Just get it from `PyPI <https://pypi.org/project/pytest-auto-parametrize>`__::

    python3 -m pip install pytest-auto-parametrize --user

Usage
-----

This is an example for the usage of a `parametrized test`__ without using this
plugin:

__ http://docs.pytest.org/en/latest/parametrize.html

.. code:: python

    import pytest
    
    testparams = [
        (1, 2, 3, 4, 5, 6, 7),
        (7, 6, 5, 4, 3, 2, 1),
    ]
    
    @pytest.mark.parametrize('a, b, c, d, e, f, g', testparams)
    def test_many_args(a, b, c, d, e, f, g):
        assert d == 4

The argument list has to be repeated, which is annoying.

By using this plugin, the repetition can be avoided:

.. code:: python

    import pytest
    
    testparams = [
        (1, 2, 3, 4, 5, 6, 7),
        (7, 6, 5, 4, 3, 2, 1),
    ]
    
    @pytest.auto_parametrize(testparams)
    def test_many_args(a, b, c, d, e, f, g):
        assert d == 4

The auto-deduced parameters must be in the beginning of the parameter list, but
any other parameters can be used afterwards, e.g. fixtures:

.. code:: python

    import pytest
    
    testparams = [
        (1, 2, 3, 4, 5, 6, 7),
        (7, 6, 5, 4, 3, 2, 1),
    ]
    
    @pytest.fixture
    def myfixture():
        return 4
    
    @pytest.auto_parametrize(testparams)
    def test_many_args_and_fixture(a, b, c, d, e, f, g, myfixture):
        assert d - myfixture == 0

Limitations
-----------

Unlike ``@pytest.mark.parametrize(...)`` the decorator
``@pytest.auto_parametrize(...)`` cannot be used multiple times for the same
test function.  It can be used together with one or multiple instances of
``@pytest.mark.parametrize(...)``, though, as long as the "auto" arguments are
in the beginning of the argument list.
