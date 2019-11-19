import string , random


letter1Input = input("V for vowels, C for consonants , l for any letter : ")
letter2Input = input("V for vowels, C for consonants , l for any letter : ")
letter3Input = input("V for vowels, C for consonants , l for any letter : ")
letter4Input = input("V for vowels, C for consonants , l for any letter : ")

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
        letter3 = letter3Input

    if letter4Input == "v":
        letter4 = random.choice(vowels)
    elif letter4Input == "c":
        letter4 = random.choice(consonants)
    elif letter4Input == "l":
        letter4 = random.choice(string.ascii_lowercase)
    else:
        letter4 = letter4Input
        

        
    name = letter1+letter2+letter3+letter4
    return(name)

print('The generated name is :    ' + babygenerator())