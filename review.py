
# --------------------------------  review a vypis stavu --------------------------------

def review(vzor: list, odhad: list) -> tuple:
    """funkce porovná dvě čísla (vzor a odhad) a vyhodnotí shodu číslic"""
    cows = len(set(vzor).intersection(set(odhad)))
    bulls = 0
    for i in range(len(vzor)):
        if vzor[i] == odhad[i]:
            bulls += 1

    oddelovac = "-" * 50
    text1 = "Bull" if bulls == 1 else "Bulls"
    text2 = "Cow" if cows == 1 else "Cows"
    print(f"{bulls} {text1},  {cows} {text2}")
    print(oddelovac)
    return bulls, cows


if __name__ == "__main__":
    a = list("7951")
    b = list("7825")
    print(review(a, b))
