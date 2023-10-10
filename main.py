import random

def choose_spell(spells):
    return random.choice(spells)

spell_book = ["Огненный шар", "Ледяная стрела", "Молниеносный удар", "Теневой клинок"]

characters = {
    "Юкио": {"способность": "Управление огнем", "защита": 100, "удар": 100},
    "Мария": {"способность": "Контроль над водой", "защита": 100, "удар": 100},
    "Кейт": {"способность": "Манипуляция электричеством", "защита": 100, "удар": 100},
    "Рю": {"способность": "Иллюзии и телепортация", "защита": 100, "удар": 100}
}


def show_character_info(character):
    print(f"Информация о персонаже {character}:")
    print(f"Способность: {characters[character]['способность']}")
    print(f"Защита: {characters[character]['защита']}")
    print(f"Удар: {characters[character]['удар']}")


def magical_battle():
    player_spell = choose_spell(spell_book)
    opponent_spell = choose_spell(spell_book)

    print(f"Ваш персонаж использует заклинание: {player_spell}")
    print(f"Противник использует заклинание: {opponent_spell}")

    if player_spell == opponent_spell:
        print("Ничья! Оба заклинания столкнулись и нейтрализовали друг друга.")
    elif (player_spell == "Огненный шар" and opponent_spell == "Ледяная стрела") or \
            (player_spell == "Ледяная стрела" and opponent_spell == "Молниеносный удар") or \
            (player_spell == "Молниеносный удар" and opponent_spell == "Теневой клинок") or \
            (player_spell == "Теневой клинок" and opponent_spell == "Огненный шар"):
        print("Вы победили! Ваше заклинание сильнее противника.")
    else:
        print("Вы проиграли! Заклинание противника оказалось сильнее.")


def choose_action():
    print("Выберите действие:")
    print("1. Поговорить с персонажем")
    print("2. Проверить место пропажи учеников")
    print("3. Исследовать темные коридоры")
    print("4. break")
    choice = input()
    return choice

def dialogue():
    dialogs = [
        "Привет! Как дела?",
        "Какой прекрасный день сегодня!",
        "У нас есть важная миссия, будь готов.",
        "Какую способность ты хочешь развить?",
        "Не забудь посетить библиотеку, там интересные книги!"
    ]
    random_dialog = random.choice(dialogs)
    print(random_dialog)


def explore_corridors():
    print("Вы исследуете темные коридоры...")
    chance = random.randint(1, 100)
    if chance <= 25:
        print("Вы нашли алмазы! Поздравляю!")
    else:
        print("В коридорах ничего нет.")


def main():
    print("Добро пожаловать в игру 'Битва магов: Заклинания судьбы'!")
    player_name = input("Введите имя своего персонажа: Юкио, Мария, Рю, Кейт ")
    print(
        f"{player_name}, вам предстоит познать мир магии и раскрыть загадку, скрывающуюся в Академии Белых Заклинаний.")
    print("Вы отправляетесь на обучение в школу и сталкиваетесь с первыми вызовами.")

    while True:
        print("\nГлавное меню:")
        print("1. Информация о персонаже")
        print("2. Магическая битва")
        print("3. Расследование и приключения")
        print("4. Выход из игры")
        choice = input("Выберите действие: ")

        if choice == "1":
            show_character_info(player_name)
        elif choice == "2":
            magical_battle()
        elif choice == "3":
            print("Вы начинаете расследование и приключения в Академии Белых Заклинаний.")
            while True:
                action_choice = choose_action()
                if action_choice == "1":
                    print("Вы решаете поговорить с одним из персонажей.")
                    dialogue()
                elif action_choice == "2":
                    print("Вы проверяете место пропажи учеников.")
                    # Здесь можно добавить расследование и поиск улик
                elif action_choice == "3":
                    print("Вы исследуете темные коридоры.")
                    explore_corridors()
                elif action_choice == "4":
                    break
                else:
                    print("Выбрано недопустимое действие. Попробуйте снова.")
        elif choice == "4":
            print("Спасибо за игру! До новых встреч!")
            break
        else:
            print("Выбрано недопустимое действие. Попробуйте снова.")


# Запуск игры
main()
