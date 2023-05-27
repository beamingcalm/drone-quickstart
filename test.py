def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2

def test_multiplication():
    assert 2 * 3 == 6

def test_division():
    assert 10 / 2 == 5

if __name__ == "__main__":
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    print("All tests passed!")
