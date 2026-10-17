# Importing user-defined exception
from ProblemUserDefinedException import EmailNotValidError


def is_email_valid(mailing_list):
    """
    Check that every email in the mailing list contains an '@' symbol.

    This version does NOT handle the exception: the first invalid email
    stops the program. That is intentional; later versions add handling.

    Args:
        mailing_list (dict): Maps user IDs to email addresses,
            e.g. {1: "ana@gmail.com", 2: "bob.gmail.com"}.

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