#!/bin/python
def factorial(n):
    result=1
    while n>0:
        result=result*n
        n-=1
    return result
if __name__ == "__main__":
    n = int(raw_input().strip())
    result = factorial(n)
    print result