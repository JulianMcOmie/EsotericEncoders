class UIManager:
    @staticmethod
    def show_languages(languages):
        print("Choose one of the following esoteric languages to use:")
        for idx, lang in enumerate(languages, 1):
            print(f"{idx}: {lang.capitalize()}")

    @staticmethod
    def get_user_choice():
        return input("\n--> ")

    @staticmethod
    def show_output(language_name, extension):
        print(f"File successfully created in outputFiles/{language_name + extension}")
