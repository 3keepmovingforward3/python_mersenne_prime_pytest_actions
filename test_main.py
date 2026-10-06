from main import is_prime

def test_is_prime():
    assert is_prime(((1<<31)-1)) == True
