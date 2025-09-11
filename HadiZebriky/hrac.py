class Hrac:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.pozice = 1

    def __str__(self):
        return f"{self.jmeno} (pozice: {self.pozice})"
