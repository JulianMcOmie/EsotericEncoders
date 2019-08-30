import os

from ReverseCompilers.text_to_puberty import text_to_puberty
from ReverseCompilers.text_to_whitespace import text_to_whitespace
from ReverseCompilers.text_to_brainfuck import text_to_brainfuck
from ReverseCompilers.text_to_lolcode import text_to_lolcode
from ReverseCompilers.text_to_pikachu import text_to_pikachu

file_extensions = {"brainfuck": ".txt",
		   "puberty": ".fap",
		   "whitespace": ".txt",
		   "lolcode": ".lol",
		   "pikachu": ".txt"}

exec_list = []

name_count = 0
print("Choose one of the following esoteric languages to use:")
for filename in os.listdir("./ReverseCompilers"):
	if filename.startswith("text_to_"):
		name_count += 1
		function_filename = filename[:len(filename)-3]
		exec_list.append(function_filename + "()")
		print(str(name_count) + ": " + function_filename[8:].capitalize())

language_choice = input("\n--> ")
exec(exec_list[int(language_choice)-1])
language_name = exec_list[int(language_choice)-1][8:len(exec_list[int(language_choice)-1])-2]
print("File successfully created in outputFiles/{}".format(language_name + file_extensions[language_name]))
