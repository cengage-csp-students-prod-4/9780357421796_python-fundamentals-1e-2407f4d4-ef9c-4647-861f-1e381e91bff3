# Importing user-defined exception
from ProblemUserDefinedException import EmailNotValidError


def is_email_valid_extended_finally(mailing_list):
    """
    Validate emails, report errors, and always return the valid user IDs.

    The finally block runs whether or not an exception occurred, so the
    list of valid IDs collected so far is always returned.

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