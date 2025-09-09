import os
from hra import spust_hru
from kostka import Kostka
from hrac import Hrac

# Smazání předchozího logu
if os.path.exists("log.txt"):
    os.remove("log.txt")

def nacti_pocet_hracu():
    while True:
        try:
            pocet = int(input("Zadej počet hráčů: "))
            if pocet < 2:
                print("Musí být alespoň 2 hráči.")
                continue
            return pocet
        except ValueError:
            print("Zadej platné číslo.")

def vyber_kostku():
    volba = input("Zadej počet stěn kostky (Enter = 6): ")
    try:
        pocet = int(volba)
        if pocet < 2:
            print("Kostka musí mít alespoň 2 stěny. Používám 6.")
            return Kostka(6)
        return Kostka(pocet)
    except ValueError:
        return Kostka(6)

def zeptej_se_na_ai():
    volba = input("Chceš, aby hru hrála AI (automaticky)? [a/N]: ").strip().lower()
    return volba == "a"

def main():
    print("🐍 Vítejte ve hře Hadi a žebříky!")
    pocet = nacti_pocet_hracu()
    kostka = vyber_kostku()
    ai_rezim = zeptej_se_na_ai()

    hraci = [Hrac(f"Hráč {chr(65 + i)}") for i in range(pocet)]
    spust_hru(hraci, kostka, ai=ai_rezim)

if __name__ == "__main__":
    main()
