import random

responses = {
    "привіт": ["Привіт!", "Здоровенькі були", "Шановний, вітаю"], 
    "як справи?": ["У мене все гаразд, дякую", "Справи чудові!", "Немає скарг :)"],
    "що вмієш робити?": ["Я простий чат-бот для спілкування", "Вмію відповідати на прості запитання", "Мої можливості на разі обмежені"]
}

def get_response(user_input):
    user_input = user_input.lower()
    bot_response = "Вибачте, не зрозумів це повідомлення. Спробуйте уточнити запитання."
    if user_input in responses:
        bot_response = random.choice(responses[user_input])
        
    return bot_response


print("Привіт! Я простий чат-бот. Почнімо розмову!")
while True:
    user_input = input("Ви: ")
    print("Бот:", get_response(user_input))