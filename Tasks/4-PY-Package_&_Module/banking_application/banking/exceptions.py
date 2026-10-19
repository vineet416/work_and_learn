# Custom exceptions for the banking application

class InvalidAmountError(Exception):
    """Raised when the amount is zero or negative."""
    pass


class InsufficientBalanceError(Exception):
    """Raised when the account does not have enough balance."""
    pass
