def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after discount (if applicable), otherwise the original price
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        print(f"Discount applied: ${discount_amount:.2f}")
        return final_price
    else:
        print("No discount applied.")
        return price

# Get user input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(price, discount_percent)
    
    print(f"Final price: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numerical values.")
