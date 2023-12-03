    
while (True):
    a = input("Введіть перше число: ")
    c = input("Введіть операцію: ")
    b = input("Введіть друге число: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Неправильно введено число...")
        
    
    if (c):
        if (c == "+"):
            print("Сума: ", a + b)
        elif (c == "-"):
            print("Різниця: ", a - b)
        elif (c == "*"):
            print("Результат: ", a * b)
        elif (c == "/"):
            print("Результат: ", a / b)
        else:
            print("Неправильна операція...")

    q = input("Закінчити розрахунки? [y/n] ")
    if (q == "y" or q == "Y"):
        break