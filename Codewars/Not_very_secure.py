# In this example you have to validate if a user input string is alphanumeric. The given string is not nil, so you don't have to check that.

# The string has the following conditions to be alphanumeric:

# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces/underscore
# test.assert_equals(alphanumeric("hello_world"), False)
# test.assert_equals(alphanumeric("PassW0rd"), True)
# test.assert_equals(alphanumeric("     "), False)
# test.assert_equals(alphanumeric("a"), True)

import string
def alphanumeric(string):
    print string.isalnum()

alphanumeric("hello_world")
alphanumeric("PassW0rd")
alphanumeric("     ")
alphanumeric("a")