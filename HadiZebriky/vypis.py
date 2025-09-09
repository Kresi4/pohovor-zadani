def vypis(text: str, logovat: bool = True):
    print(text)
    if logovat:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
