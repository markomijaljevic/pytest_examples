from unittest import mock
import os

# m = mock.Mock()
# m.custom_attr = "hello world"

# print(m.custom_attr)

########################################################

# m.some_method.return_value = 42
# print(m.some_method())
# print(m.some_method('test', 'some arguments'))

########################################################

# def hello_world():
#     print("hello world")
#     return 32

# m.some_method.side_effect = hello_world
# print(m.some_method())

########################################################

# def fake_os_unlink(path):
#     raise IOError("Testing!")

# with mock.patch('os.unlink', fake_os_unlink):
#     os.unlink('foobar')


########################################################

import pytest
import requests

class WhereIsPythonError(Exception):
    pass

def is_python_still_a_programming_language():
    try:
        r = requests.get("http://python.org")
    except IOError:
        pass
    else:
        if r.status_code == 200:
            return 'Python is a programming language' in r.content
    raise WhereIsPythonError("Something bad happend")


def get_fake_get(status_code, content):
    m = mock.Mock()
    m.status_code = status_code
    m.content = content

    def fake_get(url):
        return m

    return fake_get


def raise_get(url):
    raise IOError(f"Unable to fetch url {url}")


@mock.patch('requests.get', get_fake_get(200, "Python is a programming language for sure"))
def test_python_is():
    assert is_python_still_a_programming_language() is True


@mock.patch('requests.get', get_fake_get(200, "Python is no more a programming language"))
def test_python_is_not():
    assert is_python_still_a_programming_language() is False


@mock.patch('requests.get', get_fake_get(404, "Whatever"))
def test_bad_status_code():
    with pytest.raises(WhereIsPythonError):
        is_python_still_a_programming_language()


@mock.patch('requests.get', raise_get)
def test_ioerror():
    with pytest.raises(WhereIsPythonError):
        is_python_still_a_programming_language()


