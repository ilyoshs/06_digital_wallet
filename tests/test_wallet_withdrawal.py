from src.wallet_withdrawal import withdraw
import pytest

def test_valid_withdrawal():
    # Arrange
    balance_cents = 1000
    amount_cents = 500

    # Act
    result = withdraw(balance_cents, amount_cents)

    # Assert
    assert result == 500


def test_exact_balance_withdrawal_returns_zero():
    # Arrange
    balance_cents = 1000
    amount_cents = 1000

    # Act & Assert
    assert withdraw(balance_cents, amount_cents) == 0

@pytest.mark.parametrize(
    "balance_cents, amount_cents",
    [
        (-100, 50),
        (1000, 0),
        (1000, -50),
        (1000, 1500),
    ]
)
def test_invalid_range_raises_value_error(balance_cents, amount_cents):
    with pytest.raises(ValueError):
        withdraw(balance_cents, amount_cents)



