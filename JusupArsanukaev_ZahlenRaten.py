import random

def zahlenraten():
    meinezahl = random.randint(1, 100)
    versuche = 6

    print(f"\n---------------------------------------------------------------------\n\n   Errate meine Zahl zwischen 1 und 100. Du hast genau 6 Versuche.\n\n---------------------------------------------------------------------\n")
    print(f"Cheats: {meinezahl}\n")

    while versuche > 0:
        deinezahl = int(input("Was ist deine Zahl: ")) 

        if deinezahl < meinezahl:
            print(f"\nMeine Zahl ist großer als {deinezahl}\n")
        elif deinezahl > meinezahl:
            print(f"\nMeine Zahl ist kleiner als {deinezahl}\n")
        else:
            input(f"\nDU HAST MEINE ZAHL ERRATEN! Mein Zahl war {meinezahl} :)\n")
            break

        versuche -= 1
        if versuche > 0:
            print(f"Du hast noch {versuche} Versuche übrig\n")
        else:
            input(f"Du hast verloren! Mein Zahl war {meinezahl} :(\n")
            break

zahlenraten()
