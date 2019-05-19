#!/bin/python

import sys


n = int(raw_input("Enter Number : ").strip())

print "\nusing for\n"


for i in range(1,11):
    op=n*i
    # i+=1
    print "%s x %s = %s"%(n,i,op)

print "\nusing while\n"

j=1

while 1<=j<=10:
    opt = n * i
    print "%s x %s = %s" % (n, j, opt)
    j += 1