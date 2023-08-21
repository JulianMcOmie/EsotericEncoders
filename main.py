from language_manager import LanguageManager
from ui_manager import UIManager


def main():
    language_manager = LanguageManager()
    ui_manager = UIManager(language_manager)
    ui_manager.run()


if __name__ == "__main__":
    main()
