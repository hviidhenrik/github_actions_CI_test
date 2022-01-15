"""
Unit tests go here
"""
import pytest
from src.core import my_add


@pytest.mark.parametrize("input, expected", [[(5, 5), 10], [(8, 8), 16]])
def test_my_add(input, expected):
    assert my_add(*input) == expected

