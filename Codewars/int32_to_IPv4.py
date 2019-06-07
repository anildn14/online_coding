# Take the following IPv4 address: 128.32.10.1

# This address has 4 octets where each octet is a single byte (or 8 bits).

# 1st octet 128 has the binary representation: 10000000
# 2nd octet 32 has the binary representation: 00100000
# 3rd octet 10 has the binary representation: 00001010
# 4th octet 1 has the binary representation: 00000001
# So 128.32.10.1 == 10000000.00100000.00001010.00000001

# Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

# Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

# Examples
# 2149583361 ==> "128.32.10.1"
# 32         ==> "0.0.0.32"
# 0          ==> "0.0.0.0"

# Test.assert_equals(int32_to_ip(2154959208), "128.114.17.104") 
# Test.assert_equals(int32_to_ip(0), "0.0.0.0")
# Test.assert_equals(int32_to_ip(2149583361), "128.32.10.1")

def int32_to_ip(int32):
	n='00001011'
	m=32
	bi='{0:2b}'.format(int(2149583361))
	a=0
	print bi
	print int(n,2)
	print bin(32)
	di='{0:2b}'.format(int(a)).strip().zfill(32)
	# di='{0:2b}'.format(int(a)).strip()#.zfill(32)
	# di=di.rjust(9, '0')
	print "di :",di
	di=di.zfill(32)
	print di.zfill(32),type(di)
	print '{0:32d}'.format(int(32))
	print di[0:8]
	print int(di[0:8],2)
	print int(di[24:32],2)
	print '{}.{}.{}.{}'.format(int(di[0:8],2),int(di[8:16],2),int(di[16:24],2),int(di[24:32],2))
	print '%d.%d.%d.%d'%(int(di[0:8],2),int(di[8:16],2),int(di[16:24],2),int(di[24:32],2))
int32_to_ip(5)



def int32_to_ip(int32):
  bi='{0:2b}'.format(int32).strip().zfill(32)
  return '{}.{}.{}.{}'.format(int(bi[0:8],2),int(bi[8:16],2),int(bi[16:24],2),int(bi[24:32],2))
# print int32_to_ip(5)


def int32_to_ip(int32):
    return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))
print int32_to_ip(5)



from ipaddress import IPv4Address
from ipaddress import ip_address

def int32_to_ip(int32):
    return str(IPv4Address(int32))
# print int32_to_ip(5)
