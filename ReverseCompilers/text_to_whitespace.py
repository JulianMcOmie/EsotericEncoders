def text_to_whitespace(text):
    f = open("whitespace.txt", "w+")
    f.write("   ")
    for letter in text:
        f.write("  ")
        for binary_character in str(bin(ord(letter))):
            if binary_character == "0":
                f.write("s")
                f.write(" ") #write a space
            elif binary_character == "1":
                f.write("\t") #write a tab
                
        f.write("\n") #write a line feed
