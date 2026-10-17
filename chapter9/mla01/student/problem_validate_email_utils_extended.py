# Importing user-defined exception
from ProblemUserDefinedException import EmailNotValidError


def is_email_valid_extended(mailing_list):
    """
    Validate emails and catch EmailNotValidError instead of crashing.

    When an invalid email is found, the exception is caught and a
    user-friendly message is returned. Note: the loop stops at the first
    invalid email, so later emails are never checked.

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

    # Catch only our specific exception, never a bare except
    except EmailNotValidError as error:

        # Return a user-friendly message describing the exception
        return f"Validation stopped. {error}"

    # Reached only if no exception was raised: every email was valid
    return final_users_list