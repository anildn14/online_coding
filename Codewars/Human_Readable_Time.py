# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

#     HH = hours, padded to 2 digits, range: 00 - 99
#     MM = minutes, padded to 2 digits, range: 00 - 59
#     SS = seconds, padded to 2 digits, range: 00 - 59

# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

# Test.assert_equals(make_readable(0), "00:00:00")
# Test.assert_equals(make_readable(5), "00:00:05")
# Test.assert_equals(make_readable(60), "00:01:00")
# Test.assert_equals(make_readable(86399), "23:59:59")
# Test.assert_equals(make_readable(359999), "99:59:59")

def make_readables(seconds):
    HH=(seconds-(seconds%3600))/3600
    MM=(seconds-(HH*3600))/60
    SS=(seconds%60)
    print "%02d:%02d:%02d"%(HH,MM,SS)


def make_readable(s):
	return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

print make_readable(8)
print make_readable(359)
print make_readable(359998)
print 608%3600
print 359999%3600
