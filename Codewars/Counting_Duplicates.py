# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and
# numeric digits that occur more than once in the input string. The input string can be assumed to contain
# only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

# test.assert_equals(duplicate_count("abcde"), 0)
# test.assert_equals(duplicate_count("abcdea"), 1)
# test.assert_equals(duplicate_count("indivisibility"), 1)

from collections import Counter
def duplicate_count(text):
    print text
    a={}
    for x in text:
    	if x in a:
    		a[x]+=1
    	else:
    		a[x]=1
    print a
    
    z=Counter(text)
    print len(z)
    print z.values()

    # count = sum(1 for e in z.values() if e is not 1)
    count = sum(1 for e in Counter(text.lower()).values() if e is not 1)
    print count
    # print (lambda v: z.values()>0)#, z.values()))
    # print len(lambda v: z.values()>0)#, z.values()))


duplicate_count("abcd ABCD")



def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])