S = raw_input().strip()
try:
    S=int(S)
    print S
except ValueError:
    print "Bad String"