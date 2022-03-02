
# ---------------------------------  statistika  ----------------------------------------
import sys
import os


def statistika_view(stat_hrace: list)-> list:
    """funkce zobrazí statistiku hráče a umožní zápis do tabulky hráčů"""
    oddelovac = "*" * 50
    CEND = '\033[0m'
    OKBLUE = '\033[94m'
    JELL = '\033[93m'
    OKGREEN = '\033[92m'
    print(OKBLUE + "Correct, you've guessed the right number!" + CEND)
    print(" Tvé skóré je: {}\n Počet pokusu hádání byl: {}\n Délka hraní hry: {} [min:sec.]".format(*stat_hrace))
    print(oddelovac)
    print(JELL + "Would you like to enter your name to Table WINNERS?" + CEND)
    name = input(OKGREEN + "If you want, then type your name, else press [Q/q] :" + CEND)
    if name in "Q/q":
        return False

    return name

def do_file(veta:str)-> str:
    if not os.path.exists('Table_WINNERS.txt'):
        with open('Table_WINNERS.txt', mode='a', encoding='utf-8') as soubor:
            print(veta, file=soubor)
            return 'Table_WINNERS.txt'

    with open('Table_WINNERS.txt', mode='r+', encoding='utf-8') as soubor:
        vypis = soubor.readlines()
        for i, item in enumerate(vypis):
            item = item.split(";")
            slova = veta.split(";")
            if int(item[1]) < int(slova[1]):
                vypis.insert(i, veta + "\n")
                break
        else:
            print(veta, file=soubor)
            return 'Table_WINNERS.txt'
        soubor.seek(0)
        print("".join(vypis), file=soubor)
        return 'Table_WINNERS.txt'

def file_view(nazev:str):
    hlavicka = ["JMÉNO", "SKÓRE", "POKUSŮ", "ČAS [min:sec.]"]
    with open(nazev, mode='r', encoding='utf-8') as soubor:
        print("_" * 50)
        print('\033[94m' + "{:<12}|{:^10}|{:^10}|{:^17}".format(*hlavicka) + '\033[93m')
        print("_" * 50)
        for i, radek in enumerate(soubor):
            radek = radek.rstrip()
            slova = radek.split(";")
            print("{:<12}|{:^10}|{:^10}|{:^17}".format(*slova))
            if i == 15:
                break

    os.system("notepad Table_WINNERS.txt") if sys.platform == "win32" else os.system("cat Table_WINNERS.txt")



if __name__ == "__main__":
    stat_hrace1 = ['18000', '4', '00:10']
#    print(statistika_view(stat_hrace1))

    file_view('Table_WINNERS.txt')




