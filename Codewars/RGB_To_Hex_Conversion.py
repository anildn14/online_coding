# The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
# The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

# test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
# test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
# test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
# test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
# test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")

def rgb(r, g, b):
	op=''
	if r < 0:op+='00'
	elif r>255:op+='FF'
	else:op+='{0:02X}'.format(int(r))
	if g < 0:op+='00'
	elif g>255:op+='FF'
	else:op+='{0:02X}'.format(int(g))
	if b< 0:op+='00'
	elif b>255:op+='FF'
	else:op+='{0:02X}'.format(int(b))
	return op
print rgb(-20,275,125)



def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))



def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num
def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))