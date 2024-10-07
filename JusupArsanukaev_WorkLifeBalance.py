import webbrowser
import time
import random

def timer(seconds, url):
    pausenanzahl = 0
    konzentriertearbeitszeit = 0

    while True:
        for sekunde in range(seconds, 0, -1000):
            stunden = sekunde // 3600
            minuten = (sekunde % 3600) // 60
            sekunden = sekunde % 60
            print(f"Verbleibende Zeit bis zur Pause: {stunden} Stunden, {minuten} Minuten, {sekunden} Sekunden! ", end="\r")
            time.sleep(1)

        webbrowser.open(url)
        print(f"\nTimer kurz pausiert!\n")

        pausenanzahl += 1
        if pausenanzahl == 1:
            print(f"Du hast bisher eine Pause gemacht!\n")
        else:
            print(f"Du hast insgesamt {pausenanzahl} Pausen gemacht und")

        konzentriertearbeitszeit += 1.5
        if konzentriertearbeitszeit == 1.5:
            print(f"und damit anderthalb Stunden konzentriert gearbeitet!\n")
        elif konzentriertearbeitszeit == 3.0:
            print(f"und damit 3 Stunden konzentriert gearbeitet! Bist du schon müde?\n")
        elif konzentriertearbeitszeit == 4.5:
            print(f"und damit 4 Stunden und 30 Minuten konzentriert gearbeitet! WOW!\n")
        elif konzentriertearbeitszeit == 6.0:
            print(f"und damit 6 Stunden konzentriert gearbeitet! Ok, langsam bin ich selbst vom Zählen müde!\n")
        elif konzentriertearbeitszeit == 7.5:
            print(f"und damit 7 Stunden und 30 Minuten konzentriert gearbeitet! *Gähnen Geräusche*\n")
        elif konzentriertearbeitszeit == 9.0:
            print(f"und damit 9 Stunden konzentriert gearbeitet! 9 STUNDEN?! DU HAST 9 STUNDEN GESCHAFFT?! BRAVO!\n")
        else:
            print(f"damit {konzentriertearbeitszeit} Stunden konzentriert gearbeitet! Nah, ich gehe schlafen! Jetzt ohne mich!\n")

        spielfrage()

def spielfrage():
    while True:
        userinput = input(f"Willst du etwas spielen (ja/nein)?\n").strip().lower()
        if userinput in ["ja", "yep", "yes", "yeah"]:
            zahlenraten()
            break
        elif userinput in ["nein", "no", "nah"]:
            print(f"\nTimer wird fortgesetzt!\n")
            return
        else:
            print(f"\nWas heißt denn {userinput}? Sag bitte ja oder nein!\n")


def zahlenraten():
    meinezahl = random.randint(1, 100)
    versuche = 6

    print(f"\n---------------------------------------------------------------------\n\n   Errate meine Zahl zwischen 1 und 100. Du hast genau 6 Versuche.\n\n---------------------------------------------------------------------\n")
    print(f"Cheats: {meinezahl}\n")

    while versuche > 0:
        deinezahl = int(input("Was ist deine Zahl: ")) 

        if deinezahl < meinezahl:
            print(f"\nMeine Zahl ist größer als {deinezahl}\n")
        elif deinezahl > meinezahl:
            print(f"\nMeine Zahl ist kleiner als {deinezahl}\n")
        else:
            print(f"\nDU HAST MEINE ZAHL ERRATEN! Meine Zahl war {meinezahl} :)\n")
            return

        versuche -= 1
        if versuche > 0:
            print(f"Du hast noch {versuche} Versuche übrig\n")
        else:
            input(f"Du hast verloren! Meine Zahl war {meinezahl} :(\n")

def openbrowser():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
    timer(5400, url)

openbrowser()
