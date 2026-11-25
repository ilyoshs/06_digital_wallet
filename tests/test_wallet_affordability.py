import pytest
from src.wallet_affordability import can_afford #imports the function we want to test


@pytest.mark.parametrize( 
    "balance_cents, price_cents, expected",
    [
        (1000, 500, True),
        (1000, 1000, True),
        (0, 0, True),
        (500, 1000, False),
    ]
)
def test_can_afford_returns_expected_result( #the can_afford function with various inputs and checks if the output matches the expected result
    balance_cents,
    price_cents,
    expected
):
    result = can_afford(balance_cents, price_cents) #calls the actual function

    assert result is expected #compares the result of the function with the expected result


@pytest.mark.parametrize(
    "balance_cents, price_cents, expected_exception",
    [
        (-1, 100, ValueError), #negative balance is invalid
        (100, -1, ValueError),
        (-1, -1, ValueError),
        ("100", 50, TypeError), #string input is invalid
        (100, "50", TypeError),
        (100.5, 50, TypeError), #float input is invalid
        (100, 50.5, TypeError),
        (True, 50, TypeError), #boolean input is invalid
        (100, False, TypeError),
    ]
)
def test_can_afford_invalid_inputs_raise_exception( #verify that invalid inputs raise the expected exceptions
    balance_cents,
    price_cents,
    expected_exception
):
    with pytest.raises(expected_exception): #expects the function to raise an exception for invalid inputs
        can_afford(balance_cents, price_cents) #calls the actual function with invalid inputs