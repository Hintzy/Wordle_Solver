'''
To Do:
- Handling double letters within words
- Implementation of word/index pairs on green/yellow letters for specifying position in words
    - Use enumerate function on user_guess variable?
'''

fin = open('words.txt')
fout = open('words5.txt', 'w')
fin2 = open('words5.txt')
user_guess = []
wrong = []
green = []
yellow = []
word_candidates = []
wrong_words = []
wrong_letters = []
guess_num = 1
last_results = []

def word_list_5(l):
    for line in l:
        line = line.strip()
        if len(line) == 5:
            fout.write(line)
            fout.write('\n')
    fout.close()


def wrong_let_test(w):
    global wrong_words
    for letter in wrong:
        if letter in w:
            return False
    return True


def green_let_test(w):
    global wrong_words
    for letter in green:
        if letter not in w:
            return False
        if w.index(letter) != user_guess.index(letter):
            return False
    return True


def yellow_let_test(w):
    for letter in yellow:
        if letter not in w:
            return False
        if w.index(letter) == user_guess.index(letter):
            return False
    return True


def test_series(target):
    global word_candidates
    word_candidates.clear()
    for word in target:
        if wrong_let_test(word):
            if green_let_test(word):
                if yellow_let_test(word):
                    word_candidates.append(word)


def det_eligible_words():
    global user_guess
    global guess_num
    global wrong
    global green
    global yellow
    global word_candidates
    global wrong_letters

    user_guess = list(input(f'Guess #{guess_num}: '))
    green_letters = list(input('Green letters: '))
    yellow_letters = list(input('Yellow letters: '))
    wrong_letters += [x for x in user_guess if x not in (green_letters + yellow_letters)]
    word_candidates = []

    if guess_num == 1:
        test_series(fin2)
    if guess_num > 1:
        test_series(last_results)


def print_form(l, words_per_line):
    if not l:
        print('No word matches found.')
    else:
        for i, word in enumerate(l):
            word = word.strip()
            print(word, end='\t')
            if (i + 1) % words_per_line == 0:
                print()


def print_guess_info():
    print(f'Guess #{guess_num}:', user_guess)
    print('Wrong letters: ', wrong)
    print('Green letters: ', green)
    print('Yellow letters: ', yellow, end='\n')


def print_results():
    global guess_num
    global last_results
    print()
    print('Potential Solutions: ')
    print_form(word_candidates, 10)
    last_results = word_candidates.copy()
    print()
    guess_num += 1


if __name__ == '__main__':
    word_list_5(fin)
    while guess_num < 7:
        det_eligible_words()
        print_guess_info()
        print_results()


