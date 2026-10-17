# Importing re library
import re

# Importing user-defined exceptions
from ProblemUserDefinedException import ProviderNotValidError

# Regex pattern shared by both functions (see optional_part1 for a breakdown)
EMAIL_REGEX = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

# Providers shorter than this are considered suspicious/blacklisted
MIN_PROVIDER_LENGTH = 5


def get_provider(email):
    """
    Extract the provider name from an email address.

    Example: 'john@gmail.com' -> split on '@' -> 'gmail.com'
                              -> split on '.' -> 'gmail'

    Args:
        email (str): A correctly formatted email address.

    Returns:
        str: The provider name.
    """
    domain = email.split('@')[1]
    return domain.split('.')[0]


def is_provider_valid_blacklist_optional_len(mailing_list):
    """
    Return the IDs of users with a valid email format and an allowed provider.

    A provider with fewer than 5 characters is treated as blacklisted. The
    try/except sits INSIDE the loop, so one blacklisted provider is reported
    and skipped without stopping the checks on the remaining users.

    Args:
        mailing_list (dict): Maps user IDs to email addresses.

    Returns:
        list: The IDs of users who can receive communications.
    """
    # Array to hold user ids
    final_users_list = []

    # Loop through the mailing list
    for key, email in mailing_list.items():

        # Check if the @ is present in the email and the email passes the regex pattern
        if '@' in email and re.fullmatch(EMAIL_REGEX, email):

            # Extract only the provider from the email string
            provider = get_provider(email)

            # Inserted a try.., except.. block to catch the exception
            try:
                # Check if the provider contains at least 5 characters
                if len(provider) >= MIN_PROVIDER_LENGTH:

                    # Append the id of users with email addresses with valid providers
                    final_users_list.append(key)

                else:
                    raise ProviderNotValidError(
                        f"User {key} has a blacklisted provider: '{provider}' "
                        f"(fewer than {MIN_PROVIDER_LENGTH} characters)."
                    )

            except ProviderNotValidError as error:

                # Print a user-friendly message and move on to the next user
                print(f"Skipped. {error}")

    return final_users_list


def is_provider_valid_blacklist_optional_exception(mailing_list):
    """
    Validate providers and raise ProviderNotValidError on a blacklisted one.

    Unlike the _len version, this function does not catch the exception:
    the first blacklisted provider stops execution and the caller must
    handle the error.

    Args:
        mailing_list (dict): Maps user IDs to email addresses.

    Returns:
        list: The IDs of users who can receive communications, if no
            blacklisted provider is found.

    Raises:
        ProviderNotValidError: If a provider has fewer than 5 characters.
    """
    # Array to hold user ids
    final_users_list = []

    # Loop through the mailing list
    for key, email in mailing_list.items():

        # Check if the @ is present in the email and the email passes the regex pattern
        if '@' in email and re.fullmatch(EMAIL_REGEX, email):

            # Extract only the provider from the email string
            provider = get_provider(email)

            # Check if the provider contains fewer than 5 characters
            if len(provider) < MIN_PROVIDER_LENGTH:

                # Raise the custom-defined exception
                raise ProviderNotValidError(
                    f"User {key} has a blacklisted provider: '{provider}' "
                    f"(fewer than {MIN_PROVIDER_LENGTH} characters)."
                )

            # Append the id of users with valid emails and providers
            final_users_list.append(key)

    return final_users_list