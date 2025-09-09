from utils import hod_kostkou
from vypis import vypis
from herni_deska import HerniDeska
import time

def zpracuj_kolizi(hrac, ostatni_hraci, deska):
    for jiny_hrac in ostatni_hraci:
        if jiny_hrac.pozice == hrac.pozice:
            vypis(f"👥 {hrac.jmeno} přistál na poli {hrac.pozice}, kde je {jiny_hrac.jmeno}")
            nova_pozice = deska.aplikuj_specialni_pole(max(1, jiny_hrac.pozice - 1), jiny_hrac.jmeno, vypis)
            jiny_hrac.pozice = nova_pozice

def tah_hrace(hrac, ostatni, kostka, deska, ai=False):
    vypis(f"\n {hrac.jmeno} je na poli {hrac.pozice}")
    if not ai:
        input(f"{hrac.jmeno}, stiskni Enter pro hod kostkou...")
    else:
        time.sleep(1)
    tah, hody = hod_kostkou(kostka)
    vypis(f"{hrac.jmeno} hodil: {hody} → celkem {tah}")
    time.sleep(0.5)
    nova = hrac.pozice + tah
    if nova > deska.velikost:
        vypis(f"{hrac.jmeno} nemůže překročit pole {deska.velikost}. Zůstává na místě.")
        return False
    vypis(f"{hrac.jmeno} se posunul na pole {nova}")
    hrac.pozice = deska.aplikuj_specialni_pole(nova, hrac.jmeno, vypis)
    zpracuj_kolizi(hrac, ostatni, deska)
    if hrac.pozice == deska.velikost:
        vypis(f"\n🎉 {hrac.jmeno} vyhrál hru! 🎉")
        return True
    if ai:
        time.sleep(1)
    return False

def spust_hru(hraci, kostka, ai=False):
    deska = HerniDeska()
    while True:
        for hrac in hraci:
            ostatni = [h for h in hraci if h != hrac]
            if tah_hrace(hrac, ostatni, kostka, deska, ai):
                return
