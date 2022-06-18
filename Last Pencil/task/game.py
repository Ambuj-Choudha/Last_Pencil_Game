import random


# checks the input for no. of pencils and returns bool
def pencil_check(value):
    for i in value:
        if i not in "0123456789":
            print("The number of pencils should be numeric\n")
            return False
    if value == "0":
        print("The number of pencils should be positive\n")
        return False
    return True


# checks if the correct first player name is entered
def name_check(n1, n2, text):
    if text == n1 or text == n2:
        return True
    else:
        print("Choose between {} and {}".format(repr(n1), repr(n2)))
        return False


# checks if the turn is legal or not i.e. 1, 2, or 3
def turn_check(x):
    possible = ["1", "2", "3"]
    if x not in possible:
        print("Possible values: '1', '2' or '3'\n")
        y = input()
        new_take = turn_check(y)
    else:
        return x
    return new_take  # 2nd return statement if the turn is right on the first attempt, else statement would get skipped


# removes the pencil and also checks if it's possible or not
def remove_pencil(total2, _take):
    old_value = total2  # because if total2 < 0 we want the old value back, we don't modify total2
    total2 -= _take
    if total2 > 0:
        print("|" * total2)
    elif total2 < 0:
        print("Too many pencils were taken\n")
        z = input()
        total2 = remove_pencil(old_value, int(turn_check(z)))
    return total2


# one single function to call all the functions to play a move
def play_turn(_player, total1):
    take = input(f"{_player}'s turn!\n")
    take = turn_check(take)
    take = int(take)
    new_total = remove_pencil(total1, take)
    return new_total


# function to execute the bots move
def bot_turn(_bot, total):
    print(f"{_bot}'s turn!\n")
    r = total % 4
    pick = 0
    if r != 1:      # any position where pencils are of the form 4n + 1 then its losing
        if r == 0:
            pick = 3
        else:
            pick = r - 1
    else:               # play randomly if losing
        if total != 1:
            pick = random.randint(1, 3)
        else:          # if only one pencil left then, pick 1
            pick = 1

    total = total - pick
    print(pick)
    print(total * "|")
    return total


# function to simplify things in the while loop (not used though)
def play_game(_player_, _pencils_):
    if player == bot:
        _pencils_ = bot_turn(player, _pencils_)
    else:
        _pencils_ = play_turn(player, _pencils_)
    if _pencils_ == 0:
        return _pencils_


#  MAIN PROGRAM STARTS ####################################################################

name1 = "John"  # given names of the players
name2 = "Jack"
bot = name2

pencil_flag = False  # here we ask for the no. of pencils
pencils = input("How many pencils would you like to use:\n")

while not pencil_flag:  # loop for checking the input for no. of pencils until appropriate value is received
    flag = pencil_check(pencils)
    if not flag:
        pencils = input()
    else:
        pencils = int(pencils)
        break

name_flag = False
first = input(f"Who will be the first ({name1}, {name2})\n")

while not name_flag:  # loop for checking the input for name until appropriate value is received
    name_flag = name_check(name1, name2, first)
    if not name_flag:
        first = input()
    else:
        break

# assigning the first and second player
if first == name1:
    second = name2
else:
    second = name1

# game starts after no. of pencil and 'first' player is entered -- pencils displayed on screen
print("|" * pencils)

while pencils > 0:  # loop until the game doesn't get over
    player = first
    if player == bot:
        pencils = bot_turn(player, pencils)
    else:
        pencils = play_turn(player, pencils)
    if pencils == 0:
        print("{} won!".format(second))
        break

    player = second
    if player == bot:
        pencils = bot_turn(player, pencils)
    else:
        pencils = play_turn(player, pencils)
    if pencils == 0:
        print("{} won!".format(first))
        break
