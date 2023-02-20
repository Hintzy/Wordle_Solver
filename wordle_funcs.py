"""
Functions used by wordle solver.
"""


def globally_wrong_test(w, list_1):
    """
    Tests a word/string (w) to see if any 'globally wrong' letters are present.
    Returns true if NOT present. Returns False if present.
    """
    matches = [letter for letter in list_1 if letter in w]
    return not bool(matches)


def positionally_wrong_test(w, list_1):
    """
    Tests a word/string (w) to see if any 'positionally wrong' letters are present.
    Returns true if NOT present. Returns False if present.
    """
    matches = [(let, ind) for ind, let in enumerate(w) if (let, ind) in list_1]
    return not bool(matches)


def green_test(w, list_1, list_2):
    """
    Tests a word/string (w) to see if 'correct' letters are present.
    Starts with basic test of checking that each green letter of (list_1) is present in the word (w).
    If basic test is passed, checks that position of letters within word are correct by comparing against enumerated
    word (list_2).
    Returns true if all currently identified green letters are present and in correct positions. Returns False
    if any correctly identified are omitted or in the wrong position.
    """
    for letter in list_1:
        if letter not in w:
            return False
    matches = [(let, ind) for ind, let in enumerate(w) if (let, ind) in list_2]
    return len(matches) == len(list_2)


def yellow_test(w, list_1, list_2):
    """
    Tests a word/string (w) to see if yellow letters are present.
    Returns true if all currently identified yes letters are present. Returns False if any correctly identified
    are omitted from the word, OR if any yellow letters fall in positions where they are identified as positionally
    incorrect.
    """
    for letter in list_1:
        if letter not in w:
            return False
    matches = [(let, ind) for ind, let in enumerate(w) if (let, ind) in list_2]
    return not bool(matches)


def test_series(target, wrong, wrong_tups, green, green_tups, yellow, yellow_tups):
    candidates = []
    for word in target:
        word = word.strip()
        if globally_wrong_test(word, wrong):
            if positionally_wrong_test(word, wrong_tups):
                if green_test(word, green, green_tups):
                    if yellow_test(word, yellow, yellow_tups):
                        candidates.append(word)
    return candidates


def determine_positionally_incorrect_letters(w, green, yellow, green_tups, yellow_tups):
    multiples = [letter for letter in w if w.count(letter) > 1]
    all_i = list(range(5))
    gtpl = []
    ytpl = []
    good_i = []
    bad_i = []
    positionally_incorrect = []

    def print_pi_values():
        print(f'multiples: {multiples}')
        print(f'greentupsperletter: {gtpl}')
        print(f'yellowtupsperletter: {ytpl}')
        print(f'good_i: {good_i}')
        print(f'bad_i: {bad_i}')
        print(f'positionally incorrect: {positionally_incorrect}')

    if multiples:
        for letter in list(set(multiples)):
            if letter in green + yellow:
                gtpl = [(let, i) for (let, i) in green_tups if let == letter]
                ytpl = [(let, i) for (let, i) in yellow_tups if let == letter]
                if multiples.count(letter) != len(gtpl) and not ytpl:
                    good_i = [i for (let, i) in gtpl]
                    bad_i = [i for i in all_i if i not in good_i]
                    positionally_incorrect += [(letter, i) for i in bad_i]
        # print_pi_values()

    return positionally_incorrect


def clue_input():
    return input('Enter 5-letter string indicating color of each letters. '
                 '\n\"g\" for green, \"y\" for yellow, or \"b\" for black (e.g. ggybb): ')


def correct_answer(l):
    """
    Intended to test the 'green_tups' list to see if the length is 5.  If length is 5, function returns true, as
    all correct letters/positions have been identified.  Otherwise, returns false.
    """
    return len(l) == 5


def print_form(l, words_per_line):
    """
    Prints entries in list 'l' as an argument-specified words per line.
    """
    if not l:
        print('No word matches found.')
    else:
        for i, word in enumerate(l):
            word = word.strip()
            print(word, end='\t')
            if (i + 1) % words_per_line == 0:
                print()


def print_guess_info(guess_num, user_guess, green, green_tups, yellow, yellow_tups, wrong, wrong_tups):
    """
    Print function for internal variables for troubleshooting and development.
    """
    print(f'Guess #{guess_num}:', user_guess)
    print('Green letters: ', green)
    print('Green letters tuple: ', green_tups)
    print('Yellow letters: ', yellow)
    print('Yellow letters tuple: ', yellow_tups)
    print('Globally Wrong letters: ', wrong)
    print('Limited wrong letters: ', wrong_tups, end='\n')


def print_candidate_words(word_candidates):
    """
    Prints the resulting candidate words after user inputs and filter checks on the current word list.
    """
    print('')
    print('Potential Solutions: ')
    print_form(word_candidates, 15)
    print('\n')
