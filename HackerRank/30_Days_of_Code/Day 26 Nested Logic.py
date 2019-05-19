# If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0).
# If the book is returned after the expected return day but still within the same calendar month and year as the
# expected return date,fine=15 Hackos x the no of days late.
# If the book is returned after the expected return month but still within the same calendar year as the expected
# return date, the fine=500 Hackos x the no of months late .
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 hackos.

#a=actual e=expected

a=raw_input().split(" ")
print a
e=raw_input().split(" ")
print e
# print e.split(" ")
# print e.split(" ")[0]
# if a[0]>=e[0] and a[1]==e[1] and a[2]==e[2]:
# #     fine=0
# # else:
#     fine=15 * (int(a[0])-int(e[0]))
#
# elif a[1]>=e[1] and a[2]==e[2]:
# #     fine=0
# # else:
#     fine=500*((int(a[1])-int(e[1])))
#
# elif a[2]==e[2]:
# #     fine=0
# # else:
#     fine=10000
#
# print fine
#
# # print date_fine
# # print month_fine
# # total_fine=date_fine + month_fine
# # print total_fine

if int(a[2])<int(e[2]):
    fine=0
elif int(a[2])>int(e[2]):
    fine=10000

elif int(a[1])>int(e[1]):
    fine=500*((int(a[1])-int(e[1])))

elif int(a[0])>int(e[0]):
    fine=15*((int(a[0])-int(e[0])))
else:
    fine=0
print fine



