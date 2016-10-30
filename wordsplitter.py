
words = open('new.txt') #opens the pre existing text file


for word in words.read().split(): # the function that splits the words from the text file. 
	print word