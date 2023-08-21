class Encoder:
    def __init__(self):
        pass

    def encode(self, text):
        raise NotImplementedError("Each encoder must implement the encode method")

    @staticmethod
    def file_extension():
        raise NotImplementedError("Each encoder must provide its file extension")
