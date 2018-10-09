import inspect
import pytest
from _pytest.mark import ParameterSet

__version__ = '0.1.0'


def auto_parametrize(argvalues, *args, **kwargs):
    """Deduce argument names from function signature.

    The argument values correspond to the function arguments in the
    given order.  Any trailing argument names can be fixtures or
    arguments from ``@pytest.mark.parametrize(...)`` decorators.

    """
    def decorator(func):
        try:
            argvalue = argvalues[0]
        except IndexError:
            raise ValueError('argvalues must be non-empty')
        except TypeError:
            raise TypeError('argvalues must be a sequence')
        argvalue = ParameterSet.extract_from(argvalue).values
        argspec = inspect.getargspec(func)[0]
        if isinstance(argvalue, (list, tuple)):
            argnames = argspec[:len(argvalue)]
        else:
            argnames = argspec[0]
        return pytest.mark.parametrize(
            argnames, argvalues, *args, **kwargs)(func)
    return decorator


def pytest_namespace():
    """Register pytest plugin."""
    return {'auto_parametrize': auto_parametrize}
