import pytest
from src.wallet_withdrawal import withdraw #imports the function we want to test


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
    result = withdraw(balance_cents, amount_cents) #calls the actual function

    assert result == expected #compares the result of the function with the expected result


@pytest.mark.parametrize(
    "balance_cents, amount_cents, expected_exception",
    [
        (-100, 50, ValueError), #negative balance is invalid
        (1000, 0, ValueError), #withdrawal amount must be greater than zero
        (1000, -50, ValueError), #withdrawal amount must be positive
        (1000, 1500, ValueError), #withdrawal amount cannot exceed balance
        ("1000", 500, TypeError), #string input is invalid
        (1000, "500", TypeError),
        (1000.5, 500, TypeError), #float input is invalid
        (1000, 500.5, TypeError),
        (True, 500, TypeError), #boolean input is invalid
        (1000, False, TypeError),
    ]
)
def test_invalid_inputs_raise_exception(
    balance_cents,
    amount_cents,
    expected_exception
):
    with pytest.raises(expected_exception): #expects the function to raise an exception for invalid inputs
        withdraw(balance_cents, amount_cents) #calls the actual function with invalid inputs