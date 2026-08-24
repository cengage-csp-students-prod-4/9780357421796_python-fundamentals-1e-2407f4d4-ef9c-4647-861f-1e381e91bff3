# Add Profit/Loss functionality

At this point, your script should allow the user to input values for all the variables needed to calculate the profit (or loss) of Abby’s Ice Cream business. To add this functionality, start by adding the menu item

```
8. Profit/Loss Calculation
```

under the **Analysis** section of the menu. If the user selects option **8**, the script should display something like the following:

```
Enter Selection (0 to Exit): 8
The Ice Cream Shop will have a monthly profit/loss of 90.0 or 0.18 per serving.
```

In order to perform these calculations, you’ll have to think back to Algebra and calculate things like the total expenses and the total income on a monthly basis. Finally, in order to keep the values in monetary precision, you can use the `round()` function with a precision of **2**.
