from random import randint

start_day = 1
start_month = 1

score_print = "%s/%s"

winner = False

while (not winner):
    user_input = input("Change date or month - 1 for day, 2 for month: ")
    if (user_input == 1):
        