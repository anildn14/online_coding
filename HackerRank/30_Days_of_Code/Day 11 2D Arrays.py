arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
# print arr
# print ("\n *******************************")
sum_arr=[]
# def calc_sum():
# print arr[0][0]+arr[0][1]+arr[0][2]+arr[1][1]+arr[2][0]+arr[2][1]+arr[2][2]
for n in range(4):
    for m in range(4):
        sum=arr[n][m]+arr[n][m+1]+arr[n][m+2]+arr[n+1][m+1]+arr[n+2][m]+arr[n+2][m+1]+arr[n+2][m+2]
        sum_arr.append(sum)
# print sum_arr
print max(sum_arr)
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6

# for arr_i in xrange(6):
#     print arr_i
# for arr_i in range(6):
#     print arr_i