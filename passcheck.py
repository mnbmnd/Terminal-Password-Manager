#######################################################################################
# Author: Muneeb Mennad                                                              # 
# Project Name: Passman                                                             #  
# File Name: passcheck.py                                                          #   
# Project Start: 2026-01-24                                                         #  
# Github: https://github.com/mnbmnd                                                  # 
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import string
import math

LOWERCASE = 26
UPPERCASE = 26
NUMERICAL = 10
SYMBOLS = 32
SPACE = 1

BCRYPT_COST = 12
GUESSES_PER_SEC = 1e5
SECONDS_PER_YEAR = 6.308 * (10**7)


def getSize(password):
    return len(password)


def getUppercaseCount(password):
    upperCount = 0
    for i in password:
        if i.isupper():
            upperCount += 1
    return upperCount


def getLowercaseCount(password):
    lowerCount = 0
    for i in password:
        if i.islower():
            lowerCount += 1
    return lowerCount


def getNumericCount(password):
    numericCount = 0
    for i in password:
        if i.isnumeric():
            numericCount += 1
    return numericCount


def getSymbolsCount(password):
    symbols = list(string.punctuation)
    symbolsCount = 0
    for i in password:
        if i in symbols:
            symbolsCount += 1
    return symbolsCount


def getSpaceCount(password):
    spaceCount = 0
    for i in password:
        if i == " ":
            spaceCount += 1
    return spaceCount


def getCharactersAvailable(password):
    characters = 0
    if getLowercaseCount(password):
        characters += LOWERCASE

    if getUppercaseCount(password):
        characters += UPPERCASE

    if getNumericCount(password):
        characters += NUMERICAL

    if getSymbolsCount(password):
        characters += SYMBOLS

    if getSpaceCount(password):
        characters += SPACE

    return characters


def getEntropy(password):
    passwordLength = getSize(password)
    r = getCharactersAvailable(password)
    entropy = math.log2(r**passwordLength)

    return entropy


def getSampleSpaceSize(password):
    charactersAvailable = getCharactersAvailable(password)
    n = getSize(password)
    sampleSpaceSize = charactersAvailable**n
    return sampleSpaceSize


# def getAttemptsPerSecond():
#     # function expands on attempts per second
#     pass


# def getTimeToCrack(password):
#     sampleSpace = getSampleSpaceSize(password)
#     timeToCrack = sampleSpace / (GUESSES_PER_SEC * SECONDS_PER_YEAR)
#     return timeToCrack
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
