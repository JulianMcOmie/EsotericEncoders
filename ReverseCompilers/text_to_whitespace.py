def text_to_whitespace(text):
	f = open("whitespace.txt", "w+")
	f.write("   ")
	for letter in text:
		f.write("  ") #Begin with the stack manipulation Instruction Modification Parameter, then start with the binary number of which to push to the stack
		for binary_character in str(bin(ord(letter))):
			if binary_character == "0":
				f.write(" ") #write a space
			elif binary_character == "1":
				f.write("\t") #write a tab
		f.write("\n") #signify the end of the binary number
		f.write("\t\n  ") #Go to the Input/Output Instruction Modification Parameter, then simply output the character at the top of the stack
	f.write("\n"*3) #end of program

text_to_whitespace("""Wow, you've really done it. Wait hmm what? whaaat? whaaaaaaat??? shut up with that crap okay? good. Now. what you need to find is under the red fence, remember that and the rest is history. 45°36'51.5"N 122°23'55.2"W. And yes, they are what you think. Good day, lad, and may Harold forever rest in piece. unless....""")
