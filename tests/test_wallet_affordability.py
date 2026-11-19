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
    "balance_cents, price_cents, expected_exception",
    [
        (-1, 100, ValueError),
        (100, -1, ValueError),
        (-1, -1, ValueError),
        ("100", 50, TypeError),
        (100, "50", TypeError),
        (100.5, 50, TypeError),
        (100, 50.5, TypeError),
        (True, 50, TypeError),
        (100, False, TypeError),
    ]
)
def test_can_afford_invalid_inputs_raise_exception(
    balance_cents,
    price_cents,
    expected_exception
):
    with pytest.raises(expected_exception):
        can_afford(balance_cents, price_cents)