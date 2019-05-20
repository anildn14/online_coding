def countingValleys(n, s):
	valley=0
	count=0
	# print s
	# print s.index("D")
	# print s.index("U")
	# high = 0
	# for i in s[s.index("D")::]:
	# 	if i == "D":
	# 		count-=1
	# 	else:
	# 		count+=1
	# print "count :",count

	for i in s:
		if i == "U":
			count+=1
		else:
			count -=1
		if count == 0 and i =="U":
			valley+=1
	print valley
if __name__ == '__main__':
    # n = int(raw_input())
    # s = raw_input()
    n=8
    s="UDDDUDUU"		#1
    # s="DDUUUUDD"		#1
    s="DDUUDDUDUUUD"	#2
    result = countingValleys(n, s)
	# print "result :",result
