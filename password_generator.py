##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Password Strength Checker & Generator                                                                                        #
# File Name: password_generator.py                                                                                                           #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: pchstpch                                                                                                                  #
#                                                                                                                                            #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import string
import secrets
from pathlib import Path

BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / 'words_alpha.txt'

def generatePassphrase():
    with open(file_path) as f:
        words = [word.strip() for word in f]
        password = ' '.join(secrets.choice(words) for i in range(4))
    return password
    
def generateString(length):
    characters = string.ascii_letters + string.digits # + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for i in range(int(length)))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    return password

def generatePassword(length, mode):
    if mode == 1:
        passphrase = generatePassphrase()
        return passphrase
    elif mode == 2:
        stringPass = generateString(length)
        return stringPass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #