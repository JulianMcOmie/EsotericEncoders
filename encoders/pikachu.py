import random
from .encoder import Encoder


class PikachuEncoder(Encoder):
    def encode(self, text):
        data = ["pi", "pika", "pikachu"]
        encoded_text = ""
        pre_number = 3
        for index, letter in enumerate(text):
            for _ in range(ord(letter)):
                current = random.randint(0, 2)
                while current == pre_number:
                    current = random.randint(0, 2)
                encoded_text += data[current] + " "
                pre_number = current
            encoded_text += "pi pikachu\npikachu pikachu pi pikachu"
            if index < len(text) - 1:
                encoded_text += "\n"
        return encoded_text

    @staticmethod
    def file_extension():
        return ".txt"
