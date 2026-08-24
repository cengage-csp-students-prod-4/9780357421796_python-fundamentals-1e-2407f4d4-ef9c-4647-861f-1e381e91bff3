# Read the data from the CSV
Create a function called `read_mailing_list_file()` that reads in the original dataset from a 'csv' file, transforms it in a python dictionary, and pass the data to the `update_mailing_list()` function to filter out the 'unsubscribed' users. After that, we return the ids of the active users. The template for this function is shown below:

```python
def read_mailing_list_file(filename, io_mode):
   
    """
    Input: 
   - filename: the filename of the original dataset we are going to read the data from.
   - io_mode: the `input/output` mode we will use to handle the file operation.
  
    Output: the list of ids of the active users.
    """

    return # Return the resulting ids of the active users
```