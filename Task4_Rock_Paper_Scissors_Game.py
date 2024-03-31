import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
import random
def check_winner(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result=""
    if user_choice == computer_choice:
        result= "It's a tie!"
        result_label.config(text=f"Computer chose {computer_choice}. {result}")
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result= 'You win!'
        result_label.config(text=f"Computer chose {computer_choice}. {result}")
        return 'You win!'
    else:
        result= 'Computer wins!'
        result_label.config(text=f"Computer chose {computer_choice}. {result}")
        return 'Computer wins!'
    

def play_game(user_choice):
    global user_score, computer_score
    result = check_winner(user_choice)
    if result == 'You win!':
        user_score += 1
    elif result == 'Computer wins!':
        computer_score += 1
    score_label.config(text=f"User: {user_score} | Computer: {computer_score}")
    

def restart_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    computer_choice=""
    result=""
    result_label.config(text=f"{computer_choice}. {result}")
    score_label.config(text=f"User: {user_score} | Computer: {computer_score}")

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x250")
root.resizable(False,False)
root.configure(bg='#f0f0f0')

frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(pady=20)
result_label = tk.Label(root, text="", font=('Arial', 10))
result_label.pack()

rock_img = Image.open("rock.png").resize((100, 100))
paper_img = Image.open("paper.png").resize((100, 100))
scissors_img = Image.open("scissors.jpg").resize((100, 100))

rock_img_tk = ImageTk.PhotoImage(rock_img)
paper_img_tk = ImageTk.PhotoImage(paper_img)
scissors_img_tk = ImageTk.PhotoImage(scissors_img)

rock_button = tk.Button(frame, image=rock_img_tk, command=lambda: play_game("rock"))
rock_button.pack(side=LEFT)

paper_button = tk.Button(frame, image=paper_img_tk, command=lambda: play_game("paper"))
paper_button.pack(side=LEFT)

scissors_button = tk.Button(frame, image=scissors_img_tk,  command=lambda: play_game("scissors"))
scissors_button.pack(side=LEFT)

score_label = tk.Label(root, text=f"User: {user_score} | Computer: {computer_score}", font=('Arial', 12), bg='#f0f0f0')
score_label.pack()

restart_btn = tk.Button(root, text="Restart", font=('Arial', 12), bg='#ff9999', command=restart_game)
restart_btn.pack(pady=10)

root.mainloop()
