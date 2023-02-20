import tkinter as tk
from tkinter import END
from tkinter.scrolledtext import ScrolledText
from itertools import cycle


class ColorButton(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.config(width=5, height=3, command=self.b_color)
        self.config(bg='grey')
        self.cur_color = 'grey'
        self.colors = ['green', 'yellow', 'grey']
        self.color_gen = cycle(self.colors)

    def b_color(self):
        self.cur_color = next(self.color_gen)
        self.config(bg=self.cur_color)

    def reset_button(self):
        self.config(text='', bg='grey')
        while True:
            self.cur_color = next(self.color_gen)
            if self.cur_color == 'grey':
                break

class AnswerField(ScrolledText):
    def __init__(self, *args, **kwargs):
        ScrolledText.__init__(self, *args, **kwargs)
        self.config(state='disabled')

    def print_form(self, l, words_per_line):
        """
        Prints entries in list 'l' as an argument-specified words per line. If list is empty, function returns  that
        there are no word matches.
        """
        self.config(state='normal')
        self.delete("1.0", END)
        if not l:
            self.insert(END, 'No word matches found.')
        else:
            j = 0
            for i, word in enumerate(l):
                word = word.strip()
                if i+1 != len(l):
                    self.insert(END, f'{word}, ')
                    j += 1
                else:
                    self.insert(END, f'{word}')
                if j % words_per_line == 0:
                    self.insert(END, f'\n')
        self.config(state='disabled')
