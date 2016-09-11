import inspect
import pytest
from _pytest.mark import extract_argvalue


def auto_parametrize(argvalues, *args, **kwargs):
    def decorator(func):
        try:
            argvalue = argvalues[0]
        except IndexError:
            raise ValueError('argvalues must be non-empty')
        except TypeError:
            raise TypeError('argvalues must be a sequence')
        argvalue, _ = extract_argvalue(argvalue)
        argspec = inspect.getargspec(func)[0]
        if isinstance(argvalue, (list, tuple)):
            argnames = argspec[:len(argvalue)]
        else:
            argnames = argspec[0]
        return pytest.mark.parametrize(
            argnames, argvalues, *args, **kwargs)(func)
    return decorator


def pytest_namespace():
    return {'auto_parametrize': auto_parametrize}
