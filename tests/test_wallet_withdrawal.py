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
    "balance_cents, amount_cents",
    [
        (-100, 50),
        (1000, 0),
        (1000, -50),
        (1000, 1500),
    ]
)
def test_invalid_values_raise_value_error(
    balance_cents,
    amount_cents
):
    with pytest.raises(ValueError):
        withdraw(balance_cents, amount_cents)


@pytest.mark.parametrize(
    "balance_cents, amount_cents",
    [
        ("1000", 500),
        (1000, "500"),
        (1000.5, 500),
        (1000, 500.5),
        (True, 500),
        (1000, False),
    ]
)
def test_invalid_types_raise_type_error(
    balance_cents,
    amount_cents
):
    with pytest.raises(TypeError):
        withdraw(balance_cents, amount_cents)