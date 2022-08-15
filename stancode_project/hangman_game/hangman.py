"""
File: hangman.py
Name: Abbie Chen
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    1. randomly choose a word
    2. if lives is over 0,
    then check whether the cover answer is equal to answer
    if not then keep guessing
    3. if lives is 0,
    then the user lose the game
    """
    ans = random_word()
    covered_ans = cover_the_answer(ans)
    print('The word looks like '+covered_ans)
    lives = N_TURNS
    while True:
        if lives != 0:
            if covered_ans == ans:
                print('You win!!')
                print('The word was: ' + ans)
                break
            else:
                guess = input('Your guess: ')
                effective_guess = guess.upper()
                if len(effective_guess) != 1 or not effective_guess.isalpha():
                    print('Illegal format.')
                else:
                    new_covered_ans = rebuild_new_cover(effective_guess, ans, covered_ans)
                    if ans.find(effective_guess) == -1:
                        lives -= 1
                        print('There is no '+effective_guess+"\'s in the word." )
                    else:
                        covered_ans = new_covered_ans
                        print("You're correct!")
                        print('The word looks like '+covered_ans)
                    print('You have ' + str(lives) + ' wrong guesses left.')
        if lives == 0:
            print('You are completely hung :( ')
            print('The word was: ' + ans)
            break


def rebuild_new_cover(guess, ans, covered_ans):
    # rebuild the covered answer and replace the correct guess into the cover answer string
    if ans.find(guess) != -1:
        new_covered_ans = ''
        for i in range(len(ans)):
            if ans[i] == guess:
                new_covered_ans += guess
            else:
                new_covered_ans += covered_ans[i]
    else:
        new_covered_ans = covered_ans
    return new_covered_ans


def cover_the_answer(s):
    # print the length of the words need to be guessed
    slashed_ans = ''
    for i in range(len(s)):
        slashed_ans += '-'
    return slashed_ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
