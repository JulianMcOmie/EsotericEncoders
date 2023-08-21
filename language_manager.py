from encoders.brainfuck import BrainfuckEncoder
from encoders.whitespace import WhitespaceEncoder
from encoders.lolcode import LolcodeEncoder
from encoders.pikachu import PikachuEncoder
from encoders.puberty import PubertyEncoder


class LanguageManager:
    def __init__(self):
        self.encoders = {
            'brainfuck': BrainfuckEncoder(),
            'whitespace': WhitespaceEncoder(),
            'lolcode': LolcodeEncoder(),
            'pikachu': PikachuEncoder(),
            'puberty': PubertyEncoder(),
        }

    def get_encoder(self, name):
        return self.encoders.get(name, None)

    def list_encoders(self):
        return list(self.encoders.keys())
