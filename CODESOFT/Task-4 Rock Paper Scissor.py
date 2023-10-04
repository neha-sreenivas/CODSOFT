import tkinter as tk
import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "User"
    else:
        return "Computer"
def play_round():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    computer_choice_var.set(computer_choice)
    
    result = determine_winner(user_choice, computer_choice)
    result_var.set(f"Result: {result}")
    update_scores(result)
    
def update_scores(result):
    if result == "User":
        user_score_var.set(user_score_var.get() + 1)
    elif result == "Computer":
        computer_score_var.set(computer_score_var.get() + 1)

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")


label = tk.Label(window, text="Choose rock, paper, or scissors:")
label.pack()


user_choice_var = tk.StringVar()
user_choice_var.set("rock")
user_choice_rock = tk.Radiobutton(window, text="Rock", variable=user_choice_var, value="rock")
user_choice_paper = tk.Radiobutton(window, text="Paper", variable=user_choice_var, value="paper")
user_choice_scissors = tk.Radiobutton(window, text="Scissors", variable=user_choice_var, value="scissors")

user_choice_rock.pack()
user_choice_paper.pack()
user_choice_scissors.pack()

computer_choice_var = tk.StringVar()
computer_choice_var.set("")
computer_choice_label = tk.Label(window, textvariable=computer_choice_var)
computer_choice_label.pack()


play_button = tk.Button(window, text="Play", command=play_round)
play_button.pack()


result_var = tk.StringVar()
result_var.set("")
result_label = tk.Label(window, textvariable=result_var)
result_label.pack()


user_score_var = tk.IntVar()
user_score_var.set(0)
user_score_label = tk.Label(window, textvariable=user_score_var)
user_score_label.pack()

computer_score_var = tk.IntVar()
computer_score_var.set(0)
computer_score_label = tk.Label(window, textvariable=computer_score_var)
computer_score_label.pack()


window.mainloop()
