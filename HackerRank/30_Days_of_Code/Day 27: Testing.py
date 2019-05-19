t=int(raw_input("Lectures"))
for i in range(t):
    n=raw_input("Students/Cancel").split(" ")
    a=raw_input("Time").split(" ")
    count = 0
    for j in range(int(n[0])):
        if int(a[j])<=0:
            count+=1
    if count>=int(n[1]):
        print "YES"
    else:
        print "NO"


# print('5')
# print('4 3')
# print('-1 -3 4 2')
# print('5 2')
# print('0 -1 2 1 4')
# print('4 3')
# print('-1 -3 4 2')
# print('5 2')
# print('0 -1 2 1 4')
# print('4 3')
# print('-1 -3 4 0')