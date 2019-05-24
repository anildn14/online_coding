# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example:
#  persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        # and 4 has only one digit.

#  persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
#                        # 1*2*6 = 12, and finally 1*2 = 2.

#  persistence(4) => 0   # Because 4 is already a one-digit number.
#  persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
#                  # and 4 has only one digit

#  persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
#                   # 1*2*6=12, and finally 1*2=2

#  persistence(4) # returns 0, because 4 is already a one-digit number

# Test.it("Basic tests")
# Test.assert_equals(persistence(39), 3)
# Test.assert_equals(persistence(4), 0)
# Test.assert_equals(persistence(25), 2)
# Test.assert_equals(persistence(999), 4)

print len("65")

def persistence(n):
	res=1	
	for i in str(n):
		print "i :",i
		res = res * int(i)
		print "res :",res,len(str(res))
	if len(str(res))==1:
		return res
	else:
		persistence(res)
	# if len(str(res))!=1:
	# 	print "res if:",res
	# 	persistence(res)
	# return res
print persistence(39)
	# print get_digits(n)
	# res=1
	# while n > 0:
	#     d = n%10
	#     n = n//10
	#     res *= d
	#     # if len(str)
	# print res

	# print ''.join(str(x) for x in str(n))
	# for a in str(n):
	# 	if a and len(str(n))!=0:
	# 		res*=int(a)
	# 		n=res
	# 		print res

