# Write a function last that accepts a list and returns the last element in the list.

# If the list is empty:

# In languages that have a built-in option or result type (like OCaml or Haskell), return an empty option

# In languages that do not have an empty option, just return None
# @test.describe('Sample Tests')
# def fixed_tests():

#     @test.it('Sample Test Cases')
#     def sample_tests():
#         test.assert_equals( last([1,2,3]), 3, "last([1,2,3]) == 3")
#         test.assert_equals( last([]), None, "last( [] ) == None")
def last(lst):
	if lst==[]:
		return None
	return lst[::-1][0]
print last([1,2,3])