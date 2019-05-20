def jumpingOnClouds(c):
	count=0
	for i in c:
		if i == 0:
			

		
n = int(raw_input())
c = map(int, raw_input().rstrip().split())
c=[0, 0, 1, 0, 0, 1, 0]		#4
c=[0, 0, 0, 0, 1, 0]		#3
result = jumpingOnClouds(c)