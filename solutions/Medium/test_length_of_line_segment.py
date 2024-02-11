import pytest

from Medium.length_of_line_segment import line_length

def test_on_two_valid_arguments():
    actual = line_length([15,7], [22,11])
    expected = 8.06
    message = "Actual {0} is not equal to expected {1}".format(actual, expected)
    assert isinstance(actual, float)
    assert actual == pytest.approx(expected), message