import json, re, random

# Ger ein lista við øllum valid guesses
file = open("data/validGuesses.json", encoding="utf-8")
validGuesses = json.load(file)
file.close()
a = (map(lambda x: x.lower(), validGuesses))
validGuesses = list(a)

#Ger klassa við litaðum orðum


def colorCodeLettersInGuess(answer, guess):
    # Kanna um svarið er rætt
    if guess == answer:
        return True

    # Finn grønir bókstavir
    colorCoded = {"green": {}, "yellow": {}, "white": {}}
    for i, letter in enumerate(guess):
        if letter == answer[i]:
            if letter in colorCoded["green"]:
                colorCoded["green"][letter].append(i)
            else:
                colorCoded["green"][letter] = [i]

    #Finn gulir og hvítir bókstavir
    for i, letter in enumerate(guess):
        if guess[i] in answer:
            greenNo = 0
            yellowNo = 0
            if letter in colorCoded["green"].keys():
                if i in colorCoded["green"][letter]:
                    continue
                else:
                    greenNo = len(colorCoded["green"][letter])
            if letter in colorCoded["yellow"].keys():
                yellowNo = len(colorCoded["yellow"][letter])
            if greenNo + yellowNo < answer.count(letter):
                if letter in colorCoded["yellow"]:
                    colorCoded["yellow"][letter].append(i)
                else:
                    colorCoded["yellow"][letter] = [i]
            else:
                if letter in colorCoded["white"]:
                    colorCoded["white"][letter].append(i)
                else:
                    colorCoded["white"][letter] = [i]
        else:
            if letter in colorCoded["white"]:
                colorCoded["white"][letter].append(i)
            else:
                colorCoded["white"][letter] = [i]
    return (colorCoded)


def filterValidGuesses(coloredGuess, filteredList, guess):
    regExList = [".", ".", ".", ".", "."]
    #print("Giti er:", guess)
    #Forlanga allar grønar í positiónini
    greenLetters = coloredGuess["green"].keys()
    for key in greenLetters:
        for pos in coloredGuess["green"][key]:
            regExList[pos] = key
    #Útilukka allar gular frá positiónini
    yellowLetters = coloredGuess["yellow"].keys()
    for key in yellowLetters:
        for pos in coloredGuess["yellow"][key]:
            regExList[pos] = f'[^{key}]'
    # Bygg ein pure white exclude string
    whiteLetters = coloredGuess["white"].keys()
    excludedWhiteLetters = ""
    excludedWhiteLettersPosition = []
    for key in whiteLetters:
        if (key in greenLetters
                or key in yellowLetters) or key in excludedWhiteLetters:
            continue
        else:
            excludedWhiteLetters += key
            for pos in coloredGuess["white"][key]:
                excludedWhiteLettersPosition.append(pos)
    # Smekka excluded lettes í regex positiónir
    for pos in excludedWhiteLettersPosition:
        if excludedWhiteLetters != "":
            regExList[pos] = f'[^{excludedWhiteLetters}]'

    #Set strongin saman
    regExString = "".join(regExList)
    pattern = re.compile(regExString)
    filteredValidGuesses = []
    for word in filteredList:
        if re.match(pattern, word):
            filteredValidGuesses.append(word)
    #print(filteredValidGuesses)

    return filteredValidGuesses


def averageRun(plays):
    noOfGuesses = []
    for n in range(plays):
        if n % 100 == 0:
            print(n)
        t = playWordle()
        noOfGuesses.append(t)
    print(sum(noOfGuesses) / len(noOfGuesses))


def playWordle():
    wordle = random.choice(validGuesses).lower()
    filteredList = validGuesses
    guessNo = 1
    coloredGuess = False
    while coloredGuess != True:
        #print(wordle, filteredList)
        if filteredList == []:
            print(wordle)
        guess = random.choice(filteredList).lower()
        guessNo += 1
        #print("Gitið er:", guess)
        coloredGuess = colorCodeLettersInGuess(wordle, guess)
        if coloredGuess == True:
            return guessNo
        filteredList = filterValidGuesses(coloredGuess, filteredList, guess)

    #print(f'Tú vann! Orðið var {wordle} og tú hevur gitt {guessNo} ferð')


if __name__ == "__main__":
    #print(playWordle())
    averageRun(10000)
