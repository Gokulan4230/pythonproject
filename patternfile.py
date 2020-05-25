# for i in range(4):
#     for j in range(i+1):
#         print(i, end=' ')
#     print()

# n = int(input("Enter the number :"))
# for i in range(2, n):
#     if n % i == 0:
#         print("%d is not a prime number" % n)
#         break
# else:
#     print("%d is a prime number" % n)

# n = int(input("Enter the number :"))
# for row in range(n):
#     print("*" * (n - row))
# for row1 in range(n):
#     print(" " * row1 + "*" * (n - row1))
# for row1 in range(n):
#     print("*" * (row1+1))
# for row1 in range(n):
#     print(" " * (n-row1-1) + "*" * (row1+1))

# for row in range(n):
#     print(" " * (n - row - 1) + "* " * (row+1))
# for row in range(n - 1):
#       print(" " * (row + 1) + "* " * (n - row - 1))

# for row in range(n):
#     print("*"+" "*row, end='')
#     print()
# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f = f * i
#     return f
#
#
# print(fact(int(input("Enter the number :"))))
# n = int(input("Enter the number :"))
# sum1 = 0
# for i in range(1, n+1):
#     sum1 = sum1 + i
# print(sum1)
# name = ''
# while name != "surya":
#     name = input("Enter your favourite hero name :")
#     if name != "surya":
#         print('{} is not My favourite hero '.format(name))
# else:
#     print('%s is My favourite hero ' % name)
# n = 0
# while True:
#     print('Say, i love my india : {}'.format(n))
#     n = n + 1
# n = int(input("Enter the number :"))


# for i in range(n):
#     print((chr(65+i)+' ') * n)
# for i in range(n):
#     print((chr(65 + n) + ' ') * n)
# for i in range(n):
#     print((i+1)+' ' * n)

# def palindrome(value1):
#     value2 = value1[::-1]
#     if value1 == value2:
#         print("{} is a palindrome".format(value2))
#     else:
#         print("{} is not a palindrome".format(value2))
#
#
# print(palindrome(input("Enter the value1 :")))

# def fibonnaci1(num):
#     a = 0
#     b = 1
#     print(a, b, end=' ')
#     while num - 2:
#         c = a + b
#         a = b
#         b = c
#         print(c, end=' ')
#         num = num - 1
#
#
# print(fibonnaci1(int(input("Enter the value1 :"))))
# def amstrong(num):
#     sum1 = 0
#     temp = num
#     while num != 0:
#         rem = num % 10
#         # cube = lambda rem: rem * rem * rem
#         # sum1 = sum1 + cube(rem)
#         sum1 = sum1 + rem**3
#         num = num // 10
#     if sum1 == temp:
#         print("{} is a amstrong number".format(temp))
#     else:
#         print("{} is not a amstrong number".format(temp))
#
#
# print(amstrong(int(input("Enter the number :"))))
# def login(username, password):
#     print("This is my username:{} and password:{}".format(username, password))
#
#
# login("Gokul890", 'Xys123')


# def myargs(*args):
#     for x in args:
#         if x == 'ghjk':
#             print("value is found")
#
#
# myargs("gokul", '678', 'ghjk', '1$%^%^&*')

# def getstudentmarks(**args):
#     for key, value in args.items():
#         print('{} == {}'.format(key, value))
#
#
# getstudentmarks(sname='gokul', btechmarks='70%')
# cube variable is perform like functions. so, variable arguement we have to pass the values to generate the output
# cube = lambda m: m * m * m
# print(cube(5))

# name = input("Dear sir/madam, Enter your name :")
# colour = input("& please, enter your favourite colour :")
# print(name + ' ' + 'likes' + ' ' + colour + ' ' + 'colour')

# date_of_birth_year = int(input("Dear sir/madam, please enter your birth year :"))
# age = 2020 - date_of_birth_year
# print("Hi sir/madam, you was a {} years old".format(age))

# course = "I like to learn new technology's"
# print(course.title())
# import math
#
# # number = int(input("Enter the number :"))
# # print(math.factorial(number))
# # print(math.ceil(5.9))
# # print(math.floor(5.9))
# print(math.gcd(123, 4))

# msg = input("How is climate in bangalore, today ? :")
# if msg == 'Hot':
#     msg_hot = '''today is a hot day
# Please drink plenty of water'''
#     print(msg_hot)
# elif msg == 'cool':
#     msg_cool = '''today a cold day
# please wear warm clothes'''
#     print(msg_cool)
# else:
#     print('it is lovely day')

# weight = float(input("Enter your weight :"))
# unit = input("pounds(p) or killo(k) :")
# if unit.upper() == 'P':
#     converted = weight*0.45
#     print("Your weight is {}".format(converted))
# else:
#     converted = weight / 0.45
#     print("Your weight is {}".format(converted))

# secret_number = 7
# guess_limit = 3
# guess_count = 0
# while guess_count < guess_limit:
#     num = int(input('Guess the number :'))
#     guess_count += 1
#     if num == secret_number:
#         print('you won!')
#         break
# else:
#     print('Sorry, you loss the game')

# login_limit = 3
# login_guess_count = 0
# while login_guess_count < login_limit:
#     username = input('Enter the username :')
#     password = input('Enter the password :')
#     login_guess_count += 1
#     if len(username) >= 5 and len(password) >= 5:
#         print('Logged successfully!')
#         break
#     else:
#         print('''Dear user,
#         please follow below precautions to login the application successfully.
#         ***** username and password character's should be greater than equals to 5 *****
#         ''')
# command = ''
# started = False
# while command != 'quit':
#     command = input('>>>').lower()
#     if command == 'start':
#         if started:
#             print('Car is already started!')
#         else:
#             started = True
#             print('Car started...')
#     elif command == 'stop':
#         if not started:
#             print('Car is already stopped!')
#         else:
#             started = False
#             print('Car stopped...')
#     elif command == 'help':
#         print('''
# start - to start the car
# stop  - to stop the car
# quit  - to quit
#         ''')
#     elif command == 'quit':
#         break
#     else:
#         print("sorry, i don't understand that!")
# prices = [10, 20, 30]
# total = 0
# for i in prices:
#     total = total + i
# print(total)
# n = int(input('Enter the number :'))
# for i in range(n):
#     if i == 0 or i == 2 or i == 3 or or i == 1:
#         print('e' * 1)
#     else:
#         print('e' * 2)
# number = [1, 1, 3, 1, 3]
# for i in number:
#     total = ''
#     for index in range(i):
#         total += '* '
#     print(total)
# number = [1, 5, 918, 22, 65, 98]
# max_value = 0
# for index in number:
#     if index > max_value:
#         max_value = index
# print(max_value)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# total = 0
# for row in matrix:
#     for row_data in row:
#         if row_data % 2 != 0:
#             total += row_data
# print(total)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# i = 0
# for row in matrix:
#     n = row
#     for row_data in range(len(n)):
#         if n[row_data] % 2 != 0:
#             matrix[i][row_data] = 0
#     i = i+1
# print(matrix)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# i = 0
# for row in matrix:
#     n = row
#     for row_data in range(len(n)):
#         if n[row_data] % 2 == 0:
#             matrix[i][row_data] = 0
#     i = i+1
# print(matrix)
# ********************
# numbers = [4, 5, 7, 4, 3, 3]
# no = numbers
# count = 0
# for number in numbers:
#     for index in no:
#         if number == index:
#             count = count + 1
#             if count == 2:
#                 print('Duplicate value has removed successfully in the list!')
#     numbers.remove(number)
#
# print(numbers)
# **********************************
# def my_function(x):
#     return list(dict.fromkeys(x))
#
#
# mylist = my_function([4, 5, 7, 4, 3, 3])
# print(mylist)

# numbers = [4, 5, 7, 4, 3, 3]
# unique = []
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)

# phone = input('Enter your phone number :')
# mapping_data = {
#     "1": "One",
#     "2": "Two",
#     "3": "three",
#     "4": "four",
#     "5": 'five',
#     '6': 'six',
#     '7': 'seven',
#     '8': 'eight',
#     '9': 'nine',
#     '0': 'zero'
# }
# for ch in phone:
#     print(mapping_data.get(ch, ch), end=' ')
# message = input('>>>>> Enter :')
# words = message.split(' ')
# emoji = {
#     ":)": "😊",
#     ":(": "😢",
#     '_': '❤❤',
#     '.': '👏👏👏',
#     '0': '🎁🎁',
#     '@': '🎂🎂🎂'
# }
# output = ''
# for word in words:
#     output += emoji.get(word, word) + ' '
# print(output)
# def greet(first_name, last_name):
#     print(f'Hi {first_name}{last_name}')
#     print('Welcome aboard!')
#
#
# greet(first_name="Gokul ", last_name="Muthuraj")
# def emojii(message):
#     words = message.split(' ')
#     emoji = {
#         ":)": "😊",
#         ":(": "😢",
#         '_': '❤❤',
#         '.': '👏👏👏',
#         '0': '🎁🎁',
#         '@': '🎂🎂🎂'
#     }
#     output = ''
#     for word in words:
#         output += emoji.get(word, word) + ' '
#     return output
#
#
# print(emojii(input('>>> Enter :')))
# try:
#     mess = int(input('Enter your age :'))
#     data = 10 / mess
#     print(f'My age is {mess}')
#     num = [1, 3, 4]
#     print(num[3])
# except ValueError:
#     print('Age should be integer type and should not be string type')
# except ZeroDivisionError:
#     print('Age should not be 0')
# except IndexError:
#     print('index over limit')
# # *****************************************
# class xyz:
#     def __init__(self, name, x, y):
#         self.name = name
#         self.x = x
#         self.y = y
#
#     def name1(self):
#         print(f'My name is {self.name}')
#
#     def add1(self):
#         print('sum of x and y value is {}'.format(self.x + self.y))
#
#     def __repr__(self):
#         print("the value of a is {} and b is {}".format(self.x, self.y))
#
#     def __str__(self):
#         print('addition of x and y value is {}'.format(self.x + self.y))
#
#
# data = xyz("Gokul", 10, 20)
# data.name1()
# data.add1()
# data.__repr__()
# data.__str__()
# ****************************************************
# from Find_maxvalue import maxvalue
# import Find_maxvalue
#
# number = [1, 2, 4, 67, 987]
# print(Find_maxvalue.maxvalue(number))
# package concept:
# import Calculation.arithmetic_operation
#
# print(Calculation.arithmetic_operation.add(20, 30))
# print(Calculation.arithmetic_operation.div(600, 30))
# print(Calculation.arithmetic_operation.sub(50, 30))
# print(Calculation.arithmetic_operation.square(50, 50))
import random

#
# for i in range(5):
#     for j in range(5):
#         print(f'({i}, {j})')

# class dice:
#     def roll(self):
#         n1 = random.randint(0, 100)
#         n2 = random.randint(0, 100)
#         return n1, n2
#
#
# data = dice()
# print(data.roll())
# import pathlib

# path = pathlib.Path().glob('*.py')
# path = pathlib.Path().glob('*.*')
# for file in path:
#     print(file)

# path = pathlib.Path('D:\Automation\Java concepts\Java variables.txt')
# print(path.exists())

# secret_word = 'happiness'
# guess = ''
# while guess != secret_word:
#     guess = input('guess the word which is important to live :')
# print(f'Yes, {guess} is a key to live without depression')

# secret_word = 'happiness' guess = '' guess_count = 0 guess_limit = 2 out_of_guess = False while guess !=
# secret_word and not out_of_guess: if guess_count < guess_limit: guess = input('guess the word which is important to
# live :') guess_count += 1 else: out_of_guess = True if out_of_guess: print('you could not able to find the secret
# word'+ '. ' + 'you loss the game!\nbetter lock next time!') else: print(f'Yeah, {guess} is a key to live without
# depression'+ '. ' + 'you could find the secret word. \nyou are the ' 'winner : 👏😎')

# def pow_of_number(base_num, pow_num):
#     return base_num ** pow_num
#
#
# print(pow_of_number(7, 2))
# ********************
# mess = "I Love My Family Member's"
# print(type(mess))
# vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
# translation = ''
# for index in range(len(mess)):
#     if mess[index] in vowels:
#         if mess[index] in 'aeiou':
#             translation = translation + '❤'
#         else:
#             translation = translation + '😃'
#     else:
#         translation = translation + mess[index]
# print(translation)
# def fact(num):
#     try:
#         total = 1
#         li = [1, 2, 3]
#         for n in range(1, int(num) + 1):
#             total = total * n
#         return total
#     except ValueError:
#         print('Invalid input')
#     except IndexError as err:
#         print(err)
#
#
# print(fact(input('Enter the number :')))

# story = open('blood_relationship', 'r')
# lines_of_stories = story.readlines()
# print(lines_of_stories[2])
# story.close()

# story = open('blood_relationship', 'a')
# story.write('\nMegala - she is my first lover')
# story.close()

# story = open('blood_relationships', 'r')
# story.write('''Hi all,
# I would like to say parents are backbone for children's.
#
# So, parent's should feed them children's on time and parent's must clear all children's doubts about studies.
# it is very help to children's future.
# ''')
# lines = story.readlines()
# print()
# story.close()

# filename = 'blood_relationships.txt'
# print(len(filename))
# print(filename[filename.index('.')+1:])
# **********************************************
# questions_list = ["1.What colour are bananna's?\n(a).Red \n(b).Yellow \n(c).None\n ",
#                   "2.What is our PM Name?\n(a).Modi \n(b).kedi \n(c).daddy \n",
#                   "3.What is the value of root of 25?\n(a).5 \n(b).0.5 \n(c).10 \n",
#                   "4.What is the value of addition of 2 plus 3?\n(a).0.5 \n(b).2 \n(c).5 \n"]
#
# from Calculation.arithmetic_operation import question
#
# obj_question_list = [question(questions_list[0], 'b'),
#                      question(questions_list[1], 'a'),
#                      question(questions_list[2], 'a'),
#                      question(questions_list[3], 'c')]
#
#
# def question_processor(questions):
#     score = 0
#     for quest in questions:
#         answer = input(quest.question+'\nPlease enter your answer :')
#         if answer == quest.answer:
#             score += 1
#     if score >= 2:
#         print('\n\nCongratulation 😎😎😎😎😎😎😎😎😎😎😊😊😊😊....!')
#     else:
#         print('\n\nYou got very less score ☹☹☹☹☹☹, do another try👍👍👍!')
#     print('\nyou got ' + str(score) + " out of " + str(len(obj_question_list)) + " correct !")
#
#
# question_processor(questions=obj_question_list)

# list = [23411, 13333, 516, 123, 3456, 34563, 502928]
# print(sorted(list))
# print(list)
# list.sort()
# print(list)
# print(list)

# lists = ["23411", "13333", "516"]
# Mystring = 'Keshava'
# print(Mystring)
# print(list(Mystring))
# mees = list(Mystring)
# print(mees)
# # to convert the list of string['K', 'e', 's', 'h', 'a', 'v', 'a'] into string [Keshava], we have to use Join method
# print(''.join(mees))
# print('^'.join(lists))

# age = input('Enter your age :')
# if int(age) >= 18:
#     print('you are eligible to vote!')
# else:
#     print('your are too young to vote get as soon as voter id when you are reach 18 year\'s.')

# count = 1
# total = 0
# while count <= 10:
#     total = total + (count*count)
#     count += 1
# print(total)

# prompt = 'Write a poem!\nEnter \'quit\' to exit!\n\nType your story buddy 🙂🙂🙂🙂:'
# poem_story = ''
# line = ''
# while line != 'quit':
#     line = input(prompt)
#     if line == 'quit':
#         break
#     poem_story += line+'\n'
# print(poem_story)

# Year = int(input('Enter a year : '))
# Month = int(input('Enter a month to find number of day\'s in a month : '))
# day_count = 1
# if Month in (1, 3, 5, 7, 8, 10, 12):
#     while day_count <= 31:
#         print(day_count)
#         day_count += 1
# elif Month in (4, 6, 9, 11):
#     while day_count <= 30:
#         print(day_count)
#         day_count += 1
# else:
#     if Year % 4 == 0:
#         while day_count <= 29:
#             print(day_count)
#             day_count += 1
#     else:
#         while day_count <= 28:
#             print(day_count)
#             day_count += 1
#
# print('Year = {}, Month = {}, Day count = {}'.format(Year, Month, day_count-1))
# print('You have got it successfully 🤩🤩🤩🤩🤩🤩!')
# *******************************************************
# requested_item = input('Order your food : ')
# dhosa = 20
# if requested_item == 'ghee_dosa':
#     dhosa += 20
# elif requested_item == 'masala_dosa':
#     dhosa += 15
# else:
#     dhosa += 10
#
# print(f'dhosa price is {dhosa} rupees')
# ************** check this
# print('hi, buddy can you do an help to me?', end=' ')
# print('i am trusting you that you can!!!')
# print(10, 20, 30, sep='G')
# list = [str(10), str(20), str(30)]
# print('G'.join(list))
# name = ['g', 'd']
# name[0] = 'd'
# print(name)

# employee = {
#     "Name": 'Gokul',
#     "Age": 23,
#     "Designation": "Support engineer"
# }
# print(employee.get('Name'))
# employee['Annual_salary'] = 250000
# employee['Bond_year'] = (1, 3)
# employee['Address'] = {
#     'Street': 'ITPL',
#     'Location': 'Bangalore',
#     'Pin-code': '517501'
# }
# employee['My_fav_values'] = [6, 7, 23]
# print(employee['Address'])
# for key, value in employee.items():
#     if isinstance(value, tuple) or isinstance(value, list):
#         for val in value:
#             print(f'{key} = {value}')
#         print(f'{key} = {value}')
#     elif isinstance(value, dict):
#         for key1, value1 in value.items():
#             print(f'{key1} = {value1}')
#     else:
#         print(f'{key} = {value}')
# for value in employee.values():
#     print(value)
# for key in employee.keys():
#     print(key)
# for key, value in employee.items():
#     print(f'{key} = {value}')

# class application_super:
#     def __init__(self, usn, pwd):
#         self.usn = usn
#         self.pwd = pwd
#         self.is_login_in = False
#         self.is_logout = True
#
#     def login(self):
#         if self.is_login_in:
#             print(f'{self.usn} is already logged in')
#         else:
#             self.is_login_in = True
#             print(f'{self.usn} is logged in')
#
#     def logout(self):
#         if self.is_logout:
#             self.is_logout = False
#             print(f'{self.usn} is logged out')
#         else:
#             print(f'{self.usn} is already logged out')
#
#
# login = application_super('Gokul', 'p@55w0rd')
# login.login()
# login.logout()
# login.logout()

# max_value = 0
# list_of_numbers = [10, 20, 40, 567, 8902]
# for list_of_number in list_of_numbers:
#     while list_of_number > max_value:
#         max_value = list_of_number
# print(max_value)

# class parent:
#     pass
# class child(parent):
#     pass
# print(issubclass(child, object))
# ********************************************
#
# class par:
#     def __init__(self, name):
#         self.name = name
#
#
# class chi(par):
#
#     def __init__(self, name, age):
#         par.name = name
#         self.age = age
#
#     def get_print(self):
#         print(f'{self.name}, {self.age}')
#
#
# obj = chi('Gokul', 23)
# obj.get_print()

# Set not follow the order's
# set is not allow the dulicate
# s1 = {1, 2, 2, 4, 5, 5}
# s2 = {2, 3, 4, 6, 7, 1}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.symmetric_difference(s2))
# print(s2.symmetric_difference(s1))
# print(s1.difference(s2))
# print(s2.difference(s1))
# s1.add(8)
# print(s1)
# s2.update([3, 5, 7, 8, 9, 22])
# print(s2)
# s2.clear()
# print(s2)
# print(r'c:\admin\naveen')
# print(f'c:admin\neengokul')
# a = 5
# b = 7
# print(complex(7))
# c = complex(0, 7)
# print(c)
# c = complex(5, 7)
# print(c)
# print(int(True))
# print(int(False))
# print(list(range(1, 100, 4)))

# nums = [1, 44, 55, 22, 33, 44, 33]
# print(list(dict.fromkeys(nums)))
# a, b, c = 1, 2, 3
# print(c)
# print(bin(23))
# print(13 & 14)
# print(12 | 13)
# print(12 ^ 13)
# print(13 ^ 14)
# print(2**6)

# import sys
#
# x = int(sys.argv[1])
# y = int(sys.argv[2])
# print(x + y)

# i = 1
# while i <= 5:
#     print('Telusuko ', end='rocks ' * 4)
#     i = i + 1
#     print()

# i = 1
# n = 100
# count = 0
# while i <= n:
#     if i % 3 != 0 and i % 5 != 0:
#         print(i)
#         count = count + 1
#     i += 1
# print('the total no of values are {}'.format(count))
# for i in range(100, 0, -7):
#     print(i)

# av_candy = 10
# n = int(input("How many candies you want ?\nPlease enter, here :-"))
# for i in range(1, n + 1):
#     if n > av_candy:
#         print('candies out of stock')
#         break
#     else:
#         print('candy')

# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i)

# for i in range(1, 101):
#     if i % 2 == 0:
#         pass
#     else:
#         print(i)
# n = int(input('Enter the number : '))
# for i in range(n):
#     for j in range(n):
#         print('#', end=' ')
#     n = n-1
#     print()
# n = 5
# for i in range(0, n):
#     n = n - 1
#     print(' ' * n + '#' * (i + 1))

# class a:
#     def __init__(self):
#         self.name = 'Gokul'
#         self.age = 23
#
#     def compare(self, other):
#         if self.age == other.age:
#             return True
#         else:
#             return False
#
#
# obj1 = a()
# obj1.age = 23
# obj2 = a()
# if obj1.compare(obj2):
#     print('both are same')
# else:
#     print('both are not same')
# import math
#
#
# class b:
#     @staticmethod
#     def fact(num):
#         return math.factorial(num)
#
#     @classmethod
#     def pow(cls):
#         return 'Hello'
#
#
# print(b.fact(int(input('Enter the number :- '))))
# print(b.pow())

# class employee:
#     def __init__(self, name, dept, age):
#         self.name = name
#         self.dept = dept
#         self.age = age
#         self.lap = self.Laptop()
#
#     def emp_info(self):
#         print(f'{self.name} is {self.dept} team and he is {self.age} year\'s old.')
#         self.lap.laptop_info()
#
#     class Laptop:
#         def __init__(self):
#             self.branch = 'Dell'
#             self.processor = 'i3'
#             self.Memory = '4.00GB'
#
#         def laptop_info(self):
#             print(f'Laptop company name = {self.branch}, Laptop processor = {self.processor}, Laptop Memory = {self.Memory}')
#
#
# obj1 = employee('Gokul', 'Support', '23')
# print(obj1.emp_info())
# # obj2 = employee.Laptop('i3', 'Dell', '4.00GB')
# # print(obj2.laptop_info())

# class a:
#     def __init__(self):
#         print('A init...')
#
#     def feature1(self):
#         print('feature1... ')
#
#     def feature2(self):
#         print('feature2... ')
#
#
# class b:
#     def __init__(self):
#         print('B init...')
#
#     def feature3(self):
#         print('feature3... ')
#
#     def feature4(self):
#         print('feature4... ')
#
#
# class c(a, b):
#     def __init__(self):
#         super().__init__()
# here, c is a subclass and it will inheritate the properties from a and b super class
# when we create an object for c class. then, it will try to call init of subclass(c)
# if it is not found, then it will call init of superclass
# in case of multiple inheritance, if create object for the c class, then, it will try
# to call init of subclass(c). if it is not found, then it will call init of superclass(a)
# here, subclass(c) has two superclass(a and b). then, init of superclass(a) will invoke
# if we create object for subclass(c) and it is not found init of itself.
#         print('C init...')
#
#     def feature5(self):
#         print('feature5... ')
#
#
# o1 = c()
# o1.feature5()

# class pycharm:
#     def execute(self):
#         print('''---> it will check the spelling.
# ---> compiling and running.''')
#
#
# class eclipse:
#     def execute(self):
#         print('''---> compiling and running''')
#
#
# class laptop:
#     def code_checker(self, ide):
#         ide.execute()
#
#
# ide = pycharm()
# lap = laptop()
# lap.code_checker(ide)

# class operator:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):
#         s1 = self.m1 + other.m1
#         s2 = self.m2 + other.m2
#         return s1 + s2
#
#     def __sub__(self, other):
#         s1 = self.m1 - other.m1
#         s2 = self.m2 - other.m2
#         return s1 - s2
#
#     def __gt__(self, other):
#         s1 = self.m1 + other.m1
#         s2 = self.m2 + other.m2
#         if s1 > s2:
#             return True
#         else:
#             return False
#
#
# student1 = operator(13, 5)
# student2 = operator(12, 9)
# print(student1 + student2)
# print(student1 - student2)
# if student1 > student2:
#     print('s1 wins')
# else:
#     print('s2 wins')

# from time import sleep
# from threading import Thread
#
#
# class hello(Thread):
#     def run(self):
#         for i in range(5):
#             print('Hello...😍😍')
#             sleep(1)
#
#
# class hi(Thread):
#     def run(self):
#         for i in range(5):
#             print('Hi...😍😍')
#             sleep(1)
#
#
# hello = hello()
# hi = hi()
# hello.start()
# sleep(0.2)
# hi.start()
#
# hello.join()
# hi.join()
#
# print('Bye...')

# f = open('HYD04032020.doc.csv', 'r')
# f1 = open('HYD23032020', 'w')
# for i in f:
#     f1.write(i)

# Linear search to find the desired number
# pos = 0
#
#
# def search(list, n):
#     for i in range(len(list)):
#         if list[i] == n:
#             globals()['pos'] = i
#             return True
#
#
# number_format = {
#     '1': 'st',
#     '2': 'nd',
#     '3': 'rd'
# }
#
# list = [2, 44, 25, 56, 78, 7, 45, 21, 34, 67, 98, 94]
# n = int(input('Enter the number : '))
# if search(list, n):
#     ass = number_format.get(str(pos+1))
#     if ass is not None:
#         print(f'found at {pos+1}{ass} position.')
#     else:
#         print(f'found at {pos + 1}th position.')
# else:
#     print(f'Not found at any position of list.')


# list = [2, 44, 25, 56, 78, 7, 45, 21, 34, 67, 98, 94]
# list.sort()
# print(list)
# print(sorted(list))

# list = [4, 2, 7, 9, 11, 1]
# for i in range(len(list)-1, 0, -1):
#     for j in range(i):
#         if list[j] > list[j + 1]:
#             temp = list[j]
#             list[j] = list[j + 1]
#             list[j + 1] = temp
#     print(list)

# position = -1
#
#
# def search(lib, n):
#     l = 0
#     u = len(lib) - 1
#     while l <= u:
#         index = (l + u) // 2
#         if lib[index] == n:
#             globals()['position'] = index
#             return True
#         else:
#             if lib[index] < n:
#                 l = index + 1
#             else:
#                 u = index - 1
#     return False
#
#
# lib = [4, 14, 7, 5, 76, 90, 88, 78, 66]
# n = 7
# if search(lib, n):
#     print(f'found at {position + 1} position.')
# else:
#     print('not found')

number = [6, 5, 9, 2, 7, 8]
for i in range(len(number) - 1):
    minpos = i
    for j in range(i, len(number)):
        if number[j] < number[minpos]:
            minpos = j

    temp = number[i]
    number[i] = number[minpos]
    number[minpos] = temp

    print(number)
