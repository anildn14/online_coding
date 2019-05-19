# #!/bin/python
#
# # import sys
# # import counter
# #
# # n = int(raw_input("Enter no: ").strip())
# # print n
# # print bin(n)
# # a=str("{0:b}".format(n))
# # print a
# # print len(str(a))
# # print counter.Counter(str("{0:b}".format(n)))
# # count =1
# #
# # for x in range(len(str(a))):
# #     print x
# #     if x==0 and a[x]=="1":
# #         count=1
# #     elif a[x]=="1" and a[x-1]=="1":
# #         count+=1
# #     else:
# #         count=1
# # print "count :",count
#
#
# num = int(input())
#
# result = 0
# maximum = 0
#
# while num > 0:
#     if num % 2 == 1:
#         result += 1
#         if result > maximum:
#             maximum = result
#
#     else:
#         result = 0
#     num //= 2
#     # print (num //= 2)
#
# print(maximum)

n = int(input())

max_one_count = 0
one_count = 0

while n != 0:							#15!=0			#
	factor = n // 2						#15//2=7		7//2=3		3//2=1		1//2=0		0//2=0
    # print "factor :",factor
	remainder = n - (2 * factor) 		#15-(2*7)==1	7-(2*3)==1	3-(2*1)==1	1-(2*0)==1	0-(2*0)==0
    # print "remainder :",remainder
	n = factor							#n=7			n=3			n=1			n=0			n=0
	if remainder == 1:
		one_count += 1
		max_one_count = max(max_one_count, one_count)
	else:
		one_count = 0

print(max_one_count)

#15==1111;
print 15//2
print 1//2
print 0//2