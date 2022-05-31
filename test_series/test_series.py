import pytest
from series.series import fibonacci, lucas, sum_series


def test_fibonacci():
    """
    This function tests the fibonacci function from "series.py" file
    """
    assert str(fibonacci(7)) == '13'
    assert str(fibonacci(2)) == '1'
    assert str(fibonacci(8)) == '21'
    assert str(fibonacci(12)) == '144'


def test_lucas():
    """
    This function tests the lucas function from "series.py" file
    """
    assert str(lucas(7)) == '29'
    assert str(lucas(2)) == '3'
    assert str(lucas(8)) == '47'
    assert str(lucas(12)) == '322'


def test_sum_series():
    """
    This function tests the sum_series function from "series.py" file
    """
    assert str(sum_series(7)) == '13'
    assert str(sum_series(2)) == '1'
    assert str(sum_series(8)) == '21'
    assert str(sum_series(12)) == '144'

    assert str(sum_series(7, 2, 1)) == '29'
    assert str(sum_series(2, 2, 1)) == '3'
    assert str(sum_series(8, 2, 1)) == '47'
    assert str(sum_series(12, 2, 1)) == '322'

    assert str(sum_series(7, 5, 2)) == '66'
    assert str(sum_series(2, 5, 2)) == '7'
    assert str(sum_series(8, 5, 2)) == '107'
    assert str(sum_series(12, 5, 2)) == '733'
    # 5, 2, 7, 9, 16, 25, 41, 66, 107, 173, 280, 453, 733
    # out 66, 7, 107, 733
