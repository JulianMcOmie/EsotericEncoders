def input_data():
	gender_dict = {"male": "His",
			"female": "Her"}
	subject_gender_dict = {"male": "he",
				"female": "she"}
	verb_flag_list = ["kink is ", "kinks are "]

	date = input("Date (press s to skip, type 'default' to use a pre-set date): ")
	if date.lower()=="default":
		date="It is July 16, 2019, 04:32:06 PM. "

	name = input("\nName: ")
	if name=="s":
		name = "Gareth"

	gender = input("\nGender (male or female): ")
	if gender=="s":
		gender="male"

	kinks = input("\nKinks: ")
	if kinks=="s":
		kinks="ChewToy"

	kinkFlag = 0
	if kinks.count(", ", 0, len(kinks)) > 1:
		kinkFlag = 1

	which_kink = input("\nWhich kink do you choose? ")
	if which_kink=="s":
		which_kink="ChewToy"

	first_paragraph = date + name + " is in " + gender_dict[gender].lower() + " bed, bored. " + gender_dict[gender] + " secret " + verb_flag_list[kinkFlag] + kinks + ". Suddenly " + subject_gender_dict[gender] + " spots " + which_kink + ". Then the following sounds become audible."

	return first_paragraph

def text_to_puberty():
	first_paragraph = input_data()
	text = input("Text: ")
	f = open("outputFiles/puberty.fap", "w+")
	f.write(first_paragraph + "\n\n")
	for letter in text:
		f.write("ugh ")
		for i in range(ord(letter)):
			f.write("fap ")
		f.write("yes yeah ")
	f.write("\n\nOMGMOMGETOUTTAHERE\n")

