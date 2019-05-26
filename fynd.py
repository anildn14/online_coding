sum=8
l=[1,3,5,4,7,6,9,2,8]

res=[]
for i in range(len(l)):
    for j in range(0,len(l)):
        if l[i]+l[j]==sum:
        	print l[i],l[j]
        	break

