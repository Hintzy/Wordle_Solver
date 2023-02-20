# Wordle_Solver

This program was inspired by the popularization of Wordle and a comment from a friend of mine who said she honed her Python coding skills by trying to write a program that solves the daily Wordle.

First commit:
- Introduces a text based approach that runs through the python console. 
- Relied on user input for each guess, and indication of which letters were green, yellow, or black. 
- The first commit's logic did not know how to handle repeat letters within words.  As a result, the candidate answers produced by the program are correct, but the list of candidate answers is incomplete.

Second commit:
- Continues using a text based approach.
- The logic of the program was refined to handle double letters. 
- User input method to indicate green, yellow, and black status of each letter was changed. Asked the user for an input string of five letters indicated the color of each letter within the word (e.g. 'ggybb' for [green, green, yellow, black, black]). This reduces the amount of inputs asked for by the user and reduces potential input errors.   

Third commit:
- Introduces a GUI using Tkinter. 
- Uses all existing logic of the program. 
- Code was broken into separate files for organization. 
- Code was rewritten to take an OOP approach rather than procedural. 
