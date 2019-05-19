class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def insert(self, head, data):
        # Complete this method
        new_node = data
        current = head
        print "new_node :",new_node
        print "current :",current
        # while current.data!=None:
        # while new_node!=None:
        while current!=None:
            current = current.next
            print "current :",current
            print "current.data :", current.data
            print "current.next :", current.next
        current.next = new_node
###########solution 1:
        if head is None:
            head = Node(data)
        else:
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
        return head
###########solution 1 end:
###########solution 2:
        # new_node = Node(data)
        # if (head == None):
        #     head = new_node
        # else:
        #     temp = head
        #     while (temp.next != None):
        #         temp = temp.next
        #     temp.next = new_node
        #
        # return head
###########solution 2 end:

mylist= Solution()
T=int(raw_input())
head=None
for i in range(T):
    data=int(raw_input())
    head=mylist.insert(head,data)
mylist.display(head);


