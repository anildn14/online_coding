# n sorted array of int 
# a=[1,4,10,2,3]
# 2nd highest no
# dont use sort and loop through only once

# a=[1,4,10,2,3]
# max_no= max(a)
# a.remove(max_no)
# print max(a)

# n=len(a)
# for i in range(n):
# 	while i!=n-1:
# 		if a[i] > a[i+1]:
# 			a[i],a[i+1]=a[i+1],a[i]
# print a[n-2]



cur=[2000,500,100,50,20,10,5,2]
amount=2553
#split it with minimum no of notes
count=[0,0,0,0,0,0,0,0]

for i,j in zip(cur,count):
	if amount>=i:
		j=amount//i
		amount=amount-j*i
		print (i,j)

print  "%s cant be splitted further"%amount
	


