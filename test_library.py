# Pytest file 

# Pytest checks for any files named test to open and inside those files
# it checks for any functions named test to test, so thats why we need to begin with test_

# We expect this to pass
def test_pass():
    assert 1 + 1 == 2

# We expect this to fail
def test_fail():
    assert 2 + 2 == 5

