#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
count=0
for y in range(n - 1):
    for i in range(n-1):
        if a[i]<a[i+1]:
            pass
        else:
            tmp=a[i]
            a[i]=a[i+1]
            a[i+1]=tmp
            count+=1
print "Array is sorted in %s swaps." %count
print "First Element: %s" %a[0]
print "Last Element: %s" %a[n-1]
