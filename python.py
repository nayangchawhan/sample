import tkinter as tk
from tkinter import messagebox
import random

class DiceRollingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Rolling Game")
        self.balance = 1000
        self.min_bet = 10
        self.max_bet = 100
        self.roll_history = []

        # Balance label
        self.balance_label = tk.Label(master, text="Balance: $1000", font=("Arial", 12))
        self.balance_label.pack()

        # Bet type label
        self.bet_label = tk.Label(master, text="Enter your bet (1-6, even, or odd):", font=("Arial", 10))
        self.bet_label.pack()

        # Bet entry
        self.bet_entry = tk.Entry(master, font=("Arial", 10))
        self.bet_entry.pack()

        # Bet amount label
        self.amount_label = tk.Label(master, text="Enter bet amount:", font=("Arial", 10))
        self.amount_label.pack()

        # Bet amount entry
        self.amount_entry = tk.Entry(master, font=("Arial", 10))
        self.amount_entry.pack()

        # Roll button
        self.roll_button = tk.Button(master, text="Roll Dice", command=self.roll_dice, font=("Arial", 12))
        self.roll_button.pack()

        # Roll history label
        self.history_label = tk.Label(master, text="Roll History:", font=("Arial", 10))
        self.history_label.pack()

        # Roll history text
        self.history_text = tk.Text(master, height=5, width=40, font=("Arial", 10))
        self.history_text.pack()

        # Quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit, font=("Arial", 12))
        self.quit_button.pack()

    def roll_dice(self):
        bet_type = self.bet_entry.get().lower()
        bet_amount = int(self.amount_entry.get())

        if bet_type.isdigit() and int(bet_type) >= 1 and int(bet_type) <= 6:
            bet_type = int(bet_type)
        elif bet_type not in ['even', 'odd']:
            messagebox.showerror("Error", "Invalid bet type. Please enter a number between 1-6, 'even', or 'odd'.")
            return
        if bet_amount < self.min_bet or bet_amount > self.max_bet:
            messagebox.showerror("Error", "Invalid bet amount. Please enter a bet amount between $10 and $100.")
            return
        if bet_amount > self.balance:
            messagebox.showerror("Error", "Insufficient balance.")
            return

        dice_roll = random.randint(1, 6)
        self.roll_history.append(dice_roll)

        if (bet_type == 'even' and dice_roll % 2 == 0) or (bet_type == 'odd' and dice_roll % 2 != 0) or (bet_type == dice_roll):
            self.balance += bet_amount
            messagebox.showinfo("Result", f"Dice roll: {dice_roll}\nCongratulations, you win!")
        else:
            self.balance -= bet_amount
            messagebox.showinfo("Result", f"Dice roll: {dice_roll}\nSorry, you lose.")

        self.update_balance()
        self.update_roll_history()

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

    def update_roll_history(self):
        self.history_text.delete(1.0, tk.END)
        for roll in self.roll_history:
            self.history_text.insert(tk.END, str(roll) + "\n")

def main():
    root = tk.Tk()
    app = DiceRollingGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
