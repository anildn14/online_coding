# Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:
# choose a text in capital letters including or not digits and non alphabetic characters,
# shift each letter by a given number but the transformed letter must be a letter (circular shift),
# replace each digit by its complement to 9,
# keep such as non alphabetic and non digit characters,
# downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
# reverse the whole result.

# #Example:
# your text: "BORN IN 2015!", shift 1
# 1 + 2 + 3 -> "CPSO JO 7984!"
# 4 "CpSo jO 7984!"
# 5 "!4897 Oj oSpC"
# With longer passphrases it's better to have a small and easy program. Would you write it?

# test.assert_equals(play_pass("I LOVE YOU!!!", 1), "!!!vPz fWpM J")
# test.assert_equals(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2), 
#     "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")

strs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'      #use a string like this, instead of ord()
# print strs[(strs.index(i) + shift) % 26]
def play_pass(s, n):
	a=[]
	for i in s:
		if i.isdigit():
			a.append(str(9-int(i)))
		elif i.isalpha():
			y=strs[(strs.index(i) + n) % 26]
			print  "y :",y
			# a.append(chr((ord(i)+n) % 26))
			a.append(y)
		else:
			a.append(i)
	# print a
	for i in range(len(a)):
		# if i == 0 and a[i].isalpha():
		# 	a[i]=a[i].upper()
		# else:
		# if i%2==0 and a[i].isalpha():
		# 	a[i]=a[i].upper()
		# elif i%2!=0 and a[i].isalpha():
		# 	a[i]=a[i].lower()
		# print a.index(i)

		if i%2==0:a[i]=a[i].upper()
		else:a[i]=a[i].lower()

	return ''.join(x for x in a[::-1])
# print ord('a'),ord('A'),ord('z'),ord('Z')

print play_pass("I LOVE YOU!!!", 1)
print play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2)

