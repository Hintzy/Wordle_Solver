"""
TODO:
- end game condition (max guesses, or answer correct)
"""


import tkinter as tk
from tkinter import END
from tk_custom_items import ColorButton
from tk_custom_items import AnswerField
from wordle_funcs import *


class App:

    def __init__(self):
        # initializing general program constants
        self.PATH = open('words5.txt')
        self.TITLE_FONT = ('Arial', 14, 'normal')
        self.FIELD_FONT = ('Arial', 14, 'normal')
        self.BUTTON_FONT = ('Arial', 14, 'bold')
        self.WIN_W = 800
        self.WIN_H = 700

        # initializing game relevant variables
        self.guess_num = 1
        self.user_guess = ''
        self.clue = ''
        self.green = []
        self.green_tups = []
        self.yellow = []
        self.yellow_tups = []
        self.wrong = []
        self.wrong_tups = []
        self.word_candidates = []
        self.last_results = []

        # initialize the screen
        self.root = tk.Tk()
        self.root.title('World Solver v1.0')
        self.root.geometry('800x700')
        self.root.config(padx=50, pady=25)

        # screen header and field labels
        self.header = tk.Label(self.root)
        self.header.config(text='Wordle Solver v1.0', font=self.TITLE_FONT, justify='center')
        self.header.place(x=300, y=50)

        self.ans_label = tk.Label(self.root)
        self.ans_label.config(text='Potential answers:', font=self.FIELD_FONT)
        self.ans_label.place(x=0, y=200)

        self.guess_label = tk.Label(self.root)
        self.guess_label.config(text=f'Guess #{self.guess_num}', font=self.FIELD_FONT)
        self.guess_label.place(x=0, y=120)

        # entry field - user guess
        self.guess_field = tk.Entry(self.root)
        self.guess_field.config(width=30, borderwidth=3)
        self.guess_field.insert(END, string='')
        self.guess_field.place(x=0, y= 150)

        # initialize letter buttons and set locations on screen
        self.let_1 = ColorButton(self.root)
        self.let_2 = ColorButton(self.root)
        self.let_3 = ColorButton(self.root)
        self.let_4 = ColorButton(self.root)
        self.let_5 = ColorButton(self.root)

        self.let_1.place(x=350, y=120)
        self.let_2.place(x=410, y=120)
        self.let_3.place(x=470, y=120)
        self.let_4.place(x=530, y=120)
        self.let_5.place(x=590, y=120)

        # answers field
        self.a_box = AnswerField(self.root, height=25, width=87)
        self.a_box.config(borderwidth=3, state='disabled')
        self.a_box.place(x=0, y=230)

        # confirm guess button
        self.confirm_guess = tk.Button(text='OK', command=self.take_guess)
        self.confirm_guess.place(x=200, y=145)

        # confirm colors button (and
        self.letters_OK = tk.Button()
        self.letters_OK.config(text='OK', command=self.process_guess)
        self.letters_OK.place(x=660, y=135)


        # a list of the color buttons for iteration
        self.ans_buttons = [self.let_1, self.let_2, self.let_3, self.let_4, self.let_5]

    def take_guess(self):
        """
        Takes text string from the guess field and assigns it to user_guess attribute,
        also translates them to the five colored buttons.
        """
        self.user_guess = self.guess_field.get()
        for i, button in enumerate(self.ans_buttons):
            button.config(text=(self.guess_field.get()).upper()[i])

    def process_clue(self):
        """
        Iterates through the color buttons, creating a 5-character string that represents
        the selected colors
        """
        c = ''
        d = {
            'green': 'g',
            'yellow': 'y',
            'grey': 'b'
        }
        for arg in self.ans_buttons:
            c += d[arg.cur_color]

        for i, color in enumerate(c):
            if color == 'g':
                self.green.append(self.user_guess[i])
                self.green_tups.append((self.user_guess[i], i))
                self.green = list(set(self.green))
                self.green_tups = list(set(self.green_tups))
            elif color == 'y':
                self.yellow.append(self.user_guess[i])
                self.yellow_tups.append((self.user_guess[i], i))
                self.yellow = list(set(self.yellow))
                self.yellow_tups = list(set(self.yellow_tups))

    def reset_window(self):
        """
        Resets the guess field and the colored buttons
        """
        self.guess_field.delete(0, END)
        for arg in self.ans_buttons:
            arg.reset_button()

    def process_guess(self):
        self.clue = ''
        self.process_clue()
        self.wrong += [x for x in self.user_guess if x not in (self.green + self.yellow)]
        self.wrong = list(set(self.wrong))
        self.wrong_tups += determine_positionally_incorrect_letters(self.user_guess, self.green,
                                                                    self.yellow, self.green_tups, self.yellow_tups)
        self.wrong_tups = list(set(self.wrong_tups))

        if correct_answer(self.green_tups):
            pass
            # TODO: create win condition function
        elif self.guess_num == 1:
            self.word_candidates = test_series(self.PATH, self.wrong, self.wrong_tups, self.green,
                                               self.green_tups, self.yellow, self.yellow_tups)
            self.last_results = self.word_candidates.copy()
        else:
            self.word_candidates = test_series(self.last_results, self.wrong, self.wrong_tups, self.green,
                                               self.green_tups, self.yellow, self.yellow_tups)
            self.last_results = self.word_candidates.copy()

        self.a_box.print_form(self.word_candidates, 12)
        self.guess_num += 1
        self.guess_label.config(text=f'Guess #{self.guess_num}')
        self.reset_window()
        # print_guess_info(guess_num, user_guess, green, green_tups, yellow, yellow_tups, wrong, wrong_tups)
        # print(f'clue = {clue}')

    def run(self):
        self.root.mainloop()

    def quit(self):
        self.root.quit()

