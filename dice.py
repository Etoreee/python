import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Кубики кинуті...")
    print( "Випалооо....")
    print (random.randint(min, max))
    print (random.randint(min, max))

    roll_again = input("Кинути кубики ще раз? [yes/y]:")