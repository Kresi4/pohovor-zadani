import os
from hrac import Hrac
from kostka import Kostka
from hra import spust_hru

def nacti_pocet_hracu():
    while True:
        try:
            pocet = int(input("Zadej počet hráčů (2-8): "))
            if 2 <= pocet <= 8:
                return pocet
            print("Počet hráčů musí být mezi 2 a 8.")
        except ValueError:
            print("Zadej platné číslo.")

def vyber_kostku():
    volba = input("Zadej počet stěn kostky (Enter = 6): ")
    try:
        pocet = int(volba)
        if pocet >= 2:
            return Kostka(pocet)
        print("Používám 6 stěn.")
    except ValueError:
        pass
    return Kostka(6)

def zeptej_se_na_ai():
    return input("Chceš, aby hru hrála AI (automaticky)? [a/N]: ").strip().lower() == "a"

def spustit_hru():
    if os.path.exists("log.txt"):
        os.remove("log.txt")
    print("🐍 Vítejte ve hře Hadi a žebříky!")
    pocet = nacti_pocet_hracu()
    kostka = vyber_kostku()
    ai = zeptej_se_na_ai()
    hraci = [Hrac(f"Hráč {chr(65 + i)}") for i in range(pocet)]
    spust_hru(hraci, kostka, ai=ai)
