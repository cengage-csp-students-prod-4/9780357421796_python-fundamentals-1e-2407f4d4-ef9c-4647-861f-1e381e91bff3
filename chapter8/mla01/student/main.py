# Import mailinglist_validation_util from your package
from your_package import your_module


def update_mailing_list(mailing_list):
     """
       Your docstring documentation starts here.

       For more information on how to proper document your function, please refer to the official PEP8:
        https://www.python.org/dev/peps/pep-0008/#documentation-strings.

    """

     # Checks it the flag `opt-out` is present. You can use lower() to lowercase the flags and contemplate both
     # `opt-out` and `OPT-OUT` cases
     # Then, checks for the presence of the `unsubscribed` flag Finally,
     # checks if the email address contains `@gmail` provider
     for key, value in mailing_list_copy.items():

         # Your conditional logic to filter out the unsubscribed users
         if ():
     # Remove the key if one of the above conditions is satisfied


    # An array to collect the final output
    ids = []

    # Loop through the updated mailing list and append the ids of the active users to the `id` list
    for key, value in  # Your updated dictionary:
    # Append only the ids of the active users

    # Returns the updated mailing list with the active users
    return ids




def mailing_list_utils_extended():
     """
       Your docstring documentation starts here.

    """
    return # Returning the output of the `mailinglist_validation_util` function


import csv

# Import the mailing list updater from the appropriate file
from functions_package import mailing_list_function

# Global variable to set the base path to our dataset folder
base_url = '../dataset/'


def read_mailing_list_file(filename, io_mode):
     """
       Your docstring documentation starts here.

    

    """

    # Open the file with the `with` context manager
    with open(the_url, the_io_mode) as csv_file:


        file_reader = # Open the csv file, passing the ',' delimiter, which is generally the case for csv files


        line_count = # Declare a counter to control the number of lines from dataset (this is useful to skip the
        # header row and print only the data values)


        mailing_list = # Declare a list variable to hold the rows read from file

        # Looping through each row of the file
        for row in file_reader:

            if # Check if the line is not the header row:
                # Append each line to the `mailing_list` variable, excluding the header


            line_count += # Increment the variable in 1


    mailing_list_buffer =  # Create another list variable that will be used as a temporary buffer to transform
    # our previous list into a dictionary, which is the data structure expected from the `update_mailing_list_extended`
    # function

    # Looping through the mailing list object
    for item in mailing_list:
        # Creating tuples with each row in the original list


    mailing_dict = # Transforming the list of tuples into a python dictionary


    updated_mailing_list_ids = # Call the `update_mailing_list_extended` from chapter 4 passing the mailing
    #  list dictionary


    return # Return the resulting ids of the active users


def save_output_file(updated_mailing_list, output_filename, io_mode):
     """
       Your docstring documentation starts here.



    """

    # Open the output file with the `with` context manager
    with open(base_url + output_filename, io_mode) as active_users_file:

        csv_writer = # Create a csv_writer object that will be responsible to persist the active users ids to a
        # resulting csv file

        # Write each user id as a new row to the file


def mailinglist_validation_util(filename, output_filename, io_mode):
     """
       Your docstring documentation starts here.
    """


    updated_mailing_list =  # Call the function to read the original mailing list file
    #  and cache the results from the function

    # Call the function to write the results back to a csv file
    save_output_file(...)


    output_file = # Open output file to count the number of lines written


    output_file_length = # Compute the length of the output file

    # Closing the output file

    return # Return the output file length


if __name__ == '__main__':
    # Calling the function from your package
    print('The output file has length {}.'.format(mailing_list_utils_extended()))
