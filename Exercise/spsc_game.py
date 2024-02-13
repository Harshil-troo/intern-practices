# import random
#
# def game():
#
#     choices = ["Stone","paper","Scissors"]
#
#     computer_choice = random.choice(choices)
#
#     user_choice = input("Enter your choice (Stone,Paper,Scissors): ")
#
#     print("Computer's choice: ", computer_choice)
#     print("Your choice: ", user_choice)
#
#     if computer_choice == user_choice:
#         print("It's a tie!!!")
#
#     elif (user_choice == "Stone" and computer_choice == "Scissors") or \
#          (user_choice == "Paper" and computer_choice == "Stone") or \
#          (user_choice == "Scissors" and computer_choice == "Paper") :
#         return "You Win!!"
#
#     else:
#         return "You Lose!!"
#
#
# print(game())


# def smartdiv(fx):
#     def ifx(a,b):
#         if a<b:
#             a,b = b,a
#         fx(a,b)
#     return ifx
#
# @smartdiv
# def div(a,b):
#     print(a/b)
#
#
# div(3,6)