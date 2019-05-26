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




global c
c=0
def persistences(m):
	# global c
	c=0
	i=1
	while m>=10:

		for n in str(m):
			i=i*int(n)
			# i = i - 1
			print c,i,n
		print "*"*50
		# persistences(m)
		print "m,i :",m,i
	# if len(str(i))!=1:
	# 	persistence(i)
	# elif len(str(i))==1:
	# 	print "hi"
	# 	return c

##########################################################33
def get_digits(num):
    digits = []
    while num:
        num, digit = divmod(num, 10)
        digits.append(digit)
    return digits


def multiply_all(digits):
    multiplier = 1
    while digits:
        multiplier *= digits.pop()
    return multiplier


def persistence(num):
    count = 0
    while num >= 10:
        num = multiply_all(get_digits(num))
        count += 1
    return count


###############################################################    

import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
#############################################################
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist

####################################################

def persistencey(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count
print persistence(39)
print persistence(4)
print persistence(25)
print persistencey(999)