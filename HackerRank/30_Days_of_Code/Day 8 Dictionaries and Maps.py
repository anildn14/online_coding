n=int(raw_input("Enter no.of enteries : "))
phoneBook={}
for i in range(n):
    # raw_input("Enter name and phone number with a spcae between them:")
    a=raw_input("Enter name and phone number with a spcae between them:").split(' ')
    phoneBook[a[0]]=a[1]
    print a
    print a[0]
# print phoneBook

query=raw_input()
print phoneBook.get(query)
if query in phoneBook.keys():
    print query+"="+phoneBook.get(query)
else:
    print "Not Found"