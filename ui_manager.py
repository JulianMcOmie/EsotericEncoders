class UIManager:
    def __init__(self, language_manager):
        self.language_manager = language_manager

    def run(self):
        while True:
            print("\nChoose one of the following esoteric languages to use:")
            languages = self.language_manager.list_encoders()
            for idx, lang in enumerate(languages, 1):
                print(f"{idx}. {lang.capitalize()}")
            choice = input("\n--> ")
            encoder = self.language_manager.get_encoder(languages[int(choice) - 1])
            if encoder:
                text = input("Text to encode: ")
                encoded_text = encoder.encode(text)
                print("\nEncoded Text:\n", encoded_text)
            else:
                print("Invalid choice. Please try again.")
