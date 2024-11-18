import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def translate(text):
    translator = Translator()

    try:
        return translator.translate(text, dest="ru").text
    except:
        return "Произошла ошибка"


# Создаём функцию, которая будет получать информацию
def get_word():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        word = translate(soup.find("div", id="random_word").text.strip())
        # Получаем описание слова
        word_definition = translate(soup.find("div", id="random_word_definition").text.strip())

        # Чтобы программа возвращала словарь
        return {
            "word": word,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_word()
        word = word_dict.get("word")
        word_definition = word_dict.get("word_definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? д/н ")
        if play_again != "д":
            print("Спасибо за игру!")
            break


word_game()
