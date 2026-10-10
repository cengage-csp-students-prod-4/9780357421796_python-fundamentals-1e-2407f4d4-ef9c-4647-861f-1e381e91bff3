# Import the mailing list utilities module
import modules_package_file as mailing_list_utils


def mailing_list_utils_extended():
    """
    Test the mailing_list_utils module by running the full pipeline.

    Output:
        length of the output file produced by mailinglist_validation_util
    """
    return mailing_list_utils.mailinglist_validation_util(
        'mailing_list.csv', 'output.csv', ['r+', 'w+']
    )


if __name__ == '__main__':
    # Calling the function from your package
    print('The output file has length {}.'.format(mailing_list_utils_extended()))