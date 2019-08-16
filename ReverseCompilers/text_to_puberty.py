gender_dict = {"male": "his",
		"female": "her"}
subject_gender_dict = {"male": "he",
			"female": "she"}

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
which_kink = input("\nWhich kink do you choose? ")
if which_kink=="s":
	which_kink="ChewToy"

first_paragraph = date + name + " is in " + gender_dict[gender] + " bed, bored. " + gender_dict[gender] + " secret kinks are " + kinks + ".  Suddenly " + subject_gender_dict[gender] + " spots " + which_kink + ". Then the following sounds become audible"

input_text = input("\nText: ")


def text_to_fap(text):
	f = open("puberty.fap", "w+")
	f.write(first_paragraph + "\n\n")
	for letter in text:
		f.write("ugh ")
		for i in range(ord(letter)):
			f.write("fap ")
		f.write("yes yeah ")
	f.write("\n\nOMGMOMGETOUTTAHERE\n")

text_to_fap(input_text)
