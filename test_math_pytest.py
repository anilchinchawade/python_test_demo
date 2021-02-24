import pytest
import mathlib

def test_total():
    res = mathlib.total(3, 4)
    assert res == 7


def test_multiply():
    res = mathlib.multiply(3, 4)
    assert res == 12