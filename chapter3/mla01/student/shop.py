HOURS_PER_DAY = 8
DAYS_PER_WEEK = 6
WEEKS_PER_MONTH = 4
LABOR_HOURS_PER_MONTH = HOURS_PER_DAY * DAYS_PER_WEEK * WEEKS_PER_MONTH

VARIANCE_PERCENT = 10
VARIANCE_STEP = 2
PRICE_STEP = 0.10


def monthly_expenses(serving_cost, labor_rate, shop_rental, utilities, advertising, servings_per_month):
    ingredient_cost = serving_cost * servings_per_month
    labor_cost = labor_rate * LABOR_HOURS_PER_MONTH
    return ingredient_cost + labor_cost + shop_rental + utilities + advertising


def monthly_income(selling_price, servings_per_month):
    return selling_price * servings_per_month


def read_number(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if value < 0:
            print("Please enter a number that is 0 or greater.")
        else:
            return value


def main():
    serving_cost = 1.00
    labor_rate = 7.50
    shop_rental = 800
    utilities = 150
    advertising = 100
    servings_per_month = 1000
    selling_price = 4.00

    while True:
        print()
        print("Expenses:")
        print(f"1. Cost per serving: {serving_cost}")
        print(f"2. Labor rate per hour: {labor_rate}")
        print(f"3. Shop rental per month: {shop_rental}")
        print(f"4. Utilities per month: {utilities}")
        print(f"5. Advertising budget per month: {advertising}")
        print()
        print("Income:")
        print(f"6. Selling price (each): {selling_price}")
        print(f"7. Servings sold per month: {servings_per_month}")
        print()
        print("Analysis:")
        print("8. Profit/Loss Calculation")
        print('9. "What If" analysis with 10% variance')
        print("10. Find Break-Even")
        print()
        selection = input("Enter Selection (0 to Exit): ").strip()

        expenses = monthly_expenses(serving_cost, labor_rate, shop_rental,
                                    utilities, advertising, servings_per_month)
        income = monthly_income(selling_price, servings_per_month)

        if selection == "0":
            break
        elif selection == "1":
            serving_cost = read_number("Enter cost per serving: ")
        elif selection == "2":
            labor_rate = read_number("Enter labor rate per hour: ")
        elif selection == "3":
            shop_rental = read_number("Enter shop rental per month: ")
        elif selection == "4":
            utilities = read_number("Enter utilities per month: ")
        elif selection == "5":
            advertising = read_number("Enter advertising budget per month: ")
        elif selection == "6":
            selling_price = read_number("Enter selling price (each): ")
        elif selection == "7":
            servings_per_month = read_number("Enter servings sold per month: ")
        elif selection == "8":
            profit = round(income - expenses, 2)
            if servings_per_month > 0:
                per_serving = round(profit / servings_per_month, 2)
                print(f"The Ice Cream Shop will have a monthly profit/loss of {profit} or {per_serving} per serving.")
            else:
                print(f"The Ice Cream Shop will have a monthly profit/loss of {profit}.")
        elif selection == "9":
            print()
            print(f"Varying the Expenses From -{VARIANCE_PERCENT}% to +{VARIANCE_PERCENT}%::")
            for percent in range(-VARIANCE_PERCENT, VARIANCE_PERCENT, VARIANCE_STEP):
                varied_expenses = round(expenses * (1 + percent / 100), 2)
                profit = round(income - varied_expenses, 2)
                print("Percent: ", percent, "Expenses: ", varied_expenses, "Profit/Loss: ", profit)

            print()
            print(f"Varying the Income From -{VARIANCE_PERCENT}% to +{VARIANCE_PERCENT}%::")
            for percent in range(-VARIANCE_PERCENT, VARIANCE_PERCENT, VARIANCE_STEP):
                varied_income = round(income * (1 + percent / 100), 2)
                profit = round(varied_income - expenses, 2)
                print("Percent: ", percent, "Income: ", varied_income, "Profit/Loss: ", profit)
        elif selection == "10":
            if servings_per_month <= 0:
                print("Servings sold must be greater than 0 to find break-even.")
            else:
                price = selling_price
                profit = income - expenses
                started_positive = profit > 0
                step = -PRICE_STEP if started_positive else PRICE_STEP

                while profit != 0 and (profit > 0) == started_positive:
                    price += step
                    profit = monthly_income(price, servings_per_month) - expenses

                print(f"Break-Even occurs with a selling price of: {round(price, 2)}")
        else:
            print("Invalid selection. Please enter a number from 0 to 10.")


if __name__ == "__main__":
    main()