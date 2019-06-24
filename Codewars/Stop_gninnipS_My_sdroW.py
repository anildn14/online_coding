# Write a function that takes in a string of one or more words, and returns the same string, but with all five
# or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters
# and spaces. Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") =>
# returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"

# test.assert_equals(spin_words("Welcome"), "emocleW")



def spin_words1(sentence):
    l=[]
    for x in sentence.split():
        if len(x) >4:
            l.append(x[::-1])
        else:
            l.append(x)
    return ' '.join(X for X in l)

def spin_words2(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

def spin_words3(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())


print spin_words1("Welcome to the jungle")
print spin_words2("Welcome to the jungle")
print spin_words3("Welcome to the jungle")