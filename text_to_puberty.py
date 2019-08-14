def text_to_fap(text):
	f = open("fap.txt", "w+")
	for letter in text:
		f.write("ugh ")
		for i in range(ord(letter)):
			f.write("fap ")
		f.write("yes yeah ")
