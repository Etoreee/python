import random
import time

options = ["камінь", "ножиці", "папір", "ящірка", "Спок"]
rules = {
    "камінь": ["ножиці", "ящірка"], 
    "ножиці": ["папір", "ящірка"],
    "папір": ["камінь", "Спок"],
    "ящірка": ["папір", "Спок"],
    "Спок": ["ножиці", "камінь"]
}

players = ["Гравець", "Бот 1", "Бот 2"]
player_scores = {p: 0 for p in players}

def print_header(round_num):
    print("\n" + "-" * 30)
    print(f"{'РАУНД ' + str(round_num):^30}")
    print("-" * 30)

def print_round_result(p1, p2): 
    print(f"\n{p1} вибрав {player_choice[p1]}")
    print(f"{p2} вибрав {player_choice[p2]}")

    if player_choice[p1] == player_choice[p2]:
        print("\nНічия! Переігровка...")
        return True

    if player_choice[p2] in rules[player_choice[p1]]:
        print(f"\n{p1} перемагає {p2} ({player_choice[p1]} виграває {player_choice[p2]})")
        player_scores[p1] += 1 
    else:
        print(f"\n{p2} перемагає {p1} ({player_choice[p2]} виграває {player_choice[p1]})")     
        player_scores[p2] += 1

    return False

def print_scores():
    print("\nТекущий рахунок:")
    for player, score in player_scores.items():
        print(f"{player}: {score}")

def print_menu():
    print("\nМеню:")
    print("1. Продовжити гру")
    print("2. Вийти з гри")

def get_user_choice():
    print("\nДоступні дії:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    print("\nПравила:")
    for option in options:
        beats = [o for o in options if o in rules[option]]
        print(f"{option} б'є: {', '.join(beats)}")

    while True:
        choice = input("Ваш вибір (введіть номер дії): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        else:
            print("Некоректний ввід. Спробуйте ще раз.")

def game():
    for round_num in range(1, 4):
        print_header(round_num)
        player_choice.clear()

        for p in players:
            if p == "Гравець":
                player_choice[p] = get_user_choice()
            else:
                player_choice[p] = random.choice(options)
                time.sleep(0.5)

        while print_round_result("Гравець", "Бот 1"):
            for p in players:
                if p == "Гравець":
                    player_choice[p] = get_user_choice()
                else:
                    player_choice[p] = random.choice(options)
                    time.sleep(0.5)

        print_round_result("Бот 1", "Бот 2")
        print_scores()

        if player_scores["Гравець"] == 2:
            print("\nВи перемогли у грі!")
            break

        print_menu()
        choice = input("Ваш вибір: ")
        if choice == "2":
            print("\nВи вийшли з гри.")
            break

    print("\nКінець гри!")

if __name__ == "__main__":
    player_choice = {}
    game()
