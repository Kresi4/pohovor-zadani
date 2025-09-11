import random

class Kostka:
    def __init__(self,pocet_sten=6):
        self._pocet_sten = pocet_sten

    def hod(self):
        return random.randint(1, self._pocet_sten)

    def __str__(self):
        return str(f"Kostka s {self._pocet_sten} stěnami.")