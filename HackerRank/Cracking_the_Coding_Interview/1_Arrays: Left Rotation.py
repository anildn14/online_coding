def array_left_rotation(a, n, k):
    for i in range(k):
        temp=a[0]
        a=a[1:]
        a.append(temp)
    for i in a:
        # print i
        # print type(i)
        # print ''.join(str(i)),
        print i,

n, k = map(int, raw_input().strip().split(' '))
a = list(map(int, raw_input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
# print(*answer, sep=' ')
#
# a=[1 ,2, 3]
# print a
# temp=a[0]
# a=a[1:]
# print a
# a.append(temp)
# print a

# PYTHON 2 Solution
# def array_left_rotation(a, n, k):
#     return a[k:n] + a[:k]
# 
# n, k = map(int, raw_input().strip().split(' '))
# a = list(map(int, raw_input().strip().split(' ')))
# answer = array_left_rotation(a, n, k)
# print ' '.join(str(i) for i in answer),

# PYTHON 3 Solution
# def array_left_rotation(a, n, k):
#     return a[k:n] + a[:k]
#
# n, k = map(int, input().strip().split(' '))
# a = list(map(int, input().strip().split(' ')))
# answer = array_left_rotation(a, n, k)
# print(*answer, sep=' ')