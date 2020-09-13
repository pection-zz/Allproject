import random
import string
data= dict()
listname=list()
lowerLetters=string.ascii_lowercase
print(" please enter passcode ")
name = input()
lowercase_letters = [c for c in name if c.islower()]
# print (lowercase_letters)
# print (name)
# print (listname[:10])
if lowercase_letters != [] :

	passcode=' '.join(lowercase_letters[:10])
	data[passcode] = random.randrange(10,99)
	print ("Yourpasscode is " ,data)
else :
	for i in range (0,10):
		data = ' '.join(random.choice(lowerLetters) for j in range (0,10))
	print (" Yourpasscode is", data)


