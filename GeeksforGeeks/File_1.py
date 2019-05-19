########################################################################################

# from __future__ import division
#
# print 7/3   # 2 if no import  #2.333 import import from future

########################################################################################

# import keyword
# s = ["for","geeksforgeeks","elif","elseif","nikhil","assert","shambhavi","True","False","akshat","akash","break","ashty","lambda","suman","try"]
# for x in s:
#     if keyword.iskeyword(x):
#             print ( x + " is a python keyword")
#     else:
#         print ( x + " is not a python keyword")
#
# print (keyword.kwlist)

########################################################################################

# print False == 0 #True
# print True == 1
# print True + True + True
# print True + False + False
# assert 5 < 3, "5 is not smaller than 3"

########################################################################################

# for letter1 in 'geeksforgeeks':
#     if letter1 == 'e' or letter1 == 's':
#         continue
#     print 'Current Letter1 :', letter1
#     var = 10

########################################################################################

# for letter2 in 'geeksforgeeks':
#     # break the loop as soon it sees 'e'
#     # or 's'
#     if letter2 == 'e' or letter2 == 's':
#         break
# print 'Current Letter2 :', letter2

########################################################################################

# for letter3 in 'geeksforgeeks':
#     pass
# print 'Last Letter :', letter3

########################################################################################

# for i in 'geeksforgeeks':
#     print i,
#
# print ("\r")
# print "anildileep\rdileep"
# #dileepleep
# print "anildileep\fdileep"
# #anildileep
# #          dileep
# print (' ' is '')
# print (' ' is ' ')
# print ('ab' is ' ')
# print ({} is {})

########################################################################################
# a = 10
# def read():
#     print (a)
# def mod1():
#     global a
#     a = 5
# def mod2():
#     a = 15
# read()
# mod1()
# read()
# mod2()
# read()

########################################################################################

# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
# # Driver code to check above generator function
# for value in simpleGeneratorFun():
#     print(value)
#
# def nextSquare():
#     i = 1
#     while True:
#         yield i * i
#         i += 1  # Next execution resumes
#                 # from this point
# for num in nextSquare():
#     if num > 100:
#         break
#     print(num)

########################################################################################

# # Create a new dictionary
# d = dict()  # or d = {}
# d['xyz'] = 123
# d['abc'] = 345
# print d
# print d.keys()
# print d.values()
# for i in d:
#     print "%s  %s" % (i, d[i])
# for index, value in enumerate(d):
#     print index, value, d[value]
# print 'xyz' in d
# del d['xyz']
# print "xyz" in d
# print d

########################################################################################

# def cube(x):
#     return x**2
# print "MAP EXAMPLES"
# cubes = map(cube, range(10))
# print cubes
# print "LAMBDA EXAMPLES"
# print (lambda x: x**2,5)
# print (lambda x: x**2)(5)
# print (lambda x, y: x * y)(3, 4)
# print "FILTER EXAMPLE"
# special_cubes = filter(lambda x: x > 9 and x < 60, cubes)
# print special_cubes

# x = [2, 3, 4, 5, 6]
# y = []
# for v in x:
#     print v%2
#     if v % 2:
#         y += [v * 5]
# print y

# x = [2, 3, 4, 5, 6]
# y = map(lambda v: v * 5, filter(lambda u: u % 2, x))
# print y
########################################################################################

# try,except and else

# def AbyB(a , b):
#     try:
#         c = ((a+b) / (a-b))
#     except ZeroDivisionError:
#         print "a/b result in 0"
#     else:
#         print c
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)

########################################################################################

# try:
#     print "try"
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print "Except"
#     print "An exception"
#     raise

########################################################################################

# # A Python program to to return multiple
# # values from a method using class
# class Test:
#     def __init__(self):
#         self.str = "geeksforgeeks"
#         self.x = 20
#     # This function returns an object of Test
# def fun():
#     return Test()
# # Driver code to test above method
# t = fun()
# print(t.str)
# print(t.x)
#
#
# # A Python program to to return multiple
# # values from a method using tuple
# # This function returns a tuple
# def fun():
#     str = "geeksforgeeks"
#     x = 20
#     return str, x;  # Return tuple, we could also
#     # write (str, x)
# # Driver code to test above method
# str, x = fun()  # Assign returned tuple
# print(str)
# print(x)
#
#
# # A Python program to to return multiple
# # values from a method using list
# # This function returns a list
# def fun():
#     str = "geeksforgeeks"
#     x = 20
#     return [str, x];
# # Driver code to test above method
# list = fun()
# print(list)
#
#
# # A Python program to to return multiple
# # values from a method using dictionary
# # This function returns a dictionary
# def fun():
#     d = dict();
#     d['str'] = "GeeksforGeeks"
#     d['x'] = 20
#     return d
# # Driver code to test above method
# d = fun()
# print(d)

########################################################################################

# Print The File Path Of Imported Modules.
# import os
# import socket
#
# print(os)
# print(socket)

########################################################################################

# Checking if two words are anagrams

# from collections import Counter
# def is_anagram(str1, str2):
#     return Counter(str1) == Counter(str2)
#
# print(is_anagram('geek', 'eegk'))
# print(is_anagram('geek', 'peek'))

########################################################################################

# a = [[1, 2], [3, 4], [5, 6]]
# # Convert it to a single list without using any loops.
# # Output:- [1, 2, 3, 4, 5, 6]
#
# import itertools
# list(itertools.chain.from_iterable(a))
# # [1, 2, 3, 4, 5, 6]

########################################################################################

# # Python code to demonstrate the use of 'sys' module
# # for command line arguments
# import sys
# # command line arguments are stored in the form
# # of list in sys.argv
# argumentList = sys.argv
# print argumentList
# # Print the name of file
# print sys.argv[0]
# # Print the first argument after the name of file
# print sys.argv[1]

########################################################################################

# import sys
# from math import factorial
#
# print factorial(int(sys.argv[1]))
# print factorial(5)

########################################################################################

# Variable Arguments args(*) and kwargs(**) Both ‘args’ and ‘kwargs’ are used to get arbitrary number of arguments in a function.
# args will give us all the function parameters in the form of a list and kwargs will give  us all the keyword arguments except for those corresponding to formal parameter as dictionary.
#
# # Python program to illustrate the use of args which
# # multiplies all the values given to the function as parameter
#
#
# def multiplyAll(*values):
#     mul = 1
#
#     # values(args) will be in the form of tuple
#     print values
#     print "Type = ", type(values)
#
#     # Multiplying the all the parameters and return the result
#     for i in values:
#         mul = mul * i
#
#     return mul
#
#
# # Driver program to test above function
#
# # Multiply two numbers using above function
# ans = multiplyAll(1, 2)
# print "The multiplication of 1 and 2 is ", ans
#
# # Multiply 5 numbers using above function
# ans = multiplyAll(3, 4, 5, 6, 7)
# print "The multiplication of 3 to 7 is ", ans

# Note that args are denoted by using a single star and kwargs are denoted by two stars before the formal parameters in the function.
# Program to illustrate the use of kwargs in Python

# # Function that print the details of a student
# # The number of details per student may vary
# def printDetails(**details):
#     # Variable 'details' contains the details in the
#     # form of dictionary
#     print "Parameter details contains"
#     print details
#     print "Type = ", type(details)
#
#     # Print first name
#     print "First Name = ", details['firstName']
#
#     # Print the department of student
#     print "Department = ", details['department']
#     print ""  # Extra line break
#
#
# # Driver program to test above function
#
# # Calling the function with three arguments
# printDetails(firstName="Nikhil",
#              rollNumber="007",
#              department="CSE")
#
# # Calling the function with two arguments
# printDetails(firstName="Abhay",
#              department="ECE")

# Please note that if you are using both args and kwargs in a function then the args parameter must precede before the kwarg parameters.
# Example:
# # Function containing both args and kwargs
# def cheeseshop(kind, *arguments, **keywords):
#     print "-- Do you have any", kind, "?"
#     print "-- I'm sorry, we're all out of", kind
#     for arg in arguments:
#         print arg
#     print "-" * 40
#     keys = sorted(keywords.keys())
#     for kw in keys:
#         print kw, ":", keywords[kw]
#
#
# # Driver program to test above function
# cheeseshop("Burger", "It's very funny, sir.",
#            "It's really very, VERY funny, sir.",
#            shopkeeper='Michael Palin',
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")