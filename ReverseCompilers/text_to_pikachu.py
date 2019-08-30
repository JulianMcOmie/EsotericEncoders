import random

data = ["pi", "pika", "pikachu"]
def text_to_pikachu():
	f = open("outputFiles/pikachu.txt", "w+")
	text = input("Text: ")
	preNumber = 3
	for index in range(len(text)):
		letter = text[index]
		for i in range(ord(letter)):
			current = random.randint(0,2)
			while current == preNumber:
				current = random.randint(0,2)
			f.write(data[current] + " ")
			preNumber = current
		f.write("pi pikachu\npikachu pikachu pi pikachu")
		if index <= len(text)-2:
			f.write("\n")
