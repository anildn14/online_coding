import math
from statistics import mean

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    def __init__(self, firstName, lastName, idNumber, scores):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
		self.scores = scores



    def calculate(self):
        print "self.scores :",self.scores
        print "len(self.scores):",len(self.scores)
        print "sum(self.scores) :",sum(self.scores)
        avg=sum(self.scores)/len(self.scores)
        # avg=mean(self.scores)
        print avg
        if 90 <= self.scores <= 100:
            return 'O'
        elif 80 <= self.scores < 90:
            return 'E'
        elif 70 <= self.scores < 80:
            return 'A'
        elif 55 <= self.scores < 70:
            return 'P'
        elif 40 <= self.scores < 55:
            return 'D'
        elif self.scores < 40:
            return 'T'
        print "self.scores :",self.scores

#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here
line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
# numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()



# Actual:

def calculate(self):
    avg = int(sum(self.scores) / len(self.scores))
    if 90 <= avg <= 100:
        return 'O'
    elif 80 <= avg < 90:
        return 'E'
    elif 70 <= avg < 80:
        return 'A'
    elif 55 <= avg < 70:
        return 'P'
    elif 40 <= avg < 55:
        return 'D'
    elif avg < 40:
        return 'T'
