from src.wallet_affordability import can_afford
import pytest

def test_balance_greater_than_price():
    result = can_afford(1000, 500)

    assert result is True


def test_balance_equals_price():
    result = can_afford(1000, 1000)

    assert result is True


def test_zero_balance_zero_price():
    result = can_afford(0, 0)

    assert result is True


def test_balance_less_than_price():
    result = can_afford(500, 1000)

    assert result is False
