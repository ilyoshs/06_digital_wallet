import pytest
from src.wallet_withdrawal import withdraw


@pytest.mark.parametrize(
    "balance_cents, amount_cents, expected",
    [
        (1000, 500, 500),
        (1000, 1000, 0),
    ]
)
def test_valid_withdrawals_return_expected_balance(
    balance_cents,
    amount_cents,
    expected
):
    result = withdraw(balance_cents, amount_cents)

    assert result == expected


@pytest.mark.parametrize(
    "balance_cents, amount_cents, expected_exception",
    [
        (-100, 50, ValueError),
        (1000, 0, ValueError),
        (1000, -50, ValueError),
        (1000, 1500, ValueError),
        ("1000", 500, TypeError),
        (1000, "500", TypeError),
        (1000.5, 500, TypeError),
        (1000, 500.5, TypeError),
        (True, 500, TypeError),
        (1000, False, TypeError),
    ]
)
def test_invalid_inputs_raise_exception(
    balance_cents,
    amount_cents,
    expected_exception
):
    with pytest.raises(expected_exception):
        withdraw(balance_cents, amount_cents)