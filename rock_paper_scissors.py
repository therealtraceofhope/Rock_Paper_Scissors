import random


print("THANK YOU FOR PLAYING OUR ROCK PAPER SCISSORS GAME")
print("YOUR CHOICES ARE AS FOLLOWS - ")
rock_selection = """
ROCK:
      _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)"""


paper_selection = """
PAPER:                         
      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)"""


scissors_selection = """
SCISSORS:
      _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)"""

choice = input(f"Make your choice! Rock, Paper or Scizzors\n").capitalize

if choice == "ROCK":
    user_selection = rock_selection
elif choice == "PAPER":
    user_selection = paper_selection
else:
    user_selection = scissors_selection
print(f"User Selection: {user_selection}")

game_options = [rock_selection, paper_selection, scissors_selection]
computer_selection = random.choice(game_options)
print(f"Computer Selection: {computer_selection}")

match_result = ""
if computer_selection == rock_selection and user_selection == rock_selection:
    match_result = "MATCH RESULT: TIE"
elif computer_selection == rock_selection and user_selection == paper_selection:
    match_result = "MATCH RESULT: USER WINS!"
elif computer_selection == rock_selection and user_selection == scissors_selection:
    match_result = "MATCH RESULT: COMPUTER WINS!"
elif computer_selection == scissors_selection and user_selection == rock_selection:
    match_result = "MATCH RESULT: USER WINS!"
elif computer_selection == scissors_selection and user_selection == scissors_selection:
    match_result = "MATCH RESULT: TIE"
elif computer_selection == scissors_selection and user_selection == paper_selection:
    match_result = "MATCH RESULT: COMPUTER WINS!"
elif computer_selection == paper_selection and user_selection == rock_selection:
    match_result = "MATCH RESULT: COMPUTER WINS!"
elif computer_selection == paper_selection and user_selection == paper_selection:
    match_result = "MATCH RESULT: TIE"
elif computer_selection == paper_selection and user_selection == scissors_selection:
    match_result = "MATCH RESULT: USER WINS!"

print(match_result)



