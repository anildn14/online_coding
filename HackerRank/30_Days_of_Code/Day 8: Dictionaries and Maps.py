# n=int(raw_input("Enter n:"))
# phone={}
# for x in range(n):
#     a=raw_input("Enter name and number: ")
#     print a.split()[0]
#     print a.split()[1]
#     phone[a.split()[0]]=a.split()[1]
#     print phone
#     # print x.split()[0],x.split()[1]
#     # dict(x.split()[0])=x.split()[1]
# abc=raw_input("")
# for y in phone.keys():
#     print y+"="+phone.get(y)
# else:
#     "Not Found"

n=int(raw_input(""))
phone={}
for x in range(n):
    a=raw_input("")
    #print a.split()[0]
    #print a.split()[1]
    phone[a.split()[0]]=int(a.split()[1])
    #print phone
    # print x.split()[0],x.split()[1]
    # dict(x.split()[0])=x.split()[1]
for z in range(n):
    y=raw_input("")
    if y in phone.keys():
        print str(y)+"="+str(phone.get(y))
    else:
        print "Not found"

n=int(raw_input(""))
phone={}
for x in range(n):
    a=raw_input("").split(" ")
    phone[a[0]]=int(a[1])
for z in range(n):
    name=raw_input()
    if name in phone:
        phone1 = phone[name]
        print(name + "=" + str(phone1))
    else:
        print("Not found")
        
#actual answer

num = int(input())

phone_book = {}

for i in range(0, num):
    entry = str(raw_input()).split(" ")

    name = entry[0]
    phone = int(entry[1])
    phone_book[name] = phone

for j in range(0, num):
    name = str(raw_input())

    if name in phone_book:
        phone = phone_book[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")