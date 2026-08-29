def convert_kg(value):
    """Convert a mass in kilograms to pounds and ounces, then print the result.

    value -- mass in kilograms (int or float)
    """
    kg_to_lb = value * 2.20462
    kg_to_oz = value * 35.274

    print(value, "kg converted is", kg_to_lb, "pounds and", kg_to_oz, "ounces.")


def convert_pounds(value):
    """Convert a mass in pounds to kilograms and ounces, then print the result.

    value -- mass in pounds (int or float)
    """
    lb_to_kg = value * 0.453592
    lb_to_oz = value * 16

    print(value, "pounds converted is", lb_to_kg, "kg and", lb_to_oz, "ounces.")


def convert_ounces(value):
    """Convert a mass in ounces to kilograms and pounds, then print the result.

    value -- mass in ounces (int or float)
    """
    oz_to_kg = value * 0.0283
    oz_to_lb = value * 0.0625

    print(value, "ounces converted is", oz_to_kg, "kg and", oz_to_lb, "pounds.")


if __name__ == "__main__":
    # Test cases
    convert_kg(10)
    convert_pounds(10)
    convert_ounces(10)