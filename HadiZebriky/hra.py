from utils import hod_kostkou
import time
from herni_deska import ZEBRIKY, HADI
from vypis import vypis

def aplikuj_specialni_pole(pozice, jmeno):
    if pozice in ZEBRIKY:
        nova_pozice = ZEBRIKY[pozice]
        vypis(f"↑ {jmeno} vylezl po žebříku na pole {nova_pozice}")
        return nova_pozice
    elif pozice in HADI:
        nova_pozice = HADI[pozice]
        vypis(f"🐍 {jmeno} spadl na pole {nova_pozice}")
        return nova_pozice
    return pozice

def zpracuj_kolizi(hrac, ostatni_hraci):
    for jiny_hrac in ostatni_hraci:
        if jiny_hrac.pozice == hrac.pozice:
            vypis(f"👥 {hrac.jmeno} přistál na poli {hrac.pozice}, kde je {jiny_hrac.jmeno}")
            jiny_hrac.pozice = max(1, jiny_hrac.pozice - 1)
            vypis(f"👥 {jiny_hrac.jmeno} přistál na poli {jiny_hrac.pozice}.")
            jiny_hrac.pozice = aplikuj_specialni_pole(jiny_hrac.pozice, jiny_hrac.jmeno)


def tah_hrace(hrac, ostatni, kostka, ai=False):
    vypis(f"\n {hrac.jmeno} je na poli {hrac.pozice}")

    if not ai:
        input(f"{hrac.jmeno}, stiskni Enter pro hod kostkou...")
    else:
        time.sleep(1)  # pauza před hodem

    tah, hody = hod_kostkou(kostka)
    vypis(f"{hrac.jmeno} hodil: {hody} → celkem {tah}")

    time.sleep(0.5)  # pauza mezi hodem a přesunem

    nova = hrac.pozice + tah
    if nova > 100:
        vypis(f"{hrac.jmeno} nemůže překročit pole 100. Zůstává na místě.")
        return False

    vypis(f"{hrac.jmeno} se posunul na pole {nova}")
    nova = aplikuj_specialni_pole(nova, hrac.jmeno)

    hrac.pozice = nova
    zpracuj_kolizi(hrac, ostatni)

    if hrac.pozice == 100:
        vypis(f"\n🎉 {hrac.jmeno} vyhrál hru! 🎉")
        return True

    if ai:
        time.sleep(1)  # pauza před dalším hráčem

    return False


def spust_hru(hraci, kostka, ai=False):
    vyhral = False
    while not vyhral:
        for hrac in hraci:
            ostatni = [h for h in hraci if h != hrac]
            vyhral = tah_hrace(hrac, ostatni, kostka, ai)
            if vyhral:
                break
