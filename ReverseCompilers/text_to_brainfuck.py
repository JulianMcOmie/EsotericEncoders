def text_to_brainfuck():
	text = input("Text: ")
	f = open("outputFiles/brainfuck.txt", "w+")
	for letter in text:
		for i in range(ord(letter)):
			f.write("+")
		f.write(".")
		for i in range(ord(letter)):
			f.write("-")
