def update_mailing_list(mailing_list):
    """
    Filter a mailing list dictionary down to the users who can be notified.

    Input:
        mailing_list: dict mapping each user's uuid to their remaining fields,
                      e.g. {uuid: [username, email, subscribe_status]}

    Output:
        list of uuids for active, non-gmail users
    """
    # Iterate over a copy so we can safely delete from the original
    mailing_list_copy = mailing_list.copy()

    for key, value in mailing_list_copy.items():
        email = value[1].lower()
        status = value[2].lower()

        # Remove opted-out / unsubscribed users and gmail addresses
        if status == 'opt-out' or status == 'unsubscribed' or '@gmail' in email:
            del mailing_list[key]

    ids = []

    # Collect the ids of the remaining active users
    for key, value in mailing_list.items():
        if value[2].lower() == 'active':
            ids.append(key)

    return ids


# Alias so the stub's original name also works
update_mailing_list_extended = update_mailing_list