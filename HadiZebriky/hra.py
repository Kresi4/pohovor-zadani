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
            vypis(f"👥 {jiny_hrac.jmeno} byl posunut zpět na pole {jiny_hrac.pozice}")

def proved_tah(hrac, hod, ostatni_hraci, deska):
    vypis(f"{hrac.jmeno} hodil: {hod}")
    nova_pozice = hrac.pozice + hod
    if nova_pozice > deska.velikost:
        vypis(f"{hrac.jmeno} nemůže překročit pole {deska.velikost}. Zůstává na místě.")
        return False
    vypis(f"{hrac.jmeno} se posunul na pole {nova_pozice}")
    hrac.pozice = deska.aplikuj_specialni_pole(nova_pozice, hrac.jmeno, vypis)
    zpracuj_kolizi(hrac, ostatni_hraci, deska)
    if hrac.pozice == deska.velikost:
        vypis(f"\n🎉 {hrac.jmeno} vyhrál hru! 🎉")
        return True
    return False

def tah_hrace(hrac, ostatni_hraci, kostka, deska, ai=False):
    vypis(f"\n{hrac.jmeno} je na poli {hrac.pozice}")
    if not ai:
        input(f"{hrac.jmeno}, stiskni Enter pro hod kostkou...")
    else:
        time.sleep(1)
    hod, vsechny_hody, chyba = hod_kostkou(kostka)
    vypis(f"{hrac.jmeno} hodil: {vsechny_hody} → celkem {hod}")
    vysledek = proved_tah(hrac, hod, ostatni_hraci, deska)
    if chyba:
        vypis(chyba)
    return vysledek

def spust_hru(hraci, kostka, ai=False):
    deska = HerniDeska()
    while True:
        for hrac in hraci:
            ostatni_hraci = [h for h in hraci if h != hrac]
            if tah_hrace(hrac, ostatni_hraci, kostka, deska, ai):
                return
