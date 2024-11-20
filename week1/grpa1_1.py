# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
a = 5
b = 6
price, discount_percent = 80, 5.75
total_mins = 470
# <eoi>

output1 = a + b # int: sum of a and b
output2 = 2 * (output1) # int: twice the sum of a and b
output3 = abs(a - b) # int: absolute difference between a and b
output4 = abs(output1 - (a * b)) # int: absolute difference between sum and product of a and b
# print(output1, output2, output3, output4)

# Find discounted price given price and discount_percent
# input variables : price: int, discount_percent: float
discounted_price = (price - (price * discount_percent / 100)) # float
# print(discounted_price)

# Round the discounted_price
rounded_discounted_price = round(discounted_price) # int
# print(rounded_discounted_price)

# Find hrs and mins given the total_mins
# input variables : total_mins
hrs = total_mins // 60 # int: hint: think about floor division operator
mins = (total_mins - (hrs * 60)) # int
print(hrs, mins)