from wordlist import ADJECTIVES, NOUNS
from random import choice as randchoice
import random


def underscore(name, adjective, noun):
    name = adjective + "_" + name.lower() + "_" + noun
    return name


def camel_case(name, adjective, noun):
    camel_case_adjective = adjective[0].upper() + adjective[1:]
    camel_case_noun = noun[0].upper() + noun[1:]
    uname = name[0].upper() + name[1:]
    name = (camel_case_adjective + uname + camel_case_noun)
    return name


def make_username(name):
    usernameList = []
    for i in range(15):
        uname = ''
        adjective = randchoice(ADJECTIVES)
        noun = randchoice(NOUNS)
        if random.randint(1, 2) == 1:
            uname = underscore(name, adjective, noun)
            usernameList.append(uname)
        else:
            uname = camel_case(name, adjective, noun)
            usernameList.append(uname)

    return usernameList


if __name__ == "__main__":
    print(make_username('Mayank'))
