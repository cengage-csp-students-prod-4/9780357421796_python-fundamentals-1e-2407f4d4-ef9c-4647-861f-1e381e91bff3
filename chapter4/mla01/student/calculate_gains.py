# global variable
multiplier_amount = 1000000  # threshold that triggers a higher gain margin


def calculate_gains(amount_inv=0.0):
    """ Calculating the return gains of an investment.

    :param amount_inv: the money amount invested
    :return: tuple of (total_gains, total_amount, gain_margin)
    """

    # base amount gain margin
    gain_margin = 0.001  # 0.1%
    total_gains = 0
    total_amount = 0

    if amount_inv > 1000:

        # check whether the invested amount is greater than the multiplier amount
        if amount_inv > multiplier_amount:
            # gather the value of the division (full millions only)
            multiplier = amount_inv // multiplier_amount

            # update the `gain_margin` by the multiplier (1% per million), capped at 100%
            gain_margin = min(round(gain_margin + multiplier / 100, 3), 1.0)

        # calculate the total amount of gains
        total_gains = amount_inv * gain_margin

        # calculate the total amount plus the gain margin
        total_amount = amount_inv + total_gains

    # return the gains, the full amount and the gain margin
    return total_gains, total_amount, gain_margin


if __name__ == "__main__":
    print(calculate_gains(amount_inv=2000000))