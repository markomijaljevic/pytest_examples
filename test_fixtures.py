from _pytest.mark import param
import pytest

@pytest.fixture(autouse=True)
def database():
    # return <some database connection>
    pass

@pytest.fixture(params=['mysql', 'postgresql'])
def database(request):
    d = myapp.driver(request.param)
    yield d
    d.stop()

def test_insert(database):
    database.insert(123)
    
def test_insert_2(database):
    database.insert(6565)
