#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.

dic={}
def sockMerchant(n, ar):
	pairs=0
	for i in ar:
		if i not in dic:
			dic[i]=1
		else:
			dic[i]+=1
	print "dic :",dic
	for i in dic.values():
		pairs+=i//2
	return pairs
if __name__ == '__main__':
    n = int(raw_input("Enter no of inputs :"))
    ar = map(int, raw_input("Enter the pairs :").rstrip().split())
    result = sockMerchant(n, ar)
    print "result :",result