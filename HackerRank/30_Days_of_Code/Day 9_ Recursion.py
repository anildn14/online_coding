import sys


def factorial(n):
    xyz=1
    for i in range(n):

        xyz = xyz * (n - 1)
        # i += 1
        print "i :",i
        print "xyz :",xyz
    # Complete this function


if __name__ == "__main__":
    n = int(raw_input().strip())
    result = factorial(n)
    print result