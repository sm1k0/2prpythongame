import csv
import time
import json
import unittest
from io import StringIO
from unittest.mock import patch


class TestGame(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()

    def tearDown(self):
        self.output.close()

    def test_print_centered(self):
        expected_output = "Hello World!\n"
        with patch('sys.stdout', new=self.output):
            print_centered("Hello World!")
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_intro(self):
        expected_output = "\n╔╗─╔╦═══╦╗──╔╗──╔═══╗╔╗\n║║─║║╔══╣║──║║──║╔═╗║║║\n║╚═╝║╚══╣║──║║──║║─║║║║\n║╔═╗║╔══╣║─╔╣║─╔╣║─║║╚╝\n║║─║║╚══╣╚═╝║╚═╝║╚═╝║╔╗\n╚╝─╚╩═══╩═══╩═══╩═══╝╚╝\n\n"
        with patch('sys.stdout', new=self.output):
            intro()
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_choose_start(self):
        with patch('builtins.input', return_value='да') as mock_input:
            with patch('sys.stdout', new=self.output):
                choose_start()
        self.assertEqual(mock_input.call_count, 1)
        self.assertIn("Хотите начать игру? (да/нет): ", self.output.getvalue())
def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def save_game_to_json(chapter_number, chapter_data):
    user_input = input("Введите данные для сохранения в формате JSON: ")
    data = {"chapter": chapter_number, "data": chapter_data, "user_input": user_input}
    save_to_json(data, "save.json")

def load_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

def load_game_from_json():
    filename = input("Введите имя файла для загрузки сохраненной игры: ")
    try:
        data = load_from_json(filename)
        chapter_number = data["chapter"]
        chapter_data = data["data"]
        user_input = data["user_input"]
        print(f"Загружена глава {chapter_number}")
    except FileNotFoundError:
        print("Файл не найден.")

# Функция для сохранения в CSV
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['chapter', 'data']  # Наименования колонок
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for chapter, chapter_data in data.items():
            writer.writerow({'chapter': chapter, 'data': chapter_data})

def save_game_to_csv(chapter_number, chapter_data):
    # Сохраняем текущую главу в CSV-файл
    data = {chapter_number: chapter_data}
    save_to_csv(data, 'save.csv')

def load_from_csv(filename):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = {row['chapter']: row['data'] for row in reader}
        return data

def load_game_from_csv():
    try:
        data = load_from_csv('save.csv')
    except FileNotFoundError:
        print("Файл сохранения не найден.")

def print_centered(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def write_to_csv(data):
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([data])
        for row in data:
            writer.writerow(row)
def intro():
    print_centered(f"╔╗─╔╦═══╦╗──╔╗──╔═══╗╔╗")
    print_centered(f"║║─║║╔══╣║──║║──║╔═╗║║║")
    print_centered(f"║╚═╝║╚══╣║──║║──║║─║║║║")
    print_centered(f"║╔═╗║╔══╣║─╔╣║─╔╣║─║║╚╝")
    print_centered(f"║║─║║╚══╣╚═╝║╚═╝║╚═╝║╔╗")
    print_centered(f"╚╝─╚╩═══╩═══╩═══╩═══╝╚╝")
    time.sleep(2)
    print("\n")
    print_centered("Вы играете за Джонни Вайсити.")
    print_centered("Вас вызывают по срочному делу в отделение.")
    print_centered("С вами прибывает ваш напарник Алекс Путан.")
    print_centered("Вам дают очень странное дело.")
    time.sleep(2)


def print_title(title):
    print_centered(f"\n{title}\n")


def choose_start():
    choice = input("Хотите начать игру? (да/нет): ")
    if choice.lower() == "да":
        case()
    elif choice.lower() == "нет":
        print_centered("Дело отдано другому.")
    else:
        print_centered("Некорректный выбор.")


def case():
    print_centered("Дело в том, что появился новый маньяк 'Грешник'.")
    print_centered("Он уже убил более 10 человек.")
    print_centered("Он выбирает жертву по 7 смертным грехам:")
    sins = {
        1: "Похоть",
        2: "Чревоугодие",
        3: "Жадность",
        4: "Лень",
        5: "Гнев",
        6: "Зависть",
        7: "Гордыня"
    }
    for num, sin in sins.items():
        print(f"{num}. {sin}")
    choice = input("Хотите взяться за дело? (да/нет): ")
    if choice.lower() == "да":
        pass
    elif choice.lower() == "нет":
        print_centered("Дело отдано другому.")
    else:
        print_centered("Некорректный выбор.")


def choose_action(text, options):
    print(text)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    choice = input("Выберите действие: ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        choice = input("Выберите действие: ")
    return int(choice)


# Функция для главы 1
def chapter1():
    print_title("Глава 1: В поисках Грешника")
    choice = choose_action("Вас вызывают на срочное дело в полицейское отделение. Взяться за дело?", ["Да", "Нет"])
    if choice == 1:
        print_centered("Вы отправляетесь на место преступления.")
        choice = choose_action("Осмотреть тело или осмотреть местность?", ["Осмотреть тело", "Осмотреть местность"])
        if choice == 1:
            print_centered("Вы замечаете, что это не сам Грешник, а подражатель.")
            print_centered("Основываясь на порезах и ранах, вы делаете выводы о преступлениях, совершенных в порыве эмоций.")
            print_centered("Алекс подтверждает ваши догадки.")
            choice = choose_action('хотите осмотреть местность: ', ["Да", "Нет"])
            if choice == 1:
                print_centered("Вы находите следы обуви размера 43 и немного песка на месте трупа.")
                print_centered("Ваши мысли смешиваются, так как вы лично отправили Уильяма Бейкера за решетку.")
        else:
            print_centered("Вы находите следы обуви размера 43 и немного песка на месте трупа.")
            print_centered("Ваши мысли смешиваются, так как вы лично отправили Уильяма Бейкера за решетку.")
            choice = choose_action('хотите осмотреть труп: ', ["Да", "Нет"])
            if choice == 1:
                print_centered("Вы замечаете, что это не сам Грешник, а подражатель.")
                print_centered("Основываясь на порезах и ранах, вы делаете выводы о преступлениях, совершенных в порыве эмоций.")
                print_centered("Алекс подтверждает ваши догадки.")
            else:
                pass
            print_centered("Вы решаете отправиться в полицейский участок.")
    else:
        print_centered("Дело отдают другой команде. Игра заканчивается.")
    choice = input("Желаете сохранить игру? (да/нет): ")
    if choice.lower() == "да":
        save_game_to_json(1, "данные главы 1")
        save_game_to_csv(1, "данные главы 1")

# Функция для главы 2
def chapter2():
    print_title("Глава 2: Поиски Уильяма Бейкера")
    print_centered("Джонни приехал домой и обдумывает произошедшее.")
    choice = choose_action("Куда дальше поехать: Домой или к Алексу?", ["Домой", "К Алексу"])
    if choice == 1:
        print_centered("Джонни уходит домой и продолжает думать.")
        print_centered("Во сне ему снится странный сон, в котором Грешник преследует его в пустыне с лицом Алекса.")
        choice1 = choose_action("Поехать к Алексу?", ["Да", "Нет"])
        if choice1 == 1:
            print_centered("Вы приезжаете к Алексу и начинаете разговор.")
            print_centered("Алекс говорит про некого Альберта...")
            print_centered("Алекс уходит домой, а Джонни смотрит на доску подозреваемых и замечает сходство одного из них с неким Альбертом.")
            choice = choose_action("Поехать к другу Альберта или нет?", ["Да", "Нет"])
            if choice == 1:
                print_centered("Вы решаете поехать к другу Альберта независимо от алиби.")
            else:
                print_centered("Джонни уходит домой и обдумывает произошедшее.")
                print_centered("Во сне ему снится странный сон, в котором Грешник преследует его в пустыне с лицом Алекса.")

    else:
        print_centered("Вы приезжаете к Алексу и начинаете разговор.")
        print_centered("Алекс говорит про некого Альберта...")
        print_centered("Алекс уходит домой, а Джонни смотрит на доску подозреваемых и замечает сходство одного из них с неким Альбертом.")
        choice = choose_action("Поехать к другу Альберта или нет?", ["Да", "Нет"])
        if choice == 1:
            print("Вы решаете поехать к другу Альберта независимо от алиби.")
        else:
            print("Джонни уходит домой и обдумывает произошедшее.")
            print("Во сне ему снится странный сон, в котором Грешник преследует его в пустыне с лицом Алекса.")
    choice = input("Желаете сохранить игру? (да/нет): ")
    if choice.lower() == "да":
        save_game_to_json(2, "данные главы 2")
        save_game_to_csv(2, "данные главы 2")


# Функция для главы 3
def chapter3():
    print_title("Глава 3: Встреча с другом Альберта")
    print_centered("Джонни приезжает к другу Альберта и задает ему вопрос про Уильяма.")
    print_centered("Друг отвечает вопросом на вопрос и замял тему.")
    print_centered("В ходе разговора вы обнаруживаете, что 43 размер обуви сильно распорот.")
    choice = choose_action("Задать Алексу вопрос или нет?", ["Да", "Нет"])
    if choice == 1:
        print_centered("Алекс отвечает, что он пытается понять, как мыслит Грешник и кто будет следующей жертвой.")
        print_centered("Вы замечаете, что каждый раз, когда появляется главный подозреваемый, его убивает Грешник.")
        print_centered("Вы понимаете, что Альберт - следующая цель.")
    print_centered("Вы отправляетесь в полицейский участок, чтобы узнать адрес его проживания.")
    choice = input("Желаете сохранить игру? (да/нет): ")
    if choice.lower() == "да":
        save_game_to_json(3, "данные главы 3")
        save_game_to_csv(3, "данные главы 3")


def chapter4():
    print_title("Глава 4: Разоблачение и финал")
    print_centered("Джонни и Алекс приезжают на место и обнаруживают мертвого Альберта и кучу песка.")
    print_centered("По всей видимости, это был Уильям.")
    print_centered("Выясняется, что Альберт - судья, принимающий взятки.")
    print_centered("При осмотре местности Джонни обнаруживает ткань, похожую на ту, которую носит Алекс.")
    choice = choose_action("Спросить Алекса или предложить поехать в участок?",
                           ["Спросить Алекса", "Поехать в участок"])
    if choice == 1:
        print_centered("Алекс понимает, что Джонни догадался, и убивает его.")
        print_centered("Игра заканчивается.")
    else:
        print_centered("Джонни и Алекс скрывно сдают ткань на анализ.")
        print_centered("Анализ показывает, что это ткань Алекса.")
        print_centered("Джонни спрашивает у Алекса, что он хотел от этого.")
        print_centered("Алекс в злости отвечает, что ему надоело быть в тени Джонни.")
        print_centered("Джонни расстроен, что лишился своего напарника.")
        print_centered("Вы решаете либо закрыть дело и дать Уильяму шанс, либо незамедлительно звонить в полицию.")
        choice = choose_action("Закрыть дело или звонить в полицию?", ["Закрыть дело", "Звонить в полицию"])
        if choice == 1:
            print_centered("Уильям признается, что он решил сам навестить Джонни по старой дружбе.")
            print_centered("Он говорит, что ему не нравится быть пешкой и выполнять грязную работу.")
            print_centered("Он предлагает закрыть его дело взамен на небольшую информацию, которая поможет.")
            print_centered("Вы соглашаетесь и Уильям говорит, что разгадка под носом и кусок ткани докажут это.")
            print_centered("Игра заканчивается.")
        else:
            print_centered("Вы незамедлительно звоните в полицию.")
            print_centered("Уильям уже не сопротивляется и задерживается.")
            print_centered("Алекс также задерживается.")
            print_centered("Джонни расстроен, но чувствует облегчение, что правосудие восторжествовало.")
            print_centered("Игра заканчивается.")

    choice = input("Желаете сохранить игру? (да/нет): ")
    if choice.lower() == "да":
        save_game_to_json(4, "данные главы 4")
        save_game_to_csv(4, "данные главы 4")
# Основной игровой цикл
def main():
    intro()
    choice = input("Хотите начать новую игру или загрузить сохраненную? (новая/загрузить): ")
    if choice.lower() == "новая":
        case()
        chapter1()
        chapter2()
        chapter3()
        chapter4()
    elif choice.lower() == "загрузить":
        choice = input("Как вы хотите загрузить сохраненную игру? (json/csv): ")
        if choice.lower() == "json":
            load_game_from_json()
        elif choice.lower() == "csv":
            load_game_from_csv()
        else:
            print("Некорректный выбор формата.")
    else:
        print("Некорректный выбор.")

    choice = input("Хотите сохранить игру перед выходом? (да/нет): ")
    if choice.lower() == "да":
        save_game_to_json(5, "финальные данные")
        save_game_to_csv(5, "финальные данные")

# Запуск игры
if __name__ == "__main__":
    main()
