
# --------------------------------  review a vypis stavu --------------------------------

def review(vzor: list, vstup_hrace: list) -> tuple:
    """funkce porovná dvě čísla (vzor a odhad) a vyhodnotí shodu číslic"""
    cows = 0
    bulls = 0
    for i in range(len(vzor)):
        if vstup_hrace[i] in vzor:
            if vstup_hrace[i] == vzor[i]:
                bulls += 1
            else:
                cows += 1

    oddelovac = "-" * 50
    text1 = "Bull" if bulls == 1 else "Bulls"
    text2 = "Cow" if cows == 1 else "Cows"
    print(f"{bulls} {text1},  {cows} {text2}")
    print(oddelovac)
    return bulls, cows      # stačilo by vracet bulls, ale dělám funkci univerzální a vrácím i "cows"


if __name__ == "__main__":
    a = list("7951")
    b = list("7825")
    print(review(a, b))
    a = list("79512")
    b = list("78523")
    print(review(a, b))