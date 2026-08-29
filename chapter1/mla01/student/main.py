def convert_kg(value):
    kg_to_lb = value * 2.20462
    kg_to_oz = value * 35.274

    print(value, "kg converted is", kg_to_lb, "pounds and", kg_to_oz, "ounces.")


def convert_pounds(value):
    lb_to_kg = value * 0.453592
    lb_to_oz = value * 16

    print(value, "pounds converted is", lb_to_kg, "kg and", lb_to_oz, "ounces.")


def convert_ounces(value):
    oz_to_kg = value * 0.0283
    oz_to_lb = value * 0.0625

    print(value, "ounces converted is", oz_to_kg, "kg and", oz_to_lb, "pounds.")


if __name__ == "__main__":
    convert_kg(10)
    convert_pounds(10)
    convert_ounces(10)