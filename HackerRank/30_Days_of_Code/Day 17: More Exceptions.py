class Calculator():
    def power(self,no1,no2):
        # try:
            if no1>0 and no2>0:
                return no1**no2
            else:
        # except Exception:# as e:
                raise Exception("n and p should be non - negative")


myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e


#Actual Answer:

# class Calculator:
#     def power(self, n, p):
#         if n < 0 or p < 0:
#             raise Exception("n and p should be non-negative")
#         return pow(n, p)


# class Calculator():
#     def power(self,n,p):
#         if n<0 or p<0:
#             raise Exception("n and p should be non-negative")
#         else:
#             return n**p