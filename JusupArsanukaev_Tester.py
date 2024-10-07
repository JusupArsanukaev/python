import time

def frage_stellen(frage_nummer):
    print(f"Frage {frage_nummer}: Was ist die Antwort?")
    for sekunde in range(30, 0, -1):
        print(f"Verbleibende Zeit: {sekunde} Sekunden", end="\r")
        time.sleep(1)
    antwort = input("Gib deine Antwort ein: ")
    print(f"Antwort auf Frage {frage_nummer}: {antwort}\n")

def tester():
    for frage_nummer in range(1, 11):
        frage_stellen(frage_nummer)

tester()
