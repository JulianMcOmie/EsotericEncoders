from encoder import Encoder


class WhitespaceEncoder(Encoder):
    def encode(self, text):
        encoded_text = "   "  # Initial spaces for your whitespace code
        for letter in text:
            encoded_text += "  "  # Begin with the stack manipulation Instruction Modification Parameter
            # Start with the binary number of which to push to the stack
            for binary_character in str(bin(ord(letter)))[2:]:  # [2:] to skip the '0b' prefix of bin()
                if binary_character == "0":
                    encoded_text += " "  # write a space
                elif binary_character == "1":
                    encoded_text += "\t"  # write a tab
            encoded_text += "\n"  # signify the end of the binary number
            encoded_text += "\t\n  "  # Output the character at the top of the stack
        encoded_text += "\n"*3  # end of program
        return encoded_text

    @staticmethod
    def file_extension():
        return ".txt"
