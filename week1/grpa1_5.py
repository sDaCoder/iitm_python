age = int(input()) # int: Read a number as integer from standard input
dob = str(input()) # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob.split("/")[0]), int(dob.split("/")[1]), int(dob.split("/")[2]) # int, int, int: Get the correct parts from dob as int

fifth_birthday = f"{day}/{month}/{year + 5}" # str: fifth birthday formatted as day/month/year 

last_birthday = f"{day}/{month}/{year + age}" # str: last birthday formatted as day/month/year

m10 = ((month + 9) % 12) + 1
y10 = ((month + 9) // 12) + year
tenth_month = f"{day}/{m10}/{y10}" # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month, fifth_birthday, last_birthday)

weight = float(input()) # float: Read a number as float from stdin(Standard input)

weight_kg = int(weight) # float: weight in kg
weight_grams = int((weight - weight_kg) * 1000) # float: weight in grams
weight_readable = f"{weight_kg} kg {weight_grams} grams" # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)