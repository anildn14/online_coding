# Create a function args_count, that returns the count of passed argument
# args_count(1, 2, 3) -> 3
# args_count(1, 2, 3, 10) -> 4
# test.describe("Basic tests")
# test.assert_equals(args_count(100), 1)
# test.assert_equals(args_count(100, 2, 3), 3)
# test.assert_equals(args_count(32, a1=12), 2)
# test.assert_equals(args_count(), 0)

def args_count(*args,**kwargs):
	return len(kwargs)+len(args)

print args_count(32, a1=12)