class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):

        if root==None:
            # print "Node(data) :",Node(data)
            return Node(data)
        else:
            # print "root.data :", root.data

            if data<=root.data:
                cur=self.insert(root.left,data)
                # print "cur :",cur
                root.left=cur
                # print "root.left :",root.left
            else:
                cur=self.insert(root.right,data)
                # print "cur :", cur
                root.right=cur
                # print "root.right :",root.right
        # print "root :",root
        #     print "root.data",root.data
        return root

    def getHeight(self, root):
        # Write your code here

        if root:
            # print "root :",root
            left = 0
            right = 0
            if root.left:
                # print "root.left :",self.getHeight(root.left)

                left = 1 + self.getHeight(root.left)
            print "left :",left
            if root.right:
                # print "root.right :",root.right
                right = 1 + self.getHeight(root.right)
            print "right :",right

            return max(left, right)
        else:
            return 0

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
    # print "data :",data
    # print "root :",root
print "##########################################################"
height=myTree.getHeight(root)
print height


# 73521467