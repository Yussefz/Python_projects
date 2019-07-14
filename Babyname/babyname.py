import string , random

"""def babygenerator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    letter5 = random.choice(string.ascii_lowercase)
    letter6 = random.choice(string.ascii_lowercase)

    name = letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    return name

print(babygenerator())

"""
letter1Input = input("V for vowels, C for consonants , l for any letter")
letter2Input = input("V for vowels, C for consonants , l for any letter")
letter3Input = input("V for vowels, C for consonants , l for any letter")
letter5Input = input("V for vowels, C for consonants , l for any letter")

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxyz'

def babygenerator():
    if letter1Input == "v":
        letter1 = random.choice(vowels)
    elif letter1Input == "c":
        letter1 = random.choice(consonants)
    elif letter1Input == "l":
        letter1 = random.choice(string.ascii_lowercase)
    else:
        letter1 = letter1Input

    if letter2Input == "v":
        letter2 = random.choice(vowels)
    elif letter1Input == "c":
        letter2 = random.choice(consonants)
    elif letter2Input == "l":
        letter2 = random.choice(string.ascii_lowercase)
    else:
        letter2 = letter2Input

    if letter3Input == "v":
        letter3 = random.choice(vowels)
    elif letter1Input == "c":
        letter3 = random.choice(consonants)
    elif letter3Input == "l":
        letter3 = random.choice(string.ascii_lowercase)
    else:
        letter3 = letter2Input

    if letter5Input == "v":
        letter5 = random.choice(vowels)
    elif letter5Input == "c":
        letter5 = random.choice(consonants)
    elif letter5Input == "l":
        letter5 = random.choice(string.ascii_lowercase)
    else:
        letter5 = letter5Input

    name = letter1+letter2+letter3+letter5
    return(name)

print(babygenerator())