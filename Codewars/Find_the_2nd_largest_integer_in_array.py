# Find the 2nd largest integer in array If the array has no 2nd largest integer then return nil.
# Reject all non integers elements and then find the 2nd largest integer in array

# find_2nd_largest([1,2,3]) => 2

# find_2nd_largest([1,1,1,1,1]) => nil because all elements are same. Largest no. is 1. and there is no 2nd largest no.

# find_2nd_largest([1,'a','2',3,3,4,5,'b']) => 4 as after rejecting non integers array will be [1,3,3,4,5]
# Largest no. is 5. and 2nd largest is 4.

# Return nil if there is no 2nd largest integer. Take care of big numbers as well

# test.describe("Example Tests")
# test.assert_equals(find_2nd_largest([1,2,3]), 2)
# test.assert_equals(find_2nd_largest([1,1,1,1,1,1,1]), None)
# test.assert_equals(find_2nd_largest([1,'a','2',3,3,4,5,'b']),4)
# test.assert_equals(find_2nd_largest([1,'a','2',3,3,3333333333333333333334,
# 544444444444444444444444444444,'b']),3333333333333333333334)

def find_2nd_largest(arr):
	# arr=list(set(arr))
	if len(set(arr))==1:
		return None
	else:
		arr1=[x for x in arr if not type(x)==str ]
		l=arr1[0]
		l2=None
		print l,l2,arr,arr1
		for x in arr1[1:]:
			print "x,l,l2 :",x,l,l2
			# print x
			if long(x)>long(l):#: and type(x)!=str :
				l2=l
				l=long(x)
			elif l2 == None or long(l2)<long(x):
				l2=long(x)
		return l,l2
# print find_2nd_largest([1,2,3])
# print find_2nd_largest([1,1,1,1,1,1,1])
# print find_2nd_largest([1,'a','2',3,3,4,5,'b','b'])
# print find_2nd_largest([1,'a','2',3,3,3333333333333333333334,544444444444444444444444444444,'b'])
print find_2nd_largest(['k', 'A', 14844, 'T', 75663, 93592, 2254, 'j', 'f', 15919, 99054, '1', 'A', 91192, 76485, 'n', 'W', 84194, 'r', 53906])
print find_2nd_largest(['W', 99633, 19141, 91590, 'r', 43539, 33036, 'O', 86486, 'O', 'C', '5', 27723, 83160, 30571, 'I', 'Q', 'C', 'I', 53004])
# a=[1,'a','2',3,3,3333333333333333333334,544444444444444444444444444444,'b']
# for x in a:
# 	print type(x)
print long(99633)<long(91590)
# print long(3333333333333333333334)
# print long(4)


def find_2nd_largest(arr):
    arr = sorted(i for i in set(arr) if type(i) != str)
    return arr[-2] if len(arr) > 1 else None
print find_2nd_largest([1,'a','2',3,3,3333333333333333333334,544444444444444444444444444444,'b'])
print find_2nd_largest(['W', 99633, 19141, 91590, 'r', 43539, 33036, 'O', 86486, 'O', 'C', '5', 27723, 83160, 30571, 'I', 'Q', 'C', 'I', 53004])
