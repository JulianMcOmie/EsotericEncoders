from encoder import Encoder


class BrainfuckEncoder(Encoder):
    def encode(self, text):
        encoded_text = ""
        for letter in text:
            for _ in range(ord(letter)):
                encoded_text += "+"
            encoded_text += "."
            for _ in range(ord(letter)):
                encoded_text += "-"
        return encoded_text

    @staticmethod
    def file_extension():
        return ".bf"
