def text_to_lolcode():
	text = input("Text: ")
	f = open("outputFiles/lolcode.lol", "w+")
	f.write("""HAI\nVISIBLE "{}"\nKTHXBYE""".format(text))
