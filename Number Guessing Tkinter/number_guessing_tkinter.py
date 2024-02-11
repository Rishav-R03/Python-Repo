import tkinter as tk
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.num = random.randrange(1, 101)  # Generate random number 1-100
        self.health = 100
        self.count = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Guess the number: (1-100)")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.output_label = tk.Label(self.root, text="")
        self.output_label.pack()

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.count += 1

            if user_guess == self.num:
                self.display_win_message()
                self.root.unbind("<Return>")  # Disable button press if won
            elif user_guess > self.num:
                self.display_hint("Lower your guess.")
                self.health -= 10
            else:
                self.display_hint("Increase your guess.")
                self.health -= 10

            self.update_health_bar()

            if self.health <= 0:
                self.display_loss_message()
                self.root.unbind("<Return>")  # Disable button press if lost

        except ValueError:
            self.display_error_message()

    def display_win_message(self):
        self.output_label.config(text=f"You win! Correct number is {self.num}. Guesses: {self.count}")

    def display_loss_message(self):
        self.output_label.config(text=f"Game over! Correct number was {self.num}.")

    def display_hint(self, hint):
        self.output_label.config(text=f"Incorrect! {hint}")

    def update_health_bar(self):
        # Visual health bar representation (you can customize this)
        health_bar = "*" * int(self.health / 10)
        self.output_label.config(text=f"{self.output_label.cget('text')}  Health: {health_bar}")

    def display_error_message(self):
        self.output_label.config(text="Invalid input. Please enter a number.")


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
