import pytest
from src.wallet_affordability import can_afford


@pytest.mark.parametrize(
    "balance_cents, price_cents, expected",
    [
        (1000, 500, True),
        (1000, 1000, True),
        (0, 0, True),
        (500, 1000, False),
    ]
)
def test_can_afford_returns_expected_result(
    balance_cents,
    price_cents,
    expected
):
    result = can_afford(balance_cents, price_cents)

    assert result is expected


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