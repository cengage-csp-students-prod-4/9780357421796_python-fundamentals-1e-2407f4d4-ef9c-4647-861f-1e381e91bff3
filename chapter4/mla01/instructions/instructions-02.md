Another functionality for the app is the ability to estimate the return on investment over a period of time. In order to implement this feature, you will have to update the investment calculator algorithm.

The base function to calculate the return on investment from Task 1 can be reutilized here to simplify our task. This feature will take into consideration a 12-month period by default.

To calculate the total amount earned over a period of time, you will have to loop through the n-months period, increase the amount for each period. The other rules from the previous task apply here as well.

For example:
If you invest $3 million on the first month, and obtain a return of $93,000 dollars, then the amount to be invested in the second month is $3.093 million.

To summarize:

- Loop over a period of 12 months to calculate the total for each period
- Return the accumulated estimated value for a period of 12 months

> Note that to calculate the accumulated value over a 12-month period do not just multiply the gain of every month by 12 (or n). In this case, the gain of every month is added to the original value, updating the amount to be invested in the subsequent month.

The following base code is given for you in the file _calculate_gains_over_time.py_:

```python
def calculate_gains_over_time(amount_inv=0.0, period=12):
    """
    Calculating the return gains of a given amount invested based on a period of application.
    :param amount_inv: the money amount invested
    :param period: application period
    :return:
    """

    # call the base `calculate_gains` function to estimate the gains for the first period

    # calculate the first period before entering the loop

    # loop through the specified period to calculate the gain of each month

    # 1 to period-1 because the first period gains is already calculated above

        # call the function to update the value based on the period inside the loop and the updated amount

        new_amount = total_amount  # update the `new_amount` variable

    # return the final ammount
    return new_amount


print(calculate_gains_over_time(amount_inv=4000000, period=12))
```
