
# ---------------------------------  main  ----------------------------------------------
# ------------ hlavní program ze kterého pouštím hru ---Bulls_&_Cows---------------------
import time

from vstup import pozdrav, vstup_hrace
from generator_cisla import generator_cisla
from review import review
from statistika import statistika_view, do_file, file_view

delka_cisla = pozdrav()                      # úvod do hry, a vrací počet znaků hádaného čísla
vzor = generator_cisla(delka_cisla)          # vygeneruje se hádané číslo
bulls = 0
pocet_pokusu = 0
time_start = time.time()
while bulls != delka_cisla:    # hru dohraji, když všecny čísla budou správné a na svých pozicích
    bulls, cows = review(vzor, vstup_hrace(delka_cisla))    # zobrazí průběh hry a uloží stav hry
    pocet_pokusu += 1

time_elapsed = time.time() - time_start                                   # měřím délku hraní hry
score = 300 * delka_cisla + int(100000 / pocet_pokusu) + int(2000 / time_elapsed)    # můj vzorec
delka_hry = time.strftime("%M:%S", time.gmtime(time_elapsed))   # formátování na minuty a sekundy
stat_hry = [str(score), str(pocet_pokusu), delka_hry]                            # statistika hry
name = statistika_view(stat_hry)        # zobrazení na konci hry, možnost zápisu jména do tabulky

if name:                                   # pokud je vráceno nějaké jméno, tak bool(name) = True
    stat_hry.insert(0, name)
    stat_hrace_str = ";".join(stat_hry)
    nazev_file = do_file(stat_hrace_str)                        # zápis záznamu do souboru vítězů
    file_view(nazev_file)                                              # výpis tabulky ze souboru
