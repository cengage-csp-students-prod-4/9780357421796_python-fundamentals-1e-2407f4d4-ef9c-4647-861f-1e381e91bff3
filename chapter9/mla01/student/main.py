"""
TargetCRM mailing list validator.

Contains the EmailNotValidError exception and three versions of the email
validator, each adding a level of exception handling:
    1. is_email_valid                   -> raises, no handling (crashes)
    2. is_email_valid_extended          -> try/except, returns a message
    3. is_email_valid_extended_finally  -> try/except/finally, returns valid IDs
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


def is_email_valid(mailing_list):
    """
    Check that every email in the mailing list contains an '@' symbol.

    This version does NOT handle the exception: the first invalid email
    stops the program.

    Args:
        mailing_list (dict): Maps user IDs to email addresses.

    Raises:
        EmailNotValidError: If an email does not contain '@'.
    """
    # Loop through the mailing list; .items() yields (key, value) pairs
    for key, email in mailing_list.items():

        # Check if the email contains an @
        if '@' not in email:

            # Raise the custom exception, naming the offending user and email
            raise EmailNotValidError(
                f"User {key} has an invalid email address: '{email}' (missing '@')."
            )


def is_email_valid_extended(mailing_list):
    """
    Validate emails and catch EmailNotValidError instead of crashing.

    Args:
        mailing_list (dict): Maps user IDs to email addresses.

    Returns:
        str: A user-friendly error message if an invalid email is found.
        list: The IDs of users with valid emails if every email is valid.
    """
    # Array to hold user ids
    final_users_list = []

    # Inserted a try.., except.. block to catch the exception
    try:

        # Loop through the mailing list
        for key, email in mailing_list.items():

            # Check if the @ is present in the email
            if '@' in email:

                # Append the id of users with valid emails
                final_users_list.append(key)

            else:

                # Raises an EmailNotValidError otherwise
                raise EmailNotValidError(
                    f"User {key} has an invalid email address: '{email}' (missing '@')."
                )

    except EmailNotValidError as error:

        # Return a user-friendly message describing the exception
        return f"Validation stopped. {error}"

    # Reached only if no exception was raised: every email was valid
    return final_users_list


def is_email_valid_extended_finally(mailing_list):
    """
    Validate emails, report errors, and always return the valid user IDs.

    Args:
        mailing_list (dict): Maps user IDs to email addresses.

    Returns:
        list: The IDs of users whose emails passed validation.
    """
    # Array to hold user ids
    final_users_list = []

    # Inserted a try.., except.. block to catch the exception
    try:
        # Loop through the mailing list
        for key, email in mailing_list.items():

            # Check if the @ is present in the email
            if '@' in email:

                # Append the id of users with valid emails
                final_users_list.append(key)

            else:

                # Raises an EmailNotValidError otherwise
                raise EmailNotValidError(
                    f"User {key} has an invalid email address: '{email}' (missing '@')."
                )

    except EmailNotValidError as error:

        # Print a user-friendly message describing the exception
        print(f"Validation stopped. {error}")

    finally:

        # Return the id of the users with valid email.
        # This runs no matter what happened in try/except.
        print("fart") 
    return final_users_list


# Demo: runs only when this file is executed directly, not when imported
if __name__ == "__main__":
    sample_list = {
        1: "ana@gmail.com",
        2: "luis@outlook.com",
        3: "john.gmail.com",    # invalid: no '@'
        4: "maria@yahoo.com",
    }

    print("extended:", is_email_valid_extended(sample_list))
    print("extended_finally:", is_email_valid_extended_finally(sample_list))

    try:
        is_email_valid(sample_list)
    except EmailNotValidError as error:
        print("is_email_valid raised:", error)