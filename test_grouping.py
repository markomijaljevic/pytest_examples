import pytest

@pytest.mark.one
def test_true():
    assert True

@pytest.mark.two
def test_false():
    assert False