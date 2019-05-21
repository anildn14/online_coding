# Task:
# Given an array of strings, reverse them and their order in such way that their length stays the same as the length of the original inputs.
# Example:
# Input:  {"I", "like", "big", "butts", "and", "I", "cannot", "lie!"}
# Output: {"!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"}
# Test.assert_equals(
#     reverse(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"]),
#             ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"]
# )

# Test.assert_equals(
#     reverse(["?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta", "eote", "vahu", "oyodpm", "ir", "hsyn", "amwoH"]),
#             ["How", "many", "shrimp", "do", "you", "have", "to", "eat", "before", "your", "skin", "starts", "to", "turn", "pink?"]
# )

def reversed(a):
	rev=''.join(a)
	rev=rev[::-1]
	og=[]
	for i in a:
		og.append(len(i))
	# print og
	new=[]
	start,end=0,0
	for i in og:
		start,end=end,i+end
		new.append(rev[start:end])
	return new

def reverse1(a):
    s=reversed(''.join(a))
    print s
    return [''.join(next(s) for _ in w) for w in a]

def reverse(a):
    s = ''.join(a)[::-1]
    print s
    l, x = [], 0
    print l,x
    for i in a:
        l.append(s[x:x+len(i)])
        x += len(i)
    return l


print reverse(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"])
print reverse(["?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta", "eote", "vahu", "oyodpm", "ir", "hsyn", "amwoH"])