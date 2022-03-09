
# --------------------------------  generator_cisla  ------------------------------------

from random import choice


def generator_cisla(delka=4) -> list:
    """funkce vrátí tajné číslo, které bude hráč hádat, jako list číslic"""
    list_cislic = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cislo = []
    for i in range(delka):             # postupně vyberu číslice z listu a odeberu z listu číslic
        vyber = choice(list_cislic)
        while (i == 0 and vyber == "0"):
            vyber = choice(list_cislic)

        cislo.append(vyber)
        list_cislic.remove(vyber)
    # print("hledané cislo:", cislo)         # jen k ladění, nakonec smazat!, zobrazí hádané číslo
    return cislo


if __name__ == "__main__":
    print(generator_cisla(3))
    print(generator_cisla())
    print(generator_cisla(5))
