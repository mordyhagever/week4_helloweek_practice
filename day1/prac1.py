
#tar1

# first_name = "David"
# last_name = "Cohen"
# age = 25
# city = "Tel Aviv"
# email = "david@gmail.com"
#
# print(f"""
# ======== User Details ========
# First Name: {first_name}
# Last Name: {last_name}
# Age: {age}
# City: {city}
# Email: {email}
# ============================
# """)


#tar2

# birth_year = 2005
# current_year = 2026
#
# print(f"You are approximately {current_year - birth_year} years old")


#tar3

# height = 5
# width = 7
# area = height * width
# scope = height * 2 + width * 2
# print(f"The area is: {area}, The scope is: {scope}")


#tar4

# name = "David"
# age = 25
# height = 1.78
# is_student = True
# salary = 8500
# print(f"Name is: {name}, Type is {type(name)}")
# print(f"age is: {age}, Type is: {type(age)}")
# print(f"height is: {height}, Type is: {type(height)}")
# print(f"is_student is: {is_student}, Type is: {type(is_student)}")
# print(f"Salary is: {salary}, type is {type(salary)}")


#tar5

# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# city = input("Enter your city: ")
# age = input("Enter you age: ")
# print(f"Welcome: {first_name} {last_name}. city: {city}. age: {age}")



#tar6

# number1 = input("Enter two numbers: ")
# number2 = input()
# try:
#     int(number1)
#     int(number2)
# except ValueError:
#     print("Number are invalid")
# number1 = int(number1)
# number2 = int(number2)
# print(f"Plus = {number1 + number2}")
# print(f"Minus = {number1 - number2}")
# print(f"Multi = {number1 * number2}")
# print(f"Div = {number1 / number2}")



#tar7

# product_name = input("Enter product's name: ")
# price = input("Enter product's price: ")
# amount = input("Enter amount of products: ")
# try:
#     price = float(price)
#     amount = int(amount)
#     print(f"""
#     ====== Purchase Receipt ======
#     Product: {product_name}
#     Price: {price}
#     Quantity: {amount}
#     Total: {price * amount}
#     """)
# except ValueError:
#     print("Price or amount aren't numbers")


#tar9

# worker_name = input("Enter worker name: ")
# number_of_hours = input("Enter number of hours in a month: ")
# paid_per_hour = input("Enter amount of paid per hour: ")
# try:
#     number_of_hours = float(number_of_hours)
#     paid_per_hour = float(paid_per_hour)
#     print(f"""
# ======= Salary =======
# Worker_name: {worker_name}
# Number of hours: {number_of_hours}
# Salary: {paid_per_hour * number_of_hours}
# """)
# except ValueError:
#     print("Hours or paying wasn't valid")


#tar10

# check_number = input("Enter check number: ")
# tip_percentage = input("Enter amount of tip: ")
# number_of_people = input("Enter number of people: ")
# try:
#     check_number = float(check_number)
#     tip_percentage = float(tip_percentage)
#     number_of_people = int(number_of_people)
#     print(f" Tip amount: {tip_percentage / 100 * check_number}")
#     total = check_number + tip_percentage / 100 * check_number
#     print(f"Total amount: {total}")
#     print(f"Amount for each person: {total / number_of_people}")
# except ValueError:
#     print("One og the numbers was invalid")



#tar12

# a = 10
# b = 20
# switcher = a
# a = b
# b = switcher
# print(a, b)


#tar13

first_name = input("Enter first name: ")
last_name=  input("Enter last name: ")
age = input("Enter age: ")
school_name = input("Enter school name: ")
course_name = input("Enter course name: ")
months = int(input("Enter number of months: "))
monthly_price = float(input("Enter monthly price: "))
print(f"""
    ================================
        Student registration
    =================================
    
    Student: {first_name} {last_name}
    Age: {age}
    Institution: {school_name}
    Course: {course_name}
    Duration: {months}
    Monthly price: {monthly_price}
    
    Total Course Price: {monthly_price * months}
""")




