from calculate_gains import calculate_gains


def calculate_gains_over_time(amount_inv=0.0, period=12):
    """
    Calculating the return gains of a given amount invested based on a period of application.
    :param amount_inv: the money amount invested
    :param period: application period
    :return: the final accumulated amount
    """

    # call the base `calculate_gains` function to estimate the gains for the first period
    # calculate the first period before entering the loop
    _, total_amount, _ = calculate_gains(amount_inv)
    new_amount = total_amount

    # loop through the specified period to calculate the gain of each month
    # 1 to period-1 because the first period gains is already calculated above
    for month in range(1, period):
        # call the function to update the value based on the period inside the loop and the updated amount
        _, total_amount, _ = calculate_gains(new_amount)

        new_amount = total_amount  # update the `new_amount` variable

    # return the final amount
    return new_amount


print(calculate_gains_over_time(amount_inv=4000000, period=12))