from bdb import foo
from os import name

from pip._internal.vcs import git

#tar1

# numbers = (10, 20, 30, 40, 50)
# print(numbers)
# print(numbers[0], numbers[-1])
# print(len(numbers))
# print(numbers[2])


#tar2

# names = ("Mordy", "yakatz", "fridman", "menachem", "josh")
# for n in names:
#     print(n)
# print("ss" in names)
# print(len(names))


#tar3

# numbers = (10, 20, 30, 40, 50)
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[::-1])



#tar4

# product = ("table", 500, 3, "furniture")
# for i in range(len(product)):
#     print(product[i])


#tar6

# numbers = (10, 11, 20, 30, 40, 50)
# summ = 0
# high = 0
# count = 0
# for num in numbers:
#     summ += num
#     if num > high:
#         high = num
#     if num % 2 == 0:
#         count += 1
# print(summ)
# print(high)
# print(count)



#tar7

# products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
# new = products[:3]
# print(new)
# last = products[-3:]
# print(last)
# long = new + last
# print(long)



#tar8

# car = {"brand": "Mazda", "model": "3", "year": 2015, "price": 30000}
# car["price"] = 31000
# car["year"] = 2016
# car["color"] = "white"
# print(car)


#tar9

# salaries = {    "David": 12000,    "Moshe": 15000,    "Dana": 13500}
# print(salaries.values())
# salaries["David"] = 11000
# salaries["Mordy"] = 30000
# print(salaries)


#tar10

# products = {"table": 500, "chair": 200, "stender": 150}
# item = input("Enter product to search: ")
# found = False
# for n in products.keys():
#     if n == item:
#         print(products[n])
#         found = True
# if not found:
#     print("Not found")



#tar11

# students = {"mordy": 100, "fridman": 95, "moshe": 50, "nachum": 80, "shlomo": 65}
# for grade in students.keys():
#     print(f"Student: {grade} | Grade: {students[grade]}")


#tar12

# grades = {    "David": 90,    "Moshe": 75,    "Dana": 100,    "Noa": 55,    "Avi": 82}
# all = 0
# failed = 0
# for grade in grades.keys():
#     if grades[grade] >= 80:
#         print(grade)
#     else:
#         failed += 1
#     all += grades[grade]
#
# print(all / 5)
# print(failed)



#tar13

# products = {"table": 500, "chair": 200, "stender": 150}
# item = input("Enter a product name: ")
# found = False
# for pro in products.keys():
#     if pro == item:
#         found = True
#
# if found:
#     price = int(input("Item has been found, Enter new price: "))
#     products[item] = price
#
# else:
#     price = int(input("Adding new product, Enter price: "))
#     products[item] = price



#tar14

# students = [    {"name": "David", "age": 20, "grade": 90},
#                 {"name": "Moshe", "age": 22, "grade": 75},
#                 {"name": "Dana", "age": 21, "grade": 100},
#                 {"name": "Noa", "age": 19, "grade": 55},
#                 {"name": "Avi", "age": 23, "grade": 82}]
#
# for name in students:
#     print(name["name"])
# for grade in students:
#     print(grade["grade"])
# ave = 0
# high = 0
# for grade in students:
#     if grade["grade"] >= 80:
#         print(grade["name"])
#     ave += grade["grade"]
#     if grade["grade"] > high:
#         high = grade["grade"]
# print(ave / 5)
# print(high)




#tar15

# students.append({"name": "Yoni", "age": 22, "grade": 99})
# students[1]["grade"] = 89
# Dana = {"name": "Dana", "age": 21, "grade": 100}
# students.remove(Dana)
# print(students)



#tar16

# classroom = {    "Class A": ["David", "Moshe", "Dana"],
#                  "Class B": ["Noa", "Avi", "Michael"],
#                  "Class C": ["Daniel", "Shir", "Yossi"]}
#
# for name in classroom.keys():
#     print(name)
# for name in classroom.keys():
#     if name == "Class A":
#         print(classroom[name])
# classroom["Class B"].append("Mordy")
# classroom["Class C"].pop(-1)
# print(classroom)
# len_a = len(classroom["Class A"])
# len_b = len(classroom["Class B"])
# len_c = len(classroom["Class C"])
# print(len_a, len_b, len_c)



#tar17

# products = {    "Laptop": {        "price": 4500,        "stock": 10    },
#                 "Mouse": {        "price": 80,        "stock": 50    },
#                 "Keyboard": {        "price": 150,        "stock": 20    }}
#
#
# for item in products.values():
#     print(item["price"], end="  ")
#     print(item["stock"])
#
# products["Laptop"]["stock"] = 11
# products["USB"] = {"price": 20, "stock": 5}
# for item in products.keys():
#     if products[item]["price"] > 100:
#         print(item)



#tar18

# employees = [    ("David", "Development", 15000),
#                  ("Moshe", "Marketing", 12000),
#                  ("Dana", "Development", 18000),
#                  ("Noa", "HR", 11000)]
#
# for name in employees:
#     print(name[0])
#
# print()
# high = 0
# high_name = None
# avg = 0
# for department in employees:
#     if department[1] == "Development":
#         print(f"Word in developmenet: {department[0]}")
#
#     if department[2] > high:
#         high = department[2]
#         high_name = department[0]
#     avg += department[2]
# print()
# print(f"highest salary: {high_name}")
# print(f"Average: {avg / 4}")




#tar19

# inventory = {    "Laptop": 10,    "Mouse": 50,    "Keyboard": 20}
#
# name = input("Enter product to search: ")
# quantity = int(input("Enter quantity: "))
# found = False
# for item in inventory.keys():
#     if name == item:
#         found = True
#
# if found:
#     if quantity > inventory[name]:
#         print("Not enough in stock!")
#     else:
#         inventory[name] -= quantity
#         print("Added to cart")
# else:
#     print("Not found!")
# print(inventory)



#tar20

# votes = {    "David": 0,    "Moshe": 0,    "Dana": 0}
# runner = input("Enter runner name to vote: ")
# while runner != "stop":
#     if runner in votes.keys():
#         print("Found and added")
#         votes[runner] += 1
#     runner = input("Enter runner name to vote: ")
# print(votes)
# high = 0
# high_name = None
# for r in votes.keys():
#     if votes[r] > high:
#         high = votes[r]
#         high_name = r
# print(f"Winner is: {high_name}")


#tar21

# contacts = {"Moshe": "05278543", "Yaniv": "45372934", "Mordy": "345823495"}
# choose = 5
# while choose != 6:
#     print("""
#     ----- Menu -----
#     1. Add contact
#     2. Search contact
#     3. update contact
#     4. Delete contact
#     5. Show all contacts
#     6. Exit
#     """)
#     choose = int(input())
#     if choose == 1:
#         name = input("Enter name: ")
#         number = input("Enter phone number: ")
#         contacts[name] = number
#     elif choose == 2:
#         name = input("Enter name to search: ")
#         if name in contacts.keys():
#             print(f"Found! phone number is: {contacts[name]}")
#         else:
#             print("Not found")
#     elif choose == 3:
#         name = input("Enter name to search: ")
#         if name in contacts.keys():
#             number = input("Enter phone number to update: ")
#             contacts[name] = number
#             print("Updated successfully")
#         else:
#             print("Not found!")
#     elif choose == 4:
#         name = input("Enter name to delete: ")
#         if name in contacts.keys():
#             contacts.pop(name)
#         else:
#             print("Not found")
#     elif choose == 5:
#         print(contacts)
#
#
# print("Finished progress")



#tar22 project


products = [    {"name": "Laptop", "price": 4500, "stock": 10},
                {"name": "Mouse", "price": 80, "stock": 50},
                {"name": "Keyboard", "price": 150, "stock": 20},
                {"name": "Screen", "price": 900, "stock": 15}]

choose = 5
while choose != 0:
    print("""
    ===== Store Management =====

1. Show all products
2. Add product
3. Search product
4. Update product price
5. Update product stock
6. Sell product
7. Show products by price
8. Show products with low stock
9. Show total inventory value
0. Exit

    """)
    choose = int(input())
    if choose == 1:
        print(products)
    elif choose == 2:
        name = input("Enter name: ")
        price = int(input("Enter price: "))
        stock = int(input("Enter stock: "))
        products.append({"name": name, "price": price, "stock": stock})
        print("Added successfully")
    elif choose == 3:
        name = input("Enter product to search: ")
        found= False
        for item in products:
            if item["name"] == name:
                found = True
                print(item)
        if not found:
            print("Not found!")
    elif choose == 4:
        name = input("Enter product to update price: ")
        found = False
        for item in products:
            if item["name"] == name:
                found = True
                price = int(input("Product found, enter new price: "))
                item["price"] = price
        if not found:
            print("Not found!")
    elif choose == 5:
        name = input("Enter product to update stock: ")
        found = False
        for item in products:
            if item["name"] == name:
                found = True
                stock = int(input("Product found, enter new price: "))
                item["stock"] = stock
        if not found:
            print("Not found!")
    elif choose == 6:
        name = input("Enter product's name to sell: ")
        quantity = int(input("Enter quantity to sell: "))
        found = False
        for item in products:
            if item["name"] == name:
                found = True
                if item["stock"] < quantity:
                    print("Not enough in stock!")
                else:
                    item["stock"] -= quantity
                    print("Stock updated")
        if not found:
            print("Not found!")
    elif choose == 7:
        price = int(input("Enter price limit to show products: "))
        for item in products:
            if item["price"] < price:
                print(item)
    elif choose == 8:
        low = [item for item in products if item["stock"] < 10]
        print(low)

    elif choose == 9:
        all = 0
        for item in products:
            all += item["price"] * item["stock"]
        print(f"total vlue: {all}")






