# How to solve: To solve this problem use the Python tutor button. Paste the template(buggy) code in the python tutor, you can also include the sample input in the python tutor. This will help you identify the errors easily.

# Useful Tips while dealing with indentation

# You can indent or detent a line using the keyboard shortcut CTRL+] and CTRL+[ respectively.
# To indent or detent a whole block select the block and use the above short cuts.
# Useful Keyboard shortcuts for selecting

# Use arrow keys to move the cursor in the left, right, up and down directions
# Hold Ctrl+ left or right arrow to move the cursor by words
# Hold shift key while moving using the above methods to select the contents.
# Problem Statement

# Write a program to calculate the cost of a meal at a restaurant.

# The cost of the meal depends on the main dish and the time of the day.
# Main dishes available:
    # "paneer tikka": ₹250
    # "butter chicken": ₹240
    # "masala dosa": ₹200

# Additional discounts:
    # 15% discount for meals ordered during lunchtime (from 12 PM to 3 PM).
    # Customers can apply vouchers for an additional 10% discount on the total cost.
    # The restaurant accepts card payments.
    # For card payments, there's an additional service charge of 5% on the total cost after applying any discounts.

# Take the following inputs:
    # Main dish : str
    # Time of the day: int: 24-hour format
    # Whether the customer has a voucher: bool: True/False
    # Whether the payment is by card: bool: True/False
# Calculate and display the total cost of the meal.


main_dish = input()
time_of_day = int(input())
has_voucher = input().lower() == 'true'
is_card_payment = input().lower() == 'true'

if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else: # if main dish is invalid print invalid dish and exit the code.
    print("Invalid main dish")
    exit() 

if time_of_day >= 12 and time_of_day <= 15:
    total_cost = cost - cost * 0.15
else:
    total_cost = cost

if has_voucher == True:
    total_cost = total_cost - 0.1 * total_cost  # Apply voucher discount

if is_card_payment == True:  # service charge for card payments
    service_charge = 0.05 * total_cost
    total_cost = total_cost + service_charge

print(f"{total_cost:.2f}")