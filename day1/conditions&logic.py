

#tar1

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")


#tar2

#
# number = int(input("Enter a number: "))
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")



#tar3

# number = int(input("Enter a full number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



#tar4

# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number: "))
#
# if num2 > num1:
#     print(num2)
# elif num1 > num2:
#     print(num1)
# else:
#     print("Numbers are even!")



#tar5

# password = input("Enter password: ")
# if password == "Python123":
#     print("Access granted")
# else:
#     print("Access denied")


#tar6

# num = int(input("Enter a number: "))
# if num > 0 and num < 10:
#     print("between 1 and 10")
# elif num > 10 and num < 50:
#     print("between 11 and 50")
# elif num > 50 and num < 100:
#     print("between 50 and 100")
# else:
#     print("outside ")



#tar7

# grade = int(input("Enter your grade: "))
# if 0 < grade <= 59:
#     print("Failed")
# elif 59 < grade <= 69:
#     print("Passed")
# elif 69 < grade <= 79:
#     print("Good")
# elif 79 < grade <= 89:
#     print("Very Good")
# elif 89 < grade <= 100:
#     print("Excellent")
# else:
#     print("Number is invalid")




#tar8

# username = input("Enter username: ")
# password = input("Enter password: ")
# correct_username = "admin"
# correct_password = "123456"
#
# if username == correct_username and password == correct_password:
#     print("Login successful")
# elif username == correct_username and password != correct_password:
#     print("Wrong password")
# if username != correct_username:
#     print("unknown username")




#tar9

# age = int(input("Enter age: "))
# price = float(input("enter price: "))
# if age > 60:
#     print(f"Price is: {price - price * 0.2}")
# elif age < 18:
#     print(f"Price is: {price - price * 0.1}")
# else:
#     print(f"Price: {price}")



#tar10

# num = int(input("Enter a number: "))
# if num % 3 == 0:
#     print("Number devide by three!")
# else:
#     print("Number doesn't devide by three!")
# if num % 5 == 0:
#     print("Number devide by five!")
# else:
#     print("Number doesn't devide by three!")
# if num % 5 == 0 and num % 3 == 0:
#     print("Number devide by three and five!")
# else:
#     print("Doesn't devide by both three and five!")
# if not num % 5 == 0 and not num % 3 == 0:
#     print("Number doesn't devide by any")



#tar11


# age = int(input("Enter age: "))
# adult = bool(input("Enter 1 if there's an adult, enter 0 if you're alone: "))
# if age >= 18:
#     print("You're allowed in!")
# else:
#     if adult:
#         print("You're allowed in")
#     else:
#         print("You're not allowed in")\




#tar12

# average_grades = float(input("Enter your average grade: "))
# income = int(input("Enter your monthly income: "))
# if average_grades >= 90:
#     print("You're elligible for a scollership")
# elif average_grades >= 85 and income < 5000:
#     print("You're elligible for a scollership")
# else:
#     print("You're not elligible")



#tar13

# correct_user = "Mordy"
# correct_password = "12345"
# username = input("Enter username: ")
# password = input("Enter password: ")
# account = bool(input("Enter 1 or nothing if the account is active: "))
# if username == correct_user and password == correct_password and account:
#     print("Access granted")
# else:
#     print("Access denied")



#tar14

# num = int(input("Enter a number: "))
# if num >= 20 and num <= 80:
#     print("And check passed")
# if not (num < 20 and num < 80):
#     print("Not check passed")



#tar15


# balance = 5000
# num = int(input("Enter an amount to withdraw: "))
# if num > 0:
#     if balance > num:
#         print(f"Withdraw successfully. new balance: {balance - num}")
#     else:
#         print("Not enough money")
# else:
#     print("Error, amount must be positive!")



#tar16

# age = int(input("Enter age: "))
# subscribe = bool(input("Enter 1 if you're subscribed, else enter nothing: "))
# if age < 12:
#     if subscribe:
#         print(f"price is: {25 - 25 * 0.1}")
#     else:
#         print("Price is 25")
# elif age >= 12 and age < 18:
#     if subscribe:
#         print(f"price is: {35 - 35 * 0.1}")
#     else:
#         print("Price is 35")
# else:
#     if subscribe:
#         print(f"Price is: {50 - 50 * 0.1}")
#     else:
#         print("Price is 50")




#tar17


# age = int(input("Enter age: "))
# income = int(input("Enter income: "))
# time = float(input("Enter vetek in years: "))
#
# if age >= 21 and income >= 7000 and time >= 1:
#     print("Load is confirmed")
# else:
#     print("You're not elligible for a loan")



#tar18

# car = input("Enter type if car (private/motorcycle/company): ")
# hours = float(input("Enter number of hours you parked: "))
# if car == "motorcycle":
#     if hours <=1:
#         print(f"Price is: {9}")
#     elif hours > 5:
#         print(f"Price is: {(10 * hours) - (10 * hours) * 0.15}")
#     else:
#         print(f"Price is: {hours * 10}")
# elif car == "private":
#     if hours <= 1:
#         print(f"Price is: {20 - 20 * 0.1}")
#     elif hours > 5:
#         print(f"Price is: {20 * hours - 20 * hours * 0.15}")
#     else:
#         print(f"price is: {20 * hours}")
# elif car == "company":
#     if hours <= 1:
#         print(f"Price is: {30 - 30 * 0.1}")
#     elif hours > 5:
#         print(f"Price is: {30 * hours - 30 * hours * 0.15}")
#     else:
#         print(f"price is: {hours * 30}")
# else:
#     print("Car isn't recognized")



#tar19

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# operator = input("Enter operator (+ - * /)")
# if operator == "+":
#     print(f"Solution: {num2 + num1}")
# elif operator == "-":
#     print(f"Solution: {num1 - num2}")
# elif operator == "*":
#     print(f"Solution: {num2 * num1}")
# elif operator == "/":
#     if num2 == 0:
#         print("Error can't devide")
#     else:
#         print(f"Solution: {num1 / num2}")
# else:
#     print("Invalid operator")



#tar20


# year = int(input("Enter a year: "))
# if year % 400 == 0:
#     print("Meuberet")
# elif year % 100 == 0 and year % 400 != 0:
#     print("Meuberet")
# elif year % 4 == 0 and year % 100 != 0:
#     print("Meuberet")
# else:
#     print("Not Meuberet")



#tar21


# hours = float(input("Enter number of working hours: "))
# if hours < 182:
#     print(f"Salary: {hours * 50}")
# else:
#     bonus = hours - 182
#     if bonus > 2:
#         extra_bonus = bonus - 2
#         print(f"Salary: {182 * 50 + 2 * (50 * 1.25) + extra_bonus * (50 * 1.50)}")
#     else:
#         print(f"Salary: {182 * 50 + bonus * (50 * 1.25)}")




#tar22


# age = int(input("Enter age: "))
# total = float(input("Enter total amount: "))
# subscribed = bool(input("Enter 1 if you're subscribed or nothing of you're not: "))
# did_open = bool(input("Enter 1 if it's opened, or nothing if it's closed"))
# receipt = bool(input("Enter 1 if you have a receipt, or nothing if you don't have: "))
# days = int(input("Enter number of days that passed: "))
#
# if not receipt:
#     print("You can't return without a receipt!")
# else:
#     if did_open:
#         print("You can't return if open: ")
#     else:
#         if total <= 0:
#             print("Total must be positive!")
#         else:
#             if days > 14:
#                 if not subscribed:
#                     print("You can't return, too many days passed!")
#                 else:
#                     print(f"You can return!, amount: {total}")
#             elif days > 30:
#                 print("You can't return, too many days passed!")
#             else:
#                 print(f"You can return!, amount: {total}")











