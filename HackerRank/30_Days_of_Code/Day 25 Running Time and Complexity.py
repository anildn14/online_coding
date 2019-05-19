T=int(raw_input("Enter Test cases: "))
for i in range(T):
    data = int(input("Print the number: "))
    print "data :",data
    for x in range(2,data+1):
        if data==1:
            print "Number is not prime"
        if data%x==0 and x<data:
            print "Number is not prime"
            break
        elif data==x:
            print "prime"
            break
#ACTUAL ANSWER:

# from math import sqrt
#
# T = int(input())
#
# def isPrime(n):
#     for i in range(2, int(sqrt(n))+1):
#         if n % i is 0:
#             return False
#     return True
#
# for _ in range(T):
#     n = int(input())
#
#     if n >= 2 and isPrime(n):
#         print("Prime")
#     else:
#         print("Not prime")