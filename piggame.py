import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("enter the number of players from (2-4):")
    if players.isdigit():
        players=int(players)
        if 2 <= players <=4 :
            print(f"the number of players is {players}")
            break
        else:
            print("must be between 2 and 4")
    else:
        print("invalid,try again")

max_score = 50
players_scores=[0 for i in range(players)]

while max(players_scores) < max_score:
    for players_idx in range(players):
        print("\nPlayer",players_idx+1,"turn has started")
        print("Your total score is:",players_scores[players_idx],"\n")
        current_score =0
        while True:
            should_roll = input("would you like to roll (y)?")
            if should_roll.lower() !="y":
                break
            value=roll()
            if value==1:
                print("you rolled 1 turn done")
                current_score = 0
                break
            else:
                current_score+=value
                print("you rolled a:",value)

            print("your score is:", current_score)
        players_scores[players_idx]+= current_score
        print("your total score is:",   players_scores[players_idx])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player", winning_idx+1 , "is the winner with the score of:",max_score)

print("adsdsadsa")
