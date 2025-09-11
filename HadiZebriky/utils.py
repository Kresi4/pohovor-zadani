def hod_kostkou(kostka, max_hodu=20):
    hody = []
    soucet = 0
    for _ in range(max_hodu):
        hod = kostka.hod()
        hody.append(hod)
        soucet += hod
        if hod != 6:
            return soucet, hody, None
    return soucet, hody, "\033[1;31mPřekročen maximální počet hodů! Zkontrolujte kostku.\033[0m"
