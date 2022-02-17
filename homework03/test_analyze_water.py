from analyze_water import calculate_turbidity
from analyze_water import safe_threshold_time
import pytest

#Testing for calculate_turbidity function
def test_calculate_turbidity():
    assert calculate_turbidity({4},{2}) == 8
    assert calculate_turbidity({2},{2}) == 4
    assert calculate_turbidity({3}, {4}) == 12
    assert isinstance(calculate_turbidity({2}, {2}), float) == True

def test_calculate_turbidity_exceptions():
    #Test by sending an empty list
    with pytest.raises(ZeroDivisionError):
        calculate_turbidity([], 'a')
    #Test by sending a value that is not a float
    with pytest.raises(ValueError):
        calculate_turbidity([{'a': 1}, {'a': 'x'}], 'a')

#Testing for safe_threshold_time
def test_safe_threshold_time():
    assert safe_threshold_time([{'a': 2}]) == 50
    assert safe_threshold_time([{'a': 1.5}]) == 25
    assert safe_threshold_time([{'a': 1}]) == 0
    assert safe_threshold_time([{'a': 0.5}]) == 0
    assert isinstance(safe_threshold_time([{'a': 2}]), float) == True

def test_safe_threshold_time_exceptions():
    #Test by sending a value that is not a float
    with pytest.raises(ValueError):
        safe_threshold_tim([{'a': 'x'}], 'a')
    #Test by sending an empty list
    with pytest.raises(ZeroDivisionError):
        safe_threshold_time([], 'a')

