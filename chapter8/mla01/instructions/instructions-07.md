# Trigger the file operations
This function is the main entry point to trigger the other functions to handle file operations. First, call the `read_mailing_list_file()` to read the original dataset and process it with the `update_mailing_list()` function. Then, cache the resulting active user id list. Next, call the `save_output_file()` function to persist the user ids to an output csv file.

Finally, compute the length of the output file to check if it matches the result of our previous function to update the mailing list. The template for this function is shown below:

```python
def mailinglist_validation_util(filename, output_filename, io_mode):

    """  
   Input: 
   - filename: the name of the input file with the raw mailing list
   - output_filename: the name of the final, output csv file
   - io_mode: the io operation that this function needs, passed as an array
  
   Output: Returns the output file length 
    """

  return # Return the output file length
```
