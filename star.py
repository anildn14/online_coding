# #    *   
# #   * *
# #  * * *
# # * * * *

# # n=4
# # for i in range(1,n+1):
# # 	for j in range(1,n-i+1):
# # 		print " ",
# # 	for k in range(1,i+1):
# # 		print "*  ",
# # 	print "\n"
# # for x in range(n-1,0,-1):
# # 	for j in range(1,n-x+1):
# # 		print " ",
# # 	for k in range(1,x+1):
# # 		print "*  ",
# # 	print "\n"

# # import sys
# # print "#"*15

# # n=4
# # for i in range(1,n+1):
# # 	for j in range(1,n-i+1):
# # 		print " ",
# # 		# sys.stdout.write(" ")
# # 	for k in range(1,i+1):
# # 		print "*  ",
# # 		# sys.stdout.write("* ")
# # 	print "\n"

# # print "#"*15

# # n=4
# # for x in range(n,0,-1):
# # 	for j in range(1,n-x+1):
# # 		print " ",
# # 	for k in range(1,x+1):
# # 		print "*  ",
# # 	print "\n"

# # print "#"*15

# # n=4
# # for x in range(n,0,-1):
# # 	for j in range(1,n-x+1):
# # 		print " ",
# # 	for k in range(1,x+1):
# # 		print "*",
# # 	print "\n"


# # print "#"*15

# # n=4
# # for x in range(n,0,-1):
# # 	for k in range(1,x+1):
# # 		print "*",
# # 	for j in range(1,n-x+1):
# # 		print " ",
# # 	print "\n"


# # print "#"*15

# # n=4
# # for x in range(n,0,-1):
# # 	for k in range(1,x+1):
# # 		print str(x),
# # 	for j in range(1,n-x+1):
# # 		print " ",
# # 	print "\n"


# # print "#"*15

# # n=["a","b","c","d"]
# # for x in range(1,len(n)+1):
# # 	for j in range(1,len(n)-x+1):
# # 		print " ",
# # 	for k in range(1,x+1):
# # 		print str(n[x-1])+"  ",
# # 	print "\n"
# # for x in range(len(n)-1,0,-1):
# # 	for j in range(1,len(n)-x+1):
# # 		print " ",
# # 	for k in range(1,x+1):
# # 		print str(n[x-1])+"  ",
# # 	print "\n"


# # print "#"*15

# # n=["a","b","c","d"]
# # for x in range(len(n),0,-1):
# # 	for j in range(1,len(n)-x+1):
# # 		print " ",
# # 	for k in range(1,x+1):
# # 		print str(n[x-1])+"  ",
# # 	print "\n"

# # print "#"*15
# # # n=4
# # # for x in range(1,n+1):
# # # 	for y in range(x):
# # # 		print x

# # def palindrome(N):
# # 	for x in range(N,0,-1):
# # 		for j in range(1,N+1):
# # 			print "#",
# # 		for i in range(1, N + 1):
# # 			print(int('1' * i)**2)
# # 		print '\n'
# # # palindrome(5)


# # n=9
# # for i in range(1,n+1):
# # 	print " "*(n-i)+str(int('1' * i)**2)
# # for i in range(n-1,0,-1):
# # 	print " "*(n-i)+str(int('1' * i)**2)

# # n=9
# # for i in range(1,n):
# # 	print ((n-i)*' '+i*'* ')
# # for j in range(n-2,0,-1):
# # 	print ((n-j)*' '+j*'* ')


# # n=["a","b","c","d"]
# # for x in range(len(n)):
# # 	print ' '.join(x for x in n[0:x+1] + n[x::-1])
# # # # for x in range(len(n),0,-1):
# # # 	for j in range(1,len(n)-x+1):
# # # 		print " ",
# # # 	for k in range(1,x+1):
# # # 		print str(n[x-1])+"  ",
# # # 	print "\n"

# # # for i in range(1,n):
# # 	# print ((n-i)*' '+i*'* ')

# # n=5
# # for i in range(1,n):
# # 	print ((n-i)*' '+i*'* ')

# # for i in range(1,n):
# # 	print ((n-i)*''+i*'*')

# # for i in range(1,n):
# # 	print ((n-i)*' '+i*'*')

# # for i in range(0,n):
# # 	print (" "*i+"* "*(n-i))

# # stl=4
# # for i in range(stl):
# # 	print '*'*stl

# # for i in range(6):
# # 	for j in range(3):
# # 		print '*',
# # 	print '\n'

# # for i in range(10):
# # 	for j in range(i+1):
# # 		print j,
# # 	print '\n'

# # n=1
# # for i in range(0,5):
# # 	for j in range(0,i+1):
# # 		print n,
# # 		n=n+1
# # 	print '\n'


# # n=65
# # for i in range(0,7):
# # 	for j in range(0,i+1):
# # 		conv=chr(n)
# # 		print conv,
# # 		n=n+1
# # 	print '\n'



# # l1=[1,5,6,9,11]
# # l2=[1,5,6,9,11,15]
# # s1=len(l1)
# # s2=len(l2)
# # res=[]
# # i,j=0,0
# # while i<s1 and j<s2:
# # 	if l1[i] < l2[j]:
# # 		res.append(l1[i])
# # 		i+=1
# # 	else:
# # 		res.append(l2[j])
# # 		j+=1
# # res=res+l1[i:]+l2[j:]
# # print res


# # x = [1,2,3,4]
# # f = [1,11,22,33,44,3,4]

# # res = list(set(x+f))
# # print(res)

# # l1 = [1,2,3,4]
# # l2 = [1,11,22,33,44,3,4]
# # res = []
# # i,j=0,0
# # while i<len(l1) and j<len(l2):
# # 	if l1[i] in res:
# # 		i+=1
# # 	else:
# # 		res.append(l1[i])
# # 		# i+=1
# # 	if l2[j] in res:
# # 		j+=1
# # 	else:
# # 		res.append(l2[j])
# # 		# j+=1
# # print res

# # n = 3
# # list_1 = [1, 2, 3, 4, 5, 6] 
# # list_1 = (list_1[len(list_1) - n:len(list_1)] + list_1[0:len(list_1) - n]) 
# # print(list_1) 

# # n = 4
# # list_1 = [1, 2, 3, 4, 5, 6, 1, 7]
# # list_2 = [5, 6, 1, 7, 1, 2, 3, 4]
# # list_1 = (list_1[-n:] + list_1[:-n])
# # print list_1

# # print list_2.index(1)
# # n=-(2+1)
# # list3 = (list_2[-n:] + list_2[:-n])
# # print list3
# # print list3 == list_1
# # print list3.pop(1)	
# # print list3.remove(1)


# l=[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
# print len(l)
# count0=len(l)-l.index(0)
# print "count0 :",count0

# l=[1,2,3,4,5,6,7]
# print l[-3]

# dic={}
# l=[1,2,3,4,5,6,7,8,9,11,12,13,45,46,123,8,21,3,5,31,2,5,321,41,1,5,2,6,4,123]
# for x in l:
# 	if x not in dic:
# 		dic[x]=1
# 	else:
# 		dic[x]+=1
# print "dic :",dic


# def myFun(*args, **kwargs):  
# 	for arg in args:
# 		print arg
# 	for key, value in kwargs.items():
# 		  print ("%s == %s" %(key, value)) 
  
# # Driver code 
# myFun("Hi", first ='Geeks', mid ='for', last='Geeks')

# class A: 
#       def names(self, n = 'Rahul'): 
#               self.name = n 
#               return self.name
# class B(A): 
#       def __init__(self, roll): 
#               self.roll = roll 
  		
# object = B(23) 
# print object.roll
# print object.names()


import copy 
  
# initializing list 1 
li1 = [1, 2,[3,5], 4] 
print id(li1)
# using deepcopy to deep copy  
li2 = copy.deepcopy(li1) 
# original elements of list 
print ("The original elements before deep copying") 
for i in range(0,len(li1)): 
    print "li1[%s] :"%i,li1[i]#,end=" ") 
  
print("\r")
  
# adding and element to new list 
li2[2][0] = 7
print "li2 :",li2,li1,id(li1),id(li2)
# Change is reflected in l2  
print ("The new list of elements after deep copying ") 
for i in range(0,len( li1)): 
    print "li2[%s] :"%i,li2[i]#,end=" ") 
  
print("\r") 

print ("The original elements after deep copying") 
for i in range(0,len( li1)): 
    print "li1[%s] :"%i,li1[i]#,end=" ") 
print("\r") 

li3 = copy.copy(li1) 
li3[2][0] = 9
print "li3 :",li3,li1,id(li1),id(li3)
# Change is reflected in l2  
print ("The new list of elements after copying ") 
for i in range(0,len( li1)): 
    print "li3[%s] :"%i,li3[i]#,end=" ") 
  
print("\r") 

  
# Change is NOT reflected in original list 
# as it is a deep copy 
print ("The original elements after copying") 
for i in range(0,len( li1)): 
    print "li1[%s] :"%i,li1[i]#,end=" ") 