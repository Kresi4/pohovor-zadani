class HerniDeska:
    def __init__(self, zebriky=None, hadi=None, velikost=100):
        self.zebriky = zebriky or {
            2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84,
            36: 44, 51: 67, 71: 91, 78: 98, 87: 94
        }
        self.hadi = hadi or {
            16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53,
            89: 68, 92: 88, 95: 75, 99: 80
        }
        self.velikost = velikost

    def aplikuj_specialni_pole(self, pozice, jmeno, vypis_func=print):
        if pozice in self.zebriky:
            nova_pozice = self.zebriky[pozice]
            vypis_func(f"↑ {jmeno} vylezl po žebříku na pole {nova_pozice}")
            return nova_pozice
        elif pozice in self.hadi:
            nova_pozice = self.hadi[pozice]
            vypis_func(f"↓ {jmeno} spadl na pole {nova_pozice}")
            return nova_pozice
        return pozice


