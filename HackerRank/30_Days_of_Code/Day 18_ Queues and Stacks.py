import sys
class Solution:
    # Two instance variables: one for your stack, and one for your queue
    def __init__(self):
        self.stack = []
        self.queue = []

    # A char popCharacter() method that pops and returns the character at the top of the stack instance variable.
    def popCharacter(self):
        print "popCharacter"
        print "self.stack :", self.stack
        print "self.queue :", self.queue
        return self.stack.pop()

    # A void pushCharacter(char ch) method that pushes a character onto a stack.
    def pushCharacter(self, char):
        self.stack.append(char)
        print "pushCharacter"
        print "self.stack :",self.stack
        print "self.queue :", self.queue

    # A char dequeueCharacter() method that dequeues and returns the first character in queue the instance variable.
    def dequeueCharacter(self):
        print "dequeueCharacter"
        char = self.queue[0]
        print "char :",char
        self.queue = self.queue[1:]
        print "self.stack :", self.stack
        print "self.queue :", self.queue
        return char


    # A void enqueueCharacter(char ch) method that enqueues a character in the queue instance variable.
    def enqueueCharacter(self, char):
        self.queue.append(char)
        print "enqueueCharacter"
        print "self.stack :", self.stack
        print "self.queue :", self.queue

# read the string s
s = raw_input("Enter String : ")
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    print "i :",i
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
print "l/2 :",l/2
for i in range(l / 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write("The word, " + s + ", is a palindrome.")
else:
    sys.stdout.write("The word, " + s + ", is not a palindrome.")