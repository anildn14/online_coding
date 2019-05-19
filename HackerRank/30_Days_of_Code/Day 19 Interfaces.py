# import java.io.*;
# import java.util.*;
#
# interface AdvancedArithmetic{
#    int divisorSum(int n);
# }
# class Calculator implements AdvancedArithmetic {
#     public int divisorSum(int n) {
#         int sum = n;
#         for (int i = 1; i <= n/2; i++) {
#             if (n % i == 0)
#                 sum += i;
#         }
#         return sum;
#     }
# }
#
# class Solution {
#
# public static void main(String[] args) {
# Scanner scan = new Scanner(System.in );
# int n = scan.nextInt();
# scan.close();
#
# AdvancedArithmetic myCalculator = new Calculator();
# int sum = myCalculator.divisorSum(n);
# System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
# System.out.println(sum);
# }
# }

divisible_list=[]
user_input=int(raw_input("Enter the number :"))
print "user_input :",user_input
for i in range (1,user_input+1):
    # print i
    if user_input%i==0:
        divisible_list.append(i)
print "divisible_list :",divisible_list
print "sum(divisible_list) :", sum(divisible_list)
