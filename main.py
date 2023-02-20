from wordle_funcs import *

if __name__ == '__main__':
    PATH = open('words5.txt')

    guess_num = 1
    user_guess = []
    green = []
    green_tups = []
    yellow = []
    yellow_tups = []
    wrong = []
    wrong_tups = []
    word_candidates = []
    last_results = []


    while guess_num < 7:
        user_guess = input(f'Guess #{guess_num}: ')
        user_guess = list(user_guess.lower())
        clues = clue_input()

        for i, color in enumerate(clues):
            if color == 'g':
                green.append(user_guess[i])
                green_tups.append((user_guess[i], i))
                green = list(set(green))
                green_tups = list(set(green_tups))
            elif color == 'y':
                yellow.append(user_guess[i])
                yellow_tups.append((user_guess[i], i))
                yellow = list(set(yellow))
                yellow_tups = list(set(yellow_tups))

        wrong += [x for x in user_guess if x not in (green + yellow)]
        wrong = list(set(wrong))
        wrong_tups += determine_positionally_incorrect_letters(user_guess, green, yellow, green_tups, yellow_tups)
        wrong_tups = list(set(wrong_tups))

        if correct_answer(green_tups):
            break
        elif guess_num == 1:
            word_candidates = test_series(PATH, wrong, wrong_tups, green, green_tups, yellow, yellow_tups)
            last_results = word_candidates.copy()
        else:
            word_candidates = test_series(last_results, wrong, wrong_tups, green, green_tups, yellow, yellow_tups)
            last_results = word_candidates.copy()

        print_candidate_words(word_candidates)
        print_guess_info(guess_num, user_guess, green, green_tups, yellow, yellow_tups, wrong, wrong_tups)
        guess_num += 1

    if correct_answer(green_tups):
        print('You got it! Great job!')
    else:
        print('Out of guesses! Better luck next time!')
