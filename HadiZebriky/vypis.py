import time

def vypis(text: str, delay=0.5, logovat: bool = True):
    print(text)
    time.sleep(delay)
    if logovat:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
