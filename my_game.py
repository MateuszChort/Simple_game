'''
In this game there will be 5 rounds.
You have to collect points for final battle during 5 rounds. Boss has 10 points.
Five rounds:

1) question. There will be 3 questions. You can choose a question for 1p, 3p or 5p.
2) reward. You found a chest. The chest can have 1,3 or 5 points.
3) You meet an opponent and you have to play rock-paper-scissor game with him
4) Guess the number beetween 1 and 10. If you manage to do it in 1-2 moves, you get 3p, in 3-4moves you get 2p, in 5-6moves 1p.
5) Final battle. You play with a final boss. You have such many points, which you have already collected. Boss has 10p and you have to defeat him.
'''
import random
from time import sleep


points = 0

print("Hello in my game. There will be 5 rounds.")
sleep(1)
print("FIRST ROUND")
print("During first round you have to choose a question. You can choose easy one for 1 point. Middle difficult for 3p or very difficult for 5p.")
sleep(2)

while True:
    choice_of_question = int(input(
    'What question do you choose? Type 1 for 1p, type 3 for 3p, type 5 for 5p: '))
    if choice_of_question == 1:
        question1p = print("""
        Python language was invented by Guido van Rossum in 1991. Why did he call this language 'Python':
        a = Because he liked snakes.
        b = Because he was a fan of Monty Python’s Flying Circus.
        c = Because it is very difficult to learn.
        d = No one knows that.""")

        answer1p = input("Your answer (write a,b,c or d): ").lower()
        if answer1p == 'b':
            points += 1
            print("Congratulations. This is correct answer. You get 1 point. ")
        else:
            print("Unfortunately, this is not a correct answer. Correct is b.")

        print(f"Currently you have {points} points.")
        break
    elif choice_of_question == 3:
        question3p = print("""
        How many stars are in US flag?
        a = 52 stars
        b = 51 stars
        c = 50 stars
        d = 49 stars""")

        answer3p = input("Your answer (write a,b,c or d): ").lower()
        if answer3p == 'c':
            points += 3
            print("Congratulations. This is correct answer. You get 3 points. 50 stars on US flag means that there are 50 states of America.")
        else:
            print("Unfortunately, this is not a correct answer. Correct is c. 50 stars on US flag means that there are 50 states of America.")

        print(f"Currently you have {points} points.")
        break
    elif choice_of_question == 5:
        question5p = print("""
        What kind of animal is it that walks on four legs in the morning, two at noon, and three in the evening?
        a = cat
        b = human
        c = sphinx
        d = there is no such an animal""")

        answer5p = input("Your answer (write a,b,c or d): ").lower()
        if answer5p == 'b':
            points += 5
            print(
                "Congratulations. This is correct answer. You get 5 points. You have clearly read Edyp myth.")
        else:
            print("Unfortunately, this is not a correct answer. Correct is b. You clearly have not read Edyp myth.")
            print('day is the life of a HUMAN who crawls in childhood, walks on two legs as an adult, and in his old age often uses the third leg, i.e. a cane')
            print(f"Currently you have {points} points.")
        break
    else:
        print('You have to write 1 or 3 or 5')
        continue
sleep(2)
print("SECOND ROUND")
sleep(1)
print("""In the second round you find a box with 4 chests.
You can choose only one chest.
In one chest there is 0 points for you (probability 20%).
In second one there is 3 points (probability 40%).
In third one 5 points (probability 30%)
In fourth one there is -2 points (probability 10%)
You also can not to choose and go further with 0 points.
Let's check out how lucky you are...""")
sleep(5)
while True:
    choose_yes_or_no = input("Do you want to risk and choose a chest? (y/n): ")
    if choose_yes_or_no == 'y':
        chest_dict = {
            'chest_0p': 0.2,
            'chest_3p': 0.4,
            'chest_5p': 0.3,
            'chest_minus1p': 0.1
        }
        chest_list = tuple(chest_dict.keys())
        chest_probability = tuple(chest_dict.values())
        choice_chest = random.choices(chest_list, chest_probability)

        if choice_chest == ['chest_0p']:
            print('You picked a chest with 0p')
            points += 0
        elif choice_chest == ['chest_3p']:
            print('You picked a chest with 3p')
            points += 3
        elif choice_chest == ['chest_5p']:
            print('You picked a chest with 5p')
            points += 5
        elif choice_chest == ['chest_minus1p']:
            print('Unfortunately, you picked a chest with -2p')
            points -= 2
        break
    elif choose_yes_or_no == 'n':
        points += 0
        print(
            f'Fine, you have chosen not to pick and you still has {points} points.')
        break
    else:
        print("You have to type 'y' or 'n'.")    
        continue

print(f"After second round you have {points} points.")
sleep(2)
print('THIRD ROUND')
sleep(1)
print("""In the third round you have to play a game: Rock, paper, scissors. 
There will be 3 rounds... 
When you win the round, you score 3 points. 
When it's a draw, you get 0 points.
When you loose, we substract you 1 point.""")

i = 0
points_in_3_r = 0


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


while i < 3:
    while True:
        user = input(
            "What is your choice?: 'r' for rock,'p' for paper, 's' for scissors: ")
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            print("It's a tie, 0 points for you")
            break
        elif is_win(user, computer):
            print('You won and got 3 point')
            points += 3
            points_in_3_r += 3
            break
        
        elif is_win(computer, user):
            print('You lost, -1 point for you')
            points -= 1
            points_in_3_r -= 1
            break
        else:
            print("You have to type 'r' or 's' or 'p'")
            continue
    i += 1
print('You end the rock, paper, scissors with: ', points_in_3_r, 'point(s)')
print(f"After third round you have {points} points.")
sleep(2)
print('FOURTH ROUND')
sleep(1)
print("""In the fourth round you have to guess a number in a range 1-10. 
The number is randomly picked by a computer.
If you manage to do it in 1-2 moves -> you get 5 points, 
in 3-4 moves -> you get 3 points, 
in 5-6 moves -> 1 point.
more -> -3 points""")
sleep(5)

drawn_number = random.randint(1, 10)
for i in range(1, 10):
    answer = int(input("Type the number in range 1-10: "))
    if answer < drawn_number:
        print("Too little. Try again")
    elif answer > drawn_number:
        print("Too much. Try again")
    else:
        print("Congratulation, you guessed in", i, "time.")
        break

if i == 1 or i == 2:
    points += 3
    print('You receive 5 points.')
elif i == 3 or i == 4:
    points += 2
    print('You receive 3 points.')
elif i == 5 or i == 6:
    points += 1
    print('You receive 1 point.')
elif i > 6:
    points -= 3
    print('Sorry, but you have -3 points. There were too many tries.')

print(f"After fourth round you have {points} points.")
sleep(2)
print("Maximum points at this stage is 24 points.")
sleep(2)
print("Let's prepare at final round and final battle.")
print("At final battle you have to face a boss - a great warrior.")
sleep(2)
print(
    f"Your opponent has 10 points of life. You have such many points as you collected during 4 rounds on my-game ({points}).")
sleep(2)
print("""In this battle you can hit your opponent by either strong hit or fast hit:
 - Fast hit has 80% of probability and takes 1 point from the opponent.
 - Strong hit has 50% of probability and takes 3 points from the opponent.
Your opponent always hit and take you 1 point from your life.""")
sleep(4)
points_opp = 10
will_fast_hit_dict = {
    'hit': 0.8,
    'not_hit': 0.2
}

fast_hit_list = tuple(will_fast_hit_dict.keys())
fast_hit_probability = tuple(will_fast_hit_dict.values())


will_strong_hit_dict = {
    'hit': 0.5,
    'not_hit': 0.5
}

strong_hit_list = tuple(will_strong_hit_dict.keys())
strong_hit_probability = tuple(will_strong_hit_dict.values())


if random.randint(0, 1) == 0:
    warrior_attack = random.choices(fast_hit_list, fast_hit_probability)
else:
    warrior_attack = random.choices(strong_hit_list, strong_hit_probability)


i = 1

while points_opp > 0 and points > 0:
    your_attack = input('Do you want to hit fast or strong?: (f/s): ').lower()
    if your_attack == 'f' and random.choices(fast_hit_list, fast_hit_probability) == ['hit']:
        print("Nice. It's a hit. You take 1 point from the opponent")
        points_opp -= 1
    elif your_attack == 's' and random.choices(strong_hit_list, strong_hit_probability) == ['hit']:
        print("Nice. It's a hit. You take 3 points from the opponent")
        points_opp -= 3

    elif your_attack == 'f' and random.choices(fast_hit_list, fast_hit_probability) == ['not_hit']:
        print('Unfortunately, you did not hit')

    elif your_attack == 's' and random.choices(strong_hit_list, strong_hit_probability) == ['not_hit']:
        print('Unfortunately, you did not hit')

    else:
        print('Unfortunately, you did not hit')

    print(f'Your opponent has: {points_opp} points')
    points -= 1
    print(f'Warrior hits you by 1 point and you have: {points} points')

    i += 1

if points_opp <= 0:
    print('Congratultion, you won !')
else:
    print('Sorry, you lost. Maybe you collected too little points during the game.')

print('Thanks for participating.')
print('THE END')
