from .encoder import Encoder


class LolcodeEncoder(Encoder):
    def encode(self, text):
        encoded_text = "\n".join([
            "HAI",
            f'VISIBLE "{text}"',
            "KTHXBYE"
        ])
        return encoded_text

    @staticmethod
    def file_extension():
        return ".lol"
