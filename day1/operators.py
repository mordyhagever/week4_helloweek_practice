# #tar1
import token

# num1 = 25
# num2 = 7

# print(f"Plus: {num2 + num1}")
# print(f"Minus: {num1 - num2}")
# print(f"Multi: {num2 * num1}")
# print(f"Div: {num1 / num2}")
# print(f"Full div: {num1 // num2}")
# print(f"Rest: {num1 % num2}")
# print(f"Square: {num1 ** num2}")


#tar2

# balance = 1000
# add_250 = balance + 250
# minus_100 = balance - 100
# multi_by2 = balance * 100
# div_by4 = balance / 4
# print(f"1: {add_250}\n"
#       f"2: {minus_100}\n"
#       f"3: {multi_by2}\n"
#       f"4: {div_by4}\n")


#tar3

# price = int(input("Enter price: "))
# product = input("Enter product: ")
# percentage = int(input("Enter discount percentage: "))
# discount = price * percentage / 100
# after_discount = price - discount
# print(f"Discount: {discount}, Price after discount: {after_discount}")


#tar4

# amount = int(input("Enter amount of money: "))
# ribit_percentage = int(input("Enter the amount of ribit: "))
# ribit_for_year = amount * ribit_percentage / 100
# full_price = amount + ribit_for_year
# print(f"ribit: {ribit_for_year}, full payment: {full_price}")



#tar5
# score = float(input("Enter three scores: "))
# score2 = float(input("second: "))
# score3 = float(input("third: "))
# print(f"Average: {(score + score2 + score3) / 3}")

#tar6

# first_name = "David"
# last_name = "Cohen"
# city = "Tel Aviv"
# print(f"hello, my name is {first_name + " " + last_name} and I live in {city}")


#tar7
#
# full_name = input("Enter your full name: ")
# print(f"Full name: {full_name}, length: {len(full_name)}, caps: {full_name.upper()}, "
#       f"lower: {full_name.lower()}")


#tar8

# sentence = input("Enter a sentence: ")
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.capitalize())
# print(sentence.title())


#tar9

# name = input("Enter your full name: ")
# print(name)
# print(name.strip())
# print(len(name))
# print(len(name.strip()))



#tar10

# sentence = "I love Java programming"
# print(sentence.replace("Java", "Python"))
# print(sentence.count("love"))
# print(sentence.startswith("I"))
# print(sentence.endswith("programming"))



#tar11

# word = "Programming"
# print(f"first letter: {word[0]}")
# print(f"Last letter: {word[-1]}")
# print(f"First three letters: {word[:3]}")
# print(f"Last four letters: {word[-4:]}")
# print(f"Reversed: {word[::-1]}")



#tar12


# a = "100"
# b = "25"
# c = 10
# d = 5.5
# a = int(a)
# b = float(b)
# c = str(c)
# d = int(d)
# print(type(a), type(b), type(c), type(d))



#tar13
# age = input("Enter your age: ")
# age = int(age)
# age += 10
# print(age)


#tar14
#
# price = input("Enter price before tax: ")
# price = float(price)
# after_tax = price - price * 0.18
# print(after_tax)



#tar15

# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# age = int(input("Enter age: "))
# salary = int(input("Enter salary: "))
# years_working = int(input("Enter amount of working years: "))
#
# print(f""""
#     ======= Worker card =======
#     First name: {first_name}
#     Last name: {last_name}
#     Age: {age}
#     Salary: {salary}
#     Years Working: {years_working}
#
#     -----------------------------
#     Yearly salary: {salary * 12}
#     Adding 5% to salary: {salary + salary * 0.05}
#     Number of letters: {len(first_name) + len(last_name)}
# """)


#tar16

# shekels = float(input("Enter amount of shekels: "))
# usd_rate = 3.25
# in_dollars = shekels / usd_rate
# print(f"shekels in dollars: {shekels / usd_rate}")
# print(f"shekels to euros: {shekels / 3.75}")
# print(f"After transfer fee: {in_dollars - in_dollars * 0.02}")


#tar17

# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# brith_year = int(input("Enter birth year: "))
# email = f"{first_name}.{last_name}.{brith_year}@gmail.com"
# print(email)



#tar18
# sentence = input("Enter a full sentence: ")
# length = len(sentence)
# caps = sentence.upper()
# lower = sentence.lower()
# reversed = sentence[::-1]
# a = sentence.count("a")
# replace = sentence.replace(" ", "/")
# print(sentence)
# print(length)
# print(caps)
# print(lower)
# print(reversed)
# print(a)
# print(replace)



#tar19

# name = input("Enter name: ")
# products = input("Enter product name: ")
# price = int(input("Enter price: "))
# amount = int(input("Enter amount: "))
# discount = int(input("Enter discount percentage: "))
# tax = int(input("Enter tax percentage: "))
# final = price * amount
# discount = discount / 100 * final
# print(f"""
#     ======================
#         Receipt
#     =====================
#
# Customer: {name}
# Product: {products}
#
# Unit price: {price}
# Quantity: {amount}
#
# Subtotal: {price * amount}
# Discount: {discount}
# After discount: {final - discount}
#
# VAT: {tax / 100}
# VAT amount: {final * tax / 100}
#
# TOTAL: {final + final * tax / 100}
# """)