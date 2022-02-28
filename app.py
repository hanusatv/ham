import json, random
from pickle import FALSE, TRUE

file = open("data/validGuesses.json", encoding="utf-8")
validGuesses = json.load(file)
file.close()
a = (map(lambda x: x.lower(), validGuesses))
validGuesses = list(a)

file = open("data/wordlist.json", encoding="utf-8")
wordlist = json.load(file)
file.close()
a = (map(lambda x: x.lower(), wordlist))
wordlist = list(a)


def wordValidator(guess):
    if not len(guess) == 5:
        print("Orð skal vera 5 bókstavir")
        return FALSE
    else:
        if guess in validGuesses:
            return TRUE
        else:
            print("Orð ikki funnið")
            return FALSE


def counter(tryNo):
    return (print("Tú hevur nú ", 7 - tryNo, " forsøk eftir."))


def evaluateGuess(answer, guess, tryNo):
    logString = ""
    icons = f'{tryNo}'
    letterList = ["", "", "", "", ""]
    if guess == answer:
        icons += f'\x1b[0;30;42m {guess.upper()} \x1b[0m \nTillukku!! Tú vann \U0001F64A \U0001F44C \U0001F973'
        return icons
    for i, c in enumerate(guess):
        if c == answer[i]:
            icons += f'\x1b[0;30;42m {c.upper()} \x1b[0m'
            logString += c
        elif c in answer and answer.count(c) > logString.count(c):
            icons += f'\x1b[0;30;43m {c.upper()} \x1b[0m'
            logString += c
        else:
            icons += f'\x1b[6;30;47m {c.upper()} \x1b[0m'
    icons += "\n"

    return (icons)


if __name__ == "__main__":
    tryNo = 1
    iconsList = ""
    answer = "abbin"  #random.choice(wordlist).lower()
    while tryNo < 7:
        counter(tryNo)
        guess = input("Gita hvat orðið er: ").lower()
        if wordValidator(guess) == TRUE:
            iconsList += evaluateGuess(answer, guess, tryNo)
            print(iconsList)
            if answer == guess:
                break
            tryNo += 1
        if tryNo == 7:
            print(f'Øvv. Tú kláraði tað ikki \U0001F622 \nOrðið var {answer}')
