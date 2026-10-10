import csv

# Import the mailing list updater from the appropriate file
from update_mailing_list import update_mailing_list

# Global variable to set the base path to our dataset folder
base_url = '../dataset/'


def read_mailing_list_file(filename, io_mode):
    """
    Read the raw mailing list csv, convert it to a dictionary, and filter it.

    Input:
        filename: name of the original dataset file
        io_mode: file mode used to open the file (e.g. 'r+')

    Output:
        list of ids of the active users
    """
    with open(base_url + filename, io_mode) as csv_file:
        file_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0
        mailing_list = []

        for row in file_reader:
            # Skip the header row (line 0) and any blank lines
            if line_count != 0 and row:
                mailing_list.append(row)
            line_count += 1

    mailing_list_buffer = []

    for item in mailing_list:
        # (uuid, [username, email, subscribe_status])
        mailing_list_buffer.append((item[0], item[1:]))

    mailing_dict = dict(mailing_list_buffer)

    updated_mailing_list_ids = update_mailing_list(mailing_dict)

    return updated_mailing_list_ids


def save_output_file(updated_mailing_list, output_filename, io_mode):
    """
    Write the active user ids to an output csv file, one id per row.

    Input:
        updated_mailing_list: list of active user ids
        output_filename: name of the output csv file
        io_mode: file mode used to open the file (e.g. 'w+')

    Output:
        None. Results are written to the output file.
    """
    with open(base_url + output_filename, io_mode, newline='') as active_users_file:
        csv_writer = csv.writer(active_users_file)

        for user_id in updated_mailing_list:
            csv_writer.writerow([user_id])


def mailinglist_validation_util(filename, output_filename, io_mode):
    """
    Read, filter, and persist the mailing list, then verify the output.

    Input:
        filename: name of the raw mailing list file
        output_filename: name of the output csv file
        io_mode: list of modes, [read_mode, write_mode], e.g. ['r+', 'w+']

    Output:
        number of lines in the output file
    """
    updated_mailing_list = read_mailing_list_file(filename, io_mode[0])

    save_output_file(updated_mailing_list, output_filename, io_mode[1])

    output_file = open(base_url + output_filename, 'r')

    output_file_length = len(output_file.readlines())

    output_file.close()

    return output_file_length