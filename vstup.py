
import os
import sys


def pozdrav() -> int:
    """pozdrav a úvodní obrazovka, volba počtu číslic v hádaném čísle, počet číslic se vrací"""
    oddelovac = "-" * 50
    JELL = '\033[93m'
    CEND = '\033[0m'
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
    os.system("cls") if sys.platform == "win32" else os.system("clear")

    print(OKBLUE + "Hi there!" + CEND, oddelovac, sep="\n")
    print(JELL + "I've generated a random 4 digit number for you.",
                 "Would you like to change length of number?" + CEND, sep="\n")
    print(JELL + """
    -- easy level   --> length = 3
    -- normal level --> length = 4
    -- hard level   --> length = 5
                 """ + CEND)
    print(oddelovac)
    while (delka_cisla := input(JELL + "Yours choice must be number from (3,4,5): " + CEND)) not in "345":
        pass                    # umožní volit délku čísla 3,4,5 číslic

    print(JELL + "Let's play a bulls and cows game." + CEND, oddelovac, sep="\n")
    print(OKGREEN + "Press [Q/q] for end, else Enter a number: " + CEND, oddelovac, sep="\n")
    return int(delka_cisla)


def vstup_hrace(pozadovana_delka=4) -> list:
    """funkce načte tah hráče, ověří zda je vstupní hodnota validní a vrátí načtené číslo jako list číslic"""
    oddelovac = "-" * 60
    CRED = '\033[91m'
    CEND = '\033[0m'
    OKBLUE = '\033[94m'
    while (cislo := input()) not in "Q/q":         # možnost ukočit hru (vzdát to)
        if len(cislo) != pozadovana_delka:
            print(CRED + f"Nesprávná velikost čísla! Požadovaný počet číslic je: {pozadovana_delka}" + CEND)
            print(oddelovac)
            continue
        if not cislo.isnumeric():
            print(CRED + "Špatný vstupní údaj! Zadávej jen číselné znaky (0 ..9)!" + CEND)
            print(oddelovac)
            continue
        if cislo[0] == "0":
            print(CRED + "Číslo nemůže začínat nulou! Zadej číslo znova!" + CEND)
            print(oddelovac)
            continue
        if len(set(cislo)) != len(cislo):
            print(CRED + "Zadaj jsi špatné číslo! Žádná číslice se nesmí opakovat!" + CEND)
            print(oddelovac)
            continue

        return list(cislo)
    print(OKBLUE + "Game over!" + CEND)
    return exit()


if __name__ == "__main__":
    a = pozdrav()
    print(vstup_hrace(a))
