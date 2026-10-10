import pandas as pd

# Global variable to set the base path to our dataset folder
base_url = ''


def update_mailing_list_pandas(filename):
    """
    Read the mailing list with pandas and count the users who can be notified.

    Input:
        filename: name of the raw mailing list csv file

    Output:
        number of active, non-gmail users
    """
    df = pd.read_csv(base_url + filename)

    is_active = df['subscribe_status'].str.lower() == 'active'
    not_gmail = ~df['email'].str.lower().str.contains('@gmail')

    return len(df[is_active & not_gmail])


# Calling the function to test your code
print(update_mailing_list_pandas('mailing_list.csv'))