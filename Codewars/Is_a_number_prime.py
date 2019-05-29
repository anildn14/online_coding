# Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# Assumptions
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
# There are no fancy optimizations required, but still the most trivial solutions might time out. Try to find a solution which does not loop all the way up to n.

# @Test.describe("Basic")
# def basic():
	
#     @Test.it("Basic tests")
#     def basic_tests():
#         Test.assert_equals(is_prime(0),  False, "0  is not prime")
#         Test.assert_equals(is_prime(1),  False, "1  is not prime")
#         Test.assert_equals(is_prime(2),  True, "2  is prime")
#         Test.assert_equals(is_prime(73), True, "73 is prime")
#         Test.assert_equals(is_prime(75), False, "75 is not prime")
#         Test.assert_equals(is_prime(-1), False, "-1 is not prime")

	
#     @Test.it("Test prime")
#     def test_prime():
#         Test.assert_equals(is_prime(3),  True, "3  is not prime");
#         Test.assert_equals(is_prime(5),  True, "5  is not prime");
#         Test.assert_equals(is_prime(7),  True, "7  is prime");
#         Test.assert_equals(is_prime(41), True, "41 is prime");
#         Test.assert_equals(is_prime(5099), True, "5099 is prime");
		
#     @Test.it("Test not prime")
#     def test_not_prime():
#         Test.assert_equals(is_prime(4),  False, "4  is not prime");
#         Test.assert_equals(is_prime(6),  False, "6  is not prime");
#         Test.assert_equals(is_prime(8),  False, "8  is prime");
#         Test.assert_equals(is_prime(9), False, "9 is prime");
#         Test.assert_equals(is_prime(45), False, "45 is not prime");
#         Test.assert_equals(is_prime(-5), False, "-5 is not prime");
#         Test.assert_equals(is_prime(-8), False, "-8 is not prime");
#         Test.assert_equals(is_prime(-41), False, "-41 is not prime");

import math

def is_prime(num):
	# if 
	if num > 1:
		for n in range(2,int(math.sqrt(num))+1):
		# for n in range(2,int(math.ceil(math.sqrt(num)))+1):
		# for n in range(2,(num/2)+1):
			# for y in range(2,(n/2)+1):
			# 	if n % y==0:
			# 		return False
			if num % n==0:
				return False
		return True
	return False

print is_prime(-5)
print is_prime(9)
print is_prime(524287)
print int(math.sqrt(10))
print is_prime(2147483647)




# -*- coding: utf-8 -*-
def is_prime(num):
    import math

    # There's only one even prime: 2
    if num < 2    : return False
    if num == 2   : return True
    if num %2 == 0: return False
    """
    Property:
        Every number n that is not prime has at least one prime divisor p
        such 1 < p < square_root(n)
    """
    root = int(math.sqrt(num))
    # We know there's only one even prime, so with that in mind 
    # we're going to iterate only over the odd numbers plus using the above property
    # the performance will be improved
    for i in xrange(3, root+1, 2):
        if num % i == 0: return False

    return True