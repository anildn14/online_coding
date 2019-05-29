# A stream of data is received and needs to be reversed.

# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)
# should become:

# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)
# The total number of bits will always be a multiple of 8.

# The data is given in an array as such:

# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

# data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
# data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

# test.assert_equals(data_reverse(data1),data2)

# data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
# data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
# test.assert_equals(data_reverse(data3),data4)

def data_reverse(data):
	# print len(data)/8
	n=[]
	for i in range((len(data)/8),0,-1):
		# print data[8*(i-1):8*(i)]
		# print ''.join(data[8*(i-1):8*(i)])
		 # ''.join(str(data[8*(i-1):8*i]))
		n.extend(data[8*(i-1):8*i])
	# print [x for x in n[::-1]]
	print n
	# return [(data[8*(i-1):8*i] for i in range((len(data)/8),0,-1)]
print data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0])


def data_reverse(data):
  res = []
  
  for i in range(len(data)-8, -1, -8):
    res.extend(data[i:i+8])
  
  return res


def data_reverse(data):
    return [b for a in xrange(len(data) - 8, -1, -8) for b in data[a:a + 8]]