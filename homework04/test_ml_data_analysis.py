from ml_data_analysis import compute_average_mass
from ml_data_analysis import check_hemisphere
from ml_data_analysis import count_classes
import pytest

def test_compute_average_mass():
    assert compute_average_mass([{'a': 1}], 'a') == 1
    assert compute_average_mass([{'a': 1}, {'a': 2}], 'a') == 1.5
    assert compute_average_mass([{'a': 1}, {'a': 2}, {'a': 3}], 'a') == 2
    assert compute_average_mass([{'a': 10}, {'a': 1}, {'a': 1}], 'a') == 4
    assert isinstance(compute_average_mass([{'a': 1}, {'a': 2}], 'a'), float) == True

def test_check_hemisphere():
    assert check_hemisphere(2, 2) == 'Northern & Eastern'
    assert check_hemisphere(2, -2) == 'Northern & Western'
    assert check_hemisphere(-2, 2) == 'Southern & Eastern'
    assert check_hemisphere(-2, -2) == 'Southern & Western'
    assert isinstance(check_hemisphere(2, 2), str) == True

def test_count_classes():
    assert count_classes([{'a': 'L5'}], 'a') == {'L5': 1}
    assert count_classes([{'a': 'L4'}], 'a') == {'L4': 1}
    assert count_classes([{'a': 'L3'}], 'a') == {'L3': 1}
    assert count_classes([{'a': 'L2'}, {'a': 'L2'}], 'a') == {'L2': 2}
    assert count_classes([{'a': 'L5'}, {'a': 'L4'}], 'a') == {'L5': 1, 'L4': 1}
