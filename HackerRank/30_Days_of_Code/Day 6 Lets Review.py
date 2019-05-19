S="Hacker"
len(S)
# for i in range(0,len(S-1)):
#     print S[::2]
print S[::2]
print S[1::2]
S=raw_input("Enter a String")
odd=[]
even=[]
for i in range(len(S)):
    print i
    while i:
        if i==0:
            even.append(S[0])
        elif i%2==0:
            even.append(S[i])
        elif i%2!=0:
            odd.append(S[i])
print odd
print even

#Actual Answer
# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(raw_input("Enter a Name"))
for i in range(M):
    S=raw_input("")
    print S[::2]+" "+S[1::2]
