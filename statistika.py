
# ---------------------------------  statistika  ----------------------------------------
import os


def statistika_view(stat_hry: list) -> str:
    """funkce zobrazí statistiku hry a umožní přidat jméno ke statistice hry"""
    oddelovac = "*" * 50
    CEND = '\033[0m'
    OKBLUE = '\033[94m'
    JELL = '\033[93m'
    OKGREEN = '\033[92m'
    print(OKBLUE + "Correct, you've guessed the right number!" + CEND)
    print(" Tvé skóré je: {}\n Počet pokusu hádání byl: {}\n Délka hraní hry: {} [min:sec.]".format(*stat_hry))
    print(oddelovac)
    print(JELL + "Would you like to enter your name to Table WINNERS?" + CEND)
    name = input(OKGREEN + "If you want, then type your name, else press [Q/q] :" + CEND)
    if name in "Q/q":
        return ""            # prázný řetězec

    return name


def do_file(veta: str) -> str:
    """fukce provede zápis záznamu(věty) do soubotu a vrátí jeho jméno"""
    if not os.path.exists('Table_WINNERS.txt'):                 # při první hře neexistuje soubor
        with open('Table_WINNERS.txt', mode='a', encoding='utf-8') as soubor:
            soubor.write(veta + "\n")
            return 'Table_WINNERS.txt'

    with open('Table_WINNERS.txt', mode='r+', encoding='utf-8') as soubor:
        vypis = soubor.readlines()
        for i, item in enumerate(vypis):   # nový záznam vložím na příslušný řádek, třídím podle skoré
            item = item.split(";")
            slova = veta.split(";")
            if int(item[1]) < int(slova[1]):       # pozice skoré je na indexu [1]
                vypis.insert(i, veta + "\n")
                break
        else:
            soubor.write(veta + "\n")          # připíše záznam na konec
            return 'Table_WINNERS.txt'
        soubor.seek(0)
        soubor.write("".join(vypis))    # zapíše setřízený list podle skoré
        return 'Table_WINNERS.txt'


def file_view(nazev: str):
    """funkce provede výpis tabulky vítězů, prvnich 15 záznamu """
    hlavicka = ["JMÉNO", "SKÓRE", "POKUSŮ", "ČAS [min:sec.]"]
    with open(nazev, mode='r', encoding='utf-8') as soubor:
        print('\033[93m' + "_" * 50 + '\033[0m')
        print('\033[94m' + "{:<12}|{:^10}|{:^10}|{:^17}".format(*hlavicka) + '\033[93m')
        print("_" * 50)
        for i, radek in enumerate(soubor):
            radek = radek.rstrip()
            slova = radek.split(";")
            print("{:<12}|{:^10}|{:^10}|{:^17}".format(*slova))
            if i == 15:
                break


if __name__ == "__main__":
    stat_hry1 = ['18000', '4', '00:10']
    print(statistika_view(stat_hry1))

    veta1 = 'Martin;101756;1;00:07'

    # file_view('Table_WINNERS.txt')
