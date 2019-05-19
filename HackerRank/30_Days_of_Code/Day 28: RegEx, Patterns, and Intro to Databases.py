# # Input Format
# #
# # The first line contains an integer,N , total number of rows in the table.
# # Each of the N subsequent lines contains 2 space-separated strings denoting a person's first name and email ID, respectively.
# #
# # Constraints
# #
# #     Each of the first names consists of lower case letters a-z only.
# #     Each of the email IDs consists of lower case letters a-z,@ and . only.
# #     The length of the first name is no longer than 20.
# #     The length of the email ID is no longer than 50.
# #
# # Output Format
# #
# # Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed on a new line.
# #
# # Sample Input
# #
# # 6
# # riya riya@gmail.com
# # julia julia@julia.me
# # julia sjulia@gmail.com
# # julia julia@gmail.com
# # samantha samantha@gmail.com
# # tanya tanya@gmail.com
# #
# # Sample Output
# #
# # julia
# # julia
# # riya
# # samantha
# # tanya
#
#
# #!/bin/python
# import sys
# import re
# N = int(raw_input().strip())
# dict={}
# for a0 in xrange(N):
#     firstName,emailID = raw_input().strip().split(' ')
#     dict[firstName]=emailID
#     print dict
#     # [firstName,emailID] = [str(firstName),str(emailID)]
#     # print "firstName :",firstName
#     # print "emailID :",emailID
# # for x in dict.values():
# #     print dict.values()
# #     if re.match('[a-z]+@gmail.com',x):
# #         print True
# #         print dict.keys()

import re
N = int(raw_input().strip())
abc=[]
for a0 in xrange(N):
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]

    if re.match('[a-z.]+@gmail.com', emailID):
        abc.append(firstName)
abc.sort()
print abc
print '\n'.join(abc)


# Online Answer:
import re
arr = []
n = int(input())
for i in range(n):
    data = str(raw_input()).split(" ")
    name = data[0]
    email = data[1]
    if re.search(".+@gmail\.com$", email):
        arr.append(name)
arr.sort()
for name in arr:
    print(name)

# 6
# riya riya@gmail.com
# julia julia@julia.me
# julia sjulia@gmail.com
# julia julia@gmail.com
# samantha samantha@gmail.com
# tanya tanya@gmail.com



# EXTRA TEST CASES
# INPUT:
# 30
# riya riya@gmail.com
# julia julia@julia.me
# julia sjulia@gmail.com
# julia julia@gmail.com
# samantha samantha@gmail.com
# tanya tanya@gmail.com
# riya ariya@gmail.com
# julia bjulia@julia.me
# julia csjulia@gmail.com
# julia djulia@gmail.com
# samantha esamantha@gmail.com
# tanya ftanya@gmail.com
# riya riya@live.com
# julia julia@live.com
# julia sjulia@live.com
# julia julia@live.com
# samantha samantha@live.com
# tanya tanya@live.com
# riya ariya@live.com
# julia bjulia@live.com
# julia csjulia@live.com
# julia djulia@live.com
# samantha esamantha@live.com
# tanya ftanya@live.com
# riya gmail@riya.com
# priya priya@gmail.com
# preeti preeti@gmail.com
# alice alice@alicegmail.com
# alice alice@gmail.com
# alice gmail.alice@gmail.com
#
#
# OUTPUT:
# alice
# alice
# julia
# julia
# julia
# julia
# preeti
# priya
# riya
# riya
# samantha
# samantha
# tanya
# tanya