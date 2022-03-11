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


def evaluateGuess(answer, guess, tryNo):
    logString = ""
    icons = f'{tryNo}  '
    letterList = ["", "", "", "", ""]
    # Kanna um svarið er rætt
    if guess == answer:
        icons += f'\x1b[0;30;42m {guess[0].upper()}  {guess[1].upper()}  {guess[2].upper()}  {guess[3].upper()}  {guess[4].upper()} \x1b[0m\nTillukku!! Tú vann \U0001F64A \U0001F44C \U0001F973 UwU'
        return icons
    # Finn øll tey grønu svarini
    for i, c in enumerate(guess):
        if c == answer[i]:
            letterList[i] = f'\x1b[0;30;42m {c.upper()} \x1b[0m'
            logString += c
    #Finn øll tey gulu svarini
    for i, c in enumerate(guess):
        if letterList[i] == "" and logString.count(c) < answer.count(c):
            letterList[i] = f'\x1b[0;30;43m {c.upper()} \x1b[0m'
            logString += c
    #Set restina til hvítt
    for i, c in enumerate(guess):
        if letterList[i] == "":
            letterList[i] = f'\x1b[6;30;47m {c.upper()} \x1b[0m'

    icons += f'{letterList[0]}{letterList[1]}{letterList[2]}{letterList[3]}{letterList[4]}\n'
    return (icons)


if __name__ == "__main__":
    tryNo = 1
    iconsList = ""
    answer = random.choice(wordlist).lower()
    while tryNo < 7:
        print("Tú hevur nú ", 7 - tryNo, " forsøk eftir.")
        guess = input("Gita hvat orðið er: ").lower()
        if wordValidator(guess) == TRUE:
            iconsList += evaluateGuess(answer, guess, tryNo)
            print(iconsList)
            if answer == guess:
                break
            tryNo += 1
        if tryNo == 7:
            print(
                f'Øvv. Tú kláraði tað ikki \U0001F622 \nOrðið var "{answer.upper()}"'
            )
