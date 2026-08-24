# Save the active users to a new file
Create a function, called save_output_file() that is going to save the output from the read_mailing_list_file function with the ids of the active users into a file. The template for this function is shown below:

```python
def save_output_file(updated_mailing_list, output_filename, io_mode):

    """
    Input: 
   - updated_mailing_list: the list of ids of the active users in our CRM system database after filtered out the "unsubscribed" users.
   - output_filename: the name of the output file that will persist the users ids.
   - io_mode: the `input/output` mode we will use to handle the file operation.
  
    Output: This function does not return anything. Instead, write the results into an output csv file.
    """

    # Write each user id as a new row to the file
```