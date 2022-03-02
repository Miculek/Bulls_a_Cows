
# ---------------------------------  main  ----------------------------------------------
# ------------ hlavní program ze kterého pouštím hru ---Bulls_&_Cows---------------------
import time

from vstup import pozdrav, vstup_hrace
from generator_cisla import generator_cisla
from review import review
from statistika import statistika_view, do_file, file_view

delka_cisla = pozdrav()
vzor = generator_cisla(delka_cisla)
bulls = 0
pocet_pokusu = 0
time_start = time.time()
while bulls != delka_cisla:
    bulls, cows = review(vzor, vstup_hrace(delka_cisla))
    pocet_pokusu += 1

time_elapsed = time.time() - time_start
score = 300 * delka_cisla + int(100000 / pocet_pokusu) + int(2000 / time_elapsed)
delka_hry = time.strftime("%M:%S", time.gmtime(time_elapsed))  # formát na minuty a sekundy
stat_hrace = [str(score), str(pocet_pokusu), delka_hry]
name = statistika_view(stat_hrace)
if name:
    stat_hrace.insert(0, (name))
    stat_hrace_S = ";".join(stat_hrace)
    print(stat_hrace_S)     #TODO k ladeni
    nazev_file = do_file(stat_hrace_S)
    file_view(nazev_file)

