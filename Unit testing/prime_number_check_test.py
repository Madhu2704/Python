from prime_number_check import is_prime
import pytest
# make sure to start function name with test

test_cases_is_prime = [(3, True), (1234, False), (45, False), (12, False)]


@pytest.mark.parametrize('inputNum, expected', test_cases_is_prime)
def test_is_prime(inputNum, expected):
    assert is_prime(inputNum) == expected


def test_is_prime_output_type():
    assert type(is_prime(8)) is bool
