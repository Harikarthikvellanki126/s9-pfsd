import pytest as pytest

def fn(x):
    return x+1
def test_ans():
    assert fn(3)==5