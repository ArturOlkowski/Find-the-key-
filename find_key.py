from math import sqrt
from random import randint


GAME_WIDTH = 10
GAME_HEIGHT = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HEIGHT)

player_x = 0
player_y = 0

player_found_key = False

steps = 0

distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

# print(key_x, key_y) # information where is the key-

while not player_found_key:
    steps += 1
    print()
    print("You can move in a direction on your keyboard with [W|A|S|D]: ")

    move = input("Where are you going?: ")
    match move.lower():
        case "w":
            player_y += 1

            if player_y > GAME_HEIGHT:
                print("Au! you hit the wall..")
                player_y = GAME_HEIGHT

        case "s":
            player_y -= 1

            if player_y < 0:
                print("Au! you hit the wall..")
                player_y = 0

        case "a":
            player_x -= 1

            if player_x < 0:
                print("Au! you hit the wall..")
                player_x = 0

        case "d":
            player_x += 1
            
            if player_x > GAME_WIDTH:
                print("Au! you hit the wall..")
                player_x = GAME_WIDTH

        case "q":
            print("Game over!")
            quit()

        case "_":
            print("I don't know where are you going..")
            continue

    if player_x == key_x and player_y == key_y:
        print("Congratulations you found the key!")
        print(f"You need {steps} steps, to find the key")
        quit()

    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    # print("before",distance_before_move)  #information about where is my actiual position 
    # print("after", distance_after_move)   #information about where is my actiual position 

    if distance_before_move > distance_after_move:
        print("You are closer")
    else:
        print("You are geting further") 
    
    distance_before_move = distance_after_move

    print(player_x, player_y)
