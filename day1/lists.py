from idlelib import rpc
from sys import set_coroutine_origin_tracking_depth

#tar1

# numbers = [10, 20 ,30, 40 ,50]
# print(numbers)
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])


#tar2

# students = ["Mordy", "Yakatz", "Fridman"]
# print(len(students))
# print(students[0], students[-1])
# students[1] = "Y"
# print(students)


#tar3

# grades = [23, 85, 100, 93, 49]
# grades.append(65)
# grades.insert(0, 50)
# grades[2] = 99
# print(grades)


#tar4

# numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers.pop(0)
# numbers.pop(-1)
# numbers.pop(3)
# print(numbers)



#tar5

# products = ["table","chair","board","laptop"]
# print("chair" in products)
# print("pen" in products)


#tar6

# numbers=[1,2,3,4,5,6,7,8,9,10]
# for i in numbers:
#     print(numbers[i])



#tar7

# numbers=[1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)



#tar8

# grades = [23, 85, 100, 93, 49]
# all = 0
# for grade in grades:
#     all += grade
# print(all)



#tar9

# numbers=[1,2,3, 20,4,5,6,7,8,9,10]
# high = 0
# for num in numbers:
#     if num > high:
#         high = num
# print(high)


#tar10

# names = ["Mordy", "Yakatz", "Fridman"]
# name = input("Enter name: ")
# found = False
# for n in names:
#     if n == name:
#         found = True
# if found:
#     print("Found")
# else:
#     print("Not found")



#tar11

# numbers=[1,2,3, 20,4,5,1,6,7,8,9,10]
# num = int(input("Enter a number: "))
# for i in range(len(numbers)):
#     if numbers[i] == num:
#         print(i)


#tar12

# numbers=[1,2,3, 20,4,5,6,7,8,9,10, 50, 70, 100]
# count = 0
# for num in numbers:
#     if num > 50:
#         count += 1
# print(count)



#tar13

# numbers=[1,2,3, 20,4,5,6,7,8,9,10, 50, 70, 100]
# new = []
# for num in numbers:
#     if num % 2 == 0:
#         new.append(num)
# print(new)


#tar14

# names = ["Mordy", "Yakatz", "Fridman"]
# indexes = 0
# while indexes < len(names):
#     name = (names[indexes], indexes)
#     print(name)
#     indexes += 1



#tar15

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[2:6])
# print(numbers[::-1])


#tar16

# names = ["Mordy", "Yakatz", "Fridman", "Mosh", "Menachem", "Zuri", "Shlomo", "soibel", "nachum", "tzvi"]
# print(names[::2])
# print(names[1::2])
# print(names[::-2])



#tar17

# numbers = [1,2,3,4,5,6,7,8,9,10,12,15,17,18,22,35,32,36,33]
# new = numbers[:10]
# print(new)
# last = numbers[11:]
# print(last)
# between = numbers[5:14]
# print(between)



#tar18

# numbers = [1,2,3,4,5,6,7,8,9,10,12,15,17,18,22,35,32,36,33]
# length = len(numbers) / 2
# first = numbers[:int(length)]
# second = numbers[int(length):]
# print(first)
# print(second)



#tar19

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# multi = [num * 2 for num in numbers]
# print(multi)
# square = [num ** 2 for num in numbers]
# print(square)
# even = [num for num in numbers if num % 2 == 0]
# print(even)
# bigger = [num for num in numbers if num > 5]
# print(bigger)


#tar20

# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# past_60 = [num for num in grades if num > 60]
# print(past_60)
# under_60 = [num for num in grades if num < 60]
# print(under_60)
# factor = [num + 5 for num in grades]
# print(factor)


#tar21

# names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
# bigger_than4 = [name for name in names if len(name) > 4]
# print(bigger_than4)
# caps = [name.upper() for name in names]
# print(caps)
# ds = [name for name in names if name[0] == "D"]
# print(ds)



#tar22

# numbers = [12, 7, 25, 30, 9, 44, 18, 3]
# new = [num for num in numbers if num % 3 == 0 and num > 10]
# print(new)


#tar23

# numbers = []
# for _ in range(10):
#     num = int(input("Enter numbers"))
#     numbers.append(num)
# print(numbers)
# high = 0
# low = 10000000000000000000000000000
# all = 0
# for num in numbers:
#     if num > high:
#         high = num
#     if num < low:
#         low = num
#     all += num
# print(high)
# print(low)
# print(all / 10)


#tar24

# names = ["Moshe", "David", "Dana", "Noa", "Michael"]
# name = input("Enter a name to search: ")
# found = False
# if name in names:
#     names.remove(name)
#     found = True
# if not found:
#     print("Couldn't find name!")
# print(names)


#tar25

# numbers = [12, 7, 25, 30, 9, 44, 18, 3, 40, 10]
# even = [num for num in numbers if num % 2 == 0]
# print(even)
# odd = [num for num in numbers if num % 2 != 0]
# print(odd)
# bigger = [num for num in numbers if num > 20]
# print(bigger)



#tar26
# numbers = [12, 7, 12, 30, 9, 44, 18, 3, 40, 10]
# count = 0
# num = int(input("Enter a number to search: "))
# for i in range(len(numbers)):
#     if numbers[i] == num:
#         print(f"indexes:{i}")
#         count += 1
# print(f"Count: {count}")
# if count == 0:
#     print("Not found")


#tar27

# first = [1,2,3,4]
# second = [30,31,32]
# for num in second:
#     first.append(num)
# print(first)
# print(first[:5])
# print(first[-5:])
# print(first[::-1])


#tar28

# first = [1,2,3,4]
# number = int(input("Enter a num to add: "))
# found = False
# for num in first:
#     if number == num:
#         found = True
#         break
#     else:
#         continue
# if found:
#     print("already exist")
# else:
#     first.append(number)
# print(first)



#tar29 project


grades = [85, 72, 90, 55, 100, 63, 48, 77]

choose = 2

while choose != 11:
    print("""
    ===== Grades Management =====

1. Show all grades
2. Add a grade
3. Search for a grade
4. Remove a grade
5. Show passing grades
6. Show failing grades
7. Show highest and lowest grade
8. Show average grade
9. Show first 3 grades
10. Show grades in reverse
11. Exit

    """)
    choose = int(input())
    if choose == 1:
        for num in grades:
            print(num)
    elif choose == 2:
        new = int(input("Add grade: "))
        grades.append(new)
    elif choose == 3:
        search = int(input("Enter a grade: "))
        for i in range(len(grades)):
            if grades[i] == search:
                print(f"index: {i}")
    elif choose == 4:
        remove = int(input("Enter a grade to remove: "))
        found = False
        for num in grades:
            if remove == num:
                found = True
                grades.remove(remove)
        if not found:
            print("Not found")
    elif choose == 5:
        passing = [grade for grade in grades if grade > 60]
        print(f"Passing grades: {passing}")
    elif choose == 6:
        fail = [grade for grade in grades if grade < 60]
        print(f"failing grades: {fail}")
    elif choose == 7:
        high = 0
        low = 101
        for num in grades:
            if num > high:
                high = num
            if num < low:
                low = num
        print(f"Highest: {high}, Lowest: {low}")
    elif choose == 8:
        summ = 0
        for num in grades:
            summ += num
        print(f"Average: {summ / len(grades)}")
    elif choose == 9:
        print(f"first 3 grade: {grades[:3]}")
    elif choose == 10:
        print(f"reverse: {grades[::-1]}")

print("Finished")
























