# Import library to work with regex patterns
import re

# Import user-defined exception
from ProblemUserDefinedException import EmailNotValidError


def is_email_valid_optional_regex(mailing_list):
    """
    Validate emails with a regular expression instead of an '@' check alone.

    The regex catches malformed addresses such as 'john@gmail' (no domain
    extension) and '@email.com' (no local part).

    Args:
        mailing_list (dict): Maps user IDs to email addresses.

    Returns:
        list: The IDs of users whose emails passed validation before the
            first invalid email was found.
    """
    # Array to hold user ids
    final_users_list = []

    # The regex pattern to validate emails, piece by piece:
    #   [A-Za-z0-9._%+-]+   local part: one or more allowed characters
    #   @                   a literal '@'
    #   [A-Za-z0-9.-]+      domain name, e.g. 'gmail'
    #   \.                  a literal dot (escaped, since '.' alone means "any character")
    #   [A-Za-z]{2,}        top-level domain of 2+ letters, e.g. 'com'
    regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    # Inserted a try.., except.. block to catch the exception
    try:
        # Loop through the mailing list
        for key, email in mailing_list.items():

            # Check if the @ is present AND the whole email matches the pattern.
            # re.fullmatch requires the ENTIRE string to match; re.match would
            # only check the beginning and let trailing garbage through.
            if '@' in email and re.fullmatch(regex, email):

                # Append the id of users with valid emails
                final_users_list.append(key)

            else:

                # Raises an EmailNotValidError otherwise
                raise EmailNotValidError(
                    f"User {key} has an invalid email format: '{email}'."
                )

    except EmailNotValidError as error:

        # Print a user-friendly message describing the exception.
        # (A return here would be overridden by the return in finally.)
        print(f"Validation stopped. {error}")

    finally:

        # Return the id of the users with valid email
        print("Fart")
    return final_users_list