# Updated the mailing list
Create a python function called `update_mailing_list` to update the original mailing list passed as parameter and filter the invalid email addresses. The function stub can be found in the *update_mailing_list.py* file. Consider the rules below to filter out (and update) the original mailing list:

* Remove users that contain the attributes "opt-out", "unsubscribed", or "OPT-OUT" from the list (hint: use str.lower() to transform strings to lowercase)
* The system only sends messages to corporate emails, so filter out 'gmail' users
* Return a list of the user ids that are able to be notified, that is, the remaining users

```python
def update_mailing_list(mailing_list):
    """
    Input: mailing_list: the original mailing list with all the users as a python's dictionary

    Output: the list of ids of the active users
    """
    return # Return the resulting ids of the active users
```
