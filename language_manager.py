class LanguageManager:
    supported_languages = {
        "brainfuck": (".bf", "text_to_brainfuck"),
        "puberty": (".fap", "text_to_puberty"),
        "whitespace": (".txt", "text_to_whitespace"),
        "lolcode": (".lol", "text_to_lolcode"),
        "pikachu": (".txt", "text_to_pikachu")
    }

    @staticmethod
    def get_languages():
        return list(LanguageManager.supported_languages.keys())

    @staticmethod
    def get_extension(language):
        return LanguageManager.supported_languages[language][0]

    @staticmethod
    def get_function(language):
        return LanguageManager.supported_languages[language][1]
