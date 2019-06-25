# Notes Count
# def countCurrency(amount): 
#     notes = [2000, 500, 200, 100, 50, 20, 10, 5] 
#     notes_dict={2000:0, 500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 1:0}
#     for i in notes:
#         if amount >=i:
#             j=amount // i
#             amount = amount - (j * i)
#             print i,amount
#             notes_dict[i]=j

#     print "%s can't be divided further"%amount
#     print notes_dict

# amount = 868
# countCurrency(amount)


# Factorial
# def fac(n):
#     result=1
#     for i in range(n,0,-1):
#         result=result*i
#     print result
# # fac(1)
# fac(5)


# Fibonacci:
# def fib(n):
#     a,b=0,1
#     for i in range(n):
#         a,b=b,b+a
#         print a
# fib(10)

# Fibonacci using generators:
# def fib(n):
#     a,b=0,1
#     for i in range(n):
#         a,b=b,b+a
#         yield "{}:{}".format(i+1,a)
# for item in fib(10):
#     print item


# Palindrome:
# def pal(s):
#     st=str(s)
#     rev_st=st[::-1]
#     if st==rev_st:
#         print "Palindrome"
#     else:
#         print "Not palindrome"
# pal(1)
# pal(123)
# pal(12321)
# pal("anil")
# pal("malayalam")

# Star Pattern 1:
# n=4
# for i in range(n,0,-1):
#     print "*"*i

# Star Pattern 2:
# n=4
# for i in range(n,0,-1):
#     print str(i)*i

# Index of element:
# a=["This","is","sequence","of",5]
# def find_index(s):
#     print a.index(s)
# find_index(5)
# find_index("is")

# Reverse String:
# s="My name is Anil"
# l=s.split()
# print ' '.join(l[::-1])

# Pyg Latin:
# s="My name is Anil"
# l=s.split()
# for i in l:
#     print ''.join(i[1:])+i[0]+'ay',

# First 10 prime numbers:
# n=100
# l=[]
# for num in range(n):
#     if num > 1 and len(l)<10:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             l.append(num)
#             print(num),        


# Prime number > 5000:
# lower=5000
# upper=6000
# l=[]
# for num in range(lower,upper):
#     if num > lower and len(l)<10:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             l.append(num)
#             print(num),


# Pattern :
# l=[1,2,3,4,5]
# # print l
# for i in range(len(l),0,-1):
#     # print i,"*************"
#     # for j in range(i,len(l)):
#     #     pass
#     print ''.join(str(x) for x in l[0:i])+''.join(str(x-i) for x in l[i:len(l)])

# Palindrome Substring
# def palindromes(text):
#     text = text.lower()
#     results = []

#     for i in range(len(text)):
#         # print "i :",i,"#######"
#         for j in range(0, i):
#             chunk = text[j:i + 1]
#             # print chunk+" : "+chunk[::-1]
#             if chunk == chunk[::-1]:
#                 results.append(chunk)
#             # print results

#     return text.index(max(results, key=len)), results
# print palindromes("forgeekskeegfor")


# def pypart2(n): 
#     k = 2*n - 2
#     for i in range(0, n): 
#         for j in range(0, k): 
#             print " " ,
#         k = k - 2
#         for j in range(0, i+1): 
#             print("* ","") 
#         print("\r") 
  
# n = 5
# pypart2(n) 



# def ispangram(str): 
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet: 
#         if char not in str.lower(): 
#             return False
#     return True
      
# # Driver code 
# string = 'the quick brown fox jumps over the lazy dog'
# if(ispangram(string) == True): 
#     print("Yes") 
# else: 
#     print("No") 


# import string 
  
# alphabet = set(string.ascii_lowercase) 
  
# def ispangram(string): 
#     return set(string.lower()) >= alphabet 
      
# # Driver code 
# string = "The quick brown fox ;? /jmps over the lazy dog"
# if(ispangram(string) == True): 
#     print("Yes") 
# else: 
#     print("No") 


# import string 
  
# alphabet = set(string.ascii_lowercase) 
  
# def ispangram(str): 
#     print set(alphabet),set(str),set(alphabet) - set(str)  
#     return not set(alphabet) - set(str) 
      
# # Driver code 
# string = 'the quick brown fox jumps over ;the lazy dog'
# if(ispangram(string) == True): 
#     print("Yes") 
# else: 
#     print("No") 


# import itertools 
# import string 
  
# alphabet = set(string.ascii_lowercase) 
  
# def ispangram(str): 
#      return sum(1 for i in set(str) if 96 < ord(i) <= 122) == 26
      
# # Driver code 
# string = 'the quick brown fox jumps over the lazy dog'
# if(ispangram(string) == True): 
#     print("Yes") 
# else: 
#     print("No") 


# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)
# print(type(y))


# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"]),type(y)

# x = {"name": "John","age": 30,"city": "New York","status":None}
# print x,type(x)



# a=[1,2,3,4,5,6,7,8,9]
# b=[3,7,9]
# c=[]
# for x in a:
# 	if x in b:
# 		pass
# 	else:
# 		c.append(x)
# print c


# # BUBBLESORT
# d=[7,2,6,4,9,1,3,10,5,8]
# # d.sort()
# print "BEFORE SORTING :",d
# n=len(d)
# for i in range(n):
# 	for j in range(0,n-i-1):
# 		if d[j]>d[j+1]:
# 			d[j],d[j+1]=d[j+1],d[j]
# 	print d
# print "AFTER SORTING :",d


# #SELECTION SORT
# d=[7,2,6,4,9,1,3,10,5,8]
# print "BEFORE SORTING :",d
# for i in range(len(d)):
# 	min_idx=i
# 	for j in range(i+1,len(d)):
# 		if d[min_idx]>d[j]:
# 			min_idx=j
# 	d[i],d[min_idx]=d[min_idx],d[i]
# 	print d
# print "AFTER SORTING :",d

# Get Key of Dictionary using Value:
mydict = {'george':16,'amber':19}
print "mydict.values()).index(16) :",list(mydict.values()).index(16)
print list(mydict.keys())
print list(mydict.keys())[list(mydict.values()).index(16)]


l=[1,2,3,4,5]
ld={}
for i in l:
	
