def test_true():
    assert True

def test_false():
    assert False

def test_key():
    a = [1, 2]
    b = [1]
    assert a == b

def function(x):
    return x + 3

def test_function():
    assert function(3) == 6