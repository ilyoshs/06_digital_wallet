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

@pytest.mark.parametrize(
    "balance_cents, price_cents",
    [
        (-1, 100),
        (100, -1),
        (-1, -1),
    ]
)
def test_negative_values_raise_value_error(balance_cents, price_cents):
    with pytest.raises(ValueError):
        can_afford(balance_cents, price_cents)

@pytest.mark.parametrize(
    "balance_cents, price_cents",
    [
        ("100", 50),
        (100, "50"),
        (100.5, 50),
        (100, 50.5),
        (True, 50),
        (100, False),
    ]
)
def test_invalid_type_raises_type_error(balance_cents, price_cents):
    with pytest.raises(TypeError):
        can_afford(balance_cents, price_cents)
