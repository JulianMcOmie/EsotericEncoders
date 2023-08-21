import os
from language_manager import LanguageManager
from ui_manager import UIManager
from ReverseCompilers import *

def main():
    languages = LanguageManager.get_languages()
    UIManager.show_languages(languages)

    # Get user choice and validate it
    try:
        choice_idx = int(UIManager.get_user_choice()) - 1
        language_name = languages[choice_idx]
    except (ValueError, IndexError):
        print("Invalid choice!")
        return

    # Retrieve function name and execute
    function_name = LanguageManager.get_function(language_name)
    function_to_execute = globals()[function_name]
    function_to_execute()

    # Notify user about the output
    extension = LanguageManager.get_extension(language_name)
    UIManager.show_output(language_name, extension)

if __name__ == "__main__":
    main()
