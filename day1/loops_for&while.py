import random

#tar1

#
# count = 1
# while count <= 10:
#     print(count)
#     count += 1



#tar2

# count = 1
# while count <= 10:
#     print(count)
#     count += 1
#     if count == 11:
#         print("START")



#tar3

# count = 1
# while count <= 50:
#     if count % 2 == 0:
#         print(count)
#     count += 1



#tar4


# num = int(input("Enter a number: "))
# print(num)
# number = num
# for _ in range(4):
#     print(num + number)
#     num = number + num



#tar5

# summ = 0
# for i in range(100):
#     summ += i + 1
# print(summ)



#tar6

# correct = "Python123"
# password = input("Enter password: ")
# while password != correct:
#     password = input("Wrong password, enter again")
# print("Finished successfully")



#tar7

# secret_number = 27
# guess = int(input("Enter your guess number: "))
# while secret_number != guess:
#     guess = int(input("Wrong guess, try again: "))
# print("you guessed successfully!")



#tar8

# num = int(input("Enter a number: "))
# summ = 0
# while num != 0:
#     summ += num
#     num = int(input("Enter a number (until you reach 0): "))
# print(summ)



#tar9

# total = 0
# amount = 0
# average = 0
# grades = int(input("enter grades: "))
# while grades != 999:
#     total += grades
#     amount += 1
#     grades = int(input("Enter grades: "))
# amount += 1
# total += 999
# print(f"Amount of grades: {amount}, sum grades: {total}, average grade: {total / amount}")



#tar10

# num = int(input("Enter a number: "))
# total = 0
# amount = 0
# while num > 0:
#     total += num
#     amount += 1
#     num = int(input("Enter a number: "))
# print(f"Sum: {total}, Amount: {amount}")



#tar11

# num = int(input("Enter a number: "))
# for i in range(10):
#     print(f"{num} x {i + 1} = {num * (i + 1)}")



#tar12

# num = int(input("Enter a number: "))
# summ = 0
# while num:
#     summ += 1
#     num //= 10
# print(summ)



#tar13


# num = int(input("Enter a number: "))
# new_num = ""
# while num:
#     new = num % 10
#     new_num += str(new)
#     num //= 10
# print(new_num)



#tar14

# num = int(input("Enter a number: "))
# count = 2
# flag = True
# while count < num and flag:
#     if num % count == 0:
#         flag = False
#     count += 1
# if flag:
#     print("Rishoni")
# else:
#     print("Not rishoni")



#tar15

# balance = 5000
# print("""
#     MENU
# 1. check balance
# 2. put in money
# 3. withdraw money
# 4. Exit
# """)
# choose = int(input())
# while choose != 4:
#     if choose == 1:
#         print(f"Balance: {balance}")
#     elif choose == 2:
#         put = int(input("Enter amount to put in: "))
#         balance += put
#         print("Added successfully")
#     elif choose == 3:
#         withdraw = int(input("Enter amount to withdraw: "))
#         if withdraw > balance:
#             print("Not enough money: ")
#         else:
#             balance -= withdraw
#             print(f"Action finished. balance: {balance}")
#     print("""
#         MENU
#     1. check balance
#     2. put in money
#     3. withdraw money
#     4. Exit
#     """)
#     choose = int(input())



#tar16

# count = 1
# while True:
#     if count == 15:
#         print(count)
#         break
#     print(count)
#     count += 1



#tar17

# count = 1
# while count <= 30:
#     if count % 3 == 0:
#         count += 1
#         continue
#     print(count)
#     count += 1



#tar18

# num = int(input("Enter numbers: "))
# while True:
#     if num == 100:
#         print("Success")
#         break
#     num = int(input("Enter numbers: "))



#tar19

# count = 1
# for _ in range(20):
#     print(count)
#     count += 1


#tar20

# for i in range(51):
#     if i % 5 == 0:
#         print(i)



#tar21

# summ = 0
# for i in range(100):
#     summ += (i + 1)
# print(summ)


#tar22

# num = int(input("Enter a number: "))
# for i in range(10):
#     print(f"{num} x {i + 1} = {num * (i + 1)}")



#tar23

# num1 = int(input("Enter start number: "))
# num2 = int(input("Enter end number: "))
# summ = 0
# for i in range(num1, num2 + 1):
#     summ += i
# print(summ)



#tar24
# for i in range(1,100):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)


#tar25

# lines = int(input("Enter line length: "))
# cols = int(input("Enter cols length: "))
# for i in range(lines):
#     for j in range(cols):
#         print("*", end=" ")
#     print()


#tar26
# count = 1
# for i in range(6):
#     for j in range(count):
#         print("*", end="")
#     print()
#     count += 1


#tar27

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i * j}")
#     print()


#tar28

# for i in range(6):
#     for j in range(6):
#         print(f"{i}, {j}")
#     print()



#tar29


# choose = 1
# while choose != 3:
#     print("""
#     ===== MATH GAME =====
#
#     1. Start Game
#     2. View Instructions
#     3. Exit
#
#     Choose:
#
#     """)
#     choose = int(input())
#     points = 0
#     if choose == 1:
#         for j in range(1, 6):
#             for z in range(1, 3):
#                 print(f"{j} + {z} = ?")
#                 answer = int(input())
#                 if j + z == answer:
#                     print("Right answer!")
#                     points += 1
#                 else:
#                     print("Wrong answer!")
#     elif choose == 2:
#         print("10 math questions")
#
#     print(points)
#
#     print("""
#         ===== MATH GAME =====
#
#         1. Start Game
#         2. View Instructions
#         3. Exit
#
#         Choose:
#
#         """)
#     choose = int(input())





















