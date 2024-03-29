import pytest
from src.Calulator import Calculator
@pytest.fixture
def set_up() :
    return Calculator

@pytest.mark.parametrize("sum", [9])
def test_Cal_Add(set_up, sum):
    assert set_up.add(5,4) == sum

@pytest.mark.parametrize("diff", [1])
def test_Cal_Sub(set_up, diff):
    assert set_up.sub(5,4) == diff