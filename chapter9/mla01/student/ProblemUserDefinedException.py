"""
User-defined exceptions for the TargetCRM mailing list validator.

Both classes extend Python's built-in Exception class. Inheriting from
Exception is what makes a class "raisable"; a plain class cannot be used
with the raise statement.
"""


class EmailNotValidError(Exception):
    """Raised when the target email is not valid."""

    def __init__(self, message="The email address is not valid."):
        """
        Initialize the exception with a descriptive message.

        Args:
            message (str): Explanation of the error, passed in by the
                function that raises it. Helps programmers debug.
        """
        self.message = message
        # Pass the message to the base Exception so str(error) returns it
        super().__init__(self.message)


class ProviderNotValidError(Exception):
    """Raised when an email's provider is blacklisted (fewer than 5 characters)."""

    def __init__(self, message="The email provider is not valid."):
        """
        Initialize the exception with a descriptive message.

        Args:
            message (str): Explanation of the error, passed in by the
                function that raises it. Helps programmers debug.
        """
        self.message = message
        super().__init__(self.message)