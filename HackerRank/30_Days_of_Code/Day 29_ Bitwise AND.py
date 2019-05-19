#!/bin/python

A=1
B=2
print A&B

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    S=set(range(1,n+1))
    # for i in range(1,int(n)+1):
    #     S.add(i)
    # print S
    # print len(S)
    # for i in len(S):
    #     while i:
    and_list=[]
    for i in S:
        for j in range(i,len(S)+1):
            if i!=j:
                if i&j<k:
                    and_list.append(i&j)
    # print "and_list :",and_list
    print max(and_list)

# ONLINE ANSWER:

# #!/bin/python3
# import sys
# t = int(input().strip())
# for a0 in range(t):
#     n,k = input().strip().split(' ')
#     n,k = [int(n),int(k)]
#     print(k-1 if ((k-1) | k) <= n else k-2)