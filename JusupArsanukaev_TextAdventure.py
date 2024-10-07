import random
import time

class Ort:
    def __init__(self, name, richtungen=None):
        self.name = name
        self.richtungen = richtungen or {}

class Charakter:
    def __init__(self, name, start_ort):
        self.name = name                                                    # Name; wird zu Beginn des Spiels festgelegt
        self.health = 100                                                   # Spielerleben; bei 0 = schlechtes Ende  
        self.position = start_ort
        self.user_activ_missions = 0                                        # Begrenzung der aktiven Quests (auf 2 festgelegt; bleibt flexibel)
        self.user_reputation = 100                                          # Verhältnisse im Rahmen des gesamten Spieles: x > 75 - positiv; x < 75 und x > 50 - neutral; x < 50 - negativ
        self.user_ending_score = 50                                         # Spielende Bestimmungspunkte

        self.user_holzfaeller_quest_score = 0                               # Verhältnisse im Rahmen einer Quest (Holzfäller)
        self.holzfaeller_quest_done = 0                                     # Quest:    0 - unbestimmt; 1 - abgeschlossen; 2 - fehlgeschlagen
        self.holzfaeller_quest_status = 0                                   # Quest:    0 - unbestimmt; 1 - akzeptiert; 2 - verneint

        self.stress_quest_win = 0                                           # Ausgang des Spieles (Stress)
        self.user_stress_quest_score = 0                                    # Verhältnisse im Rahmen einer Quest (Stress)
        self.stress_quest_done = 0                                          # Quest:    0 - unbestimmt; 1 - abgeschlossen; 2 - fehlgeschlagen
        self.stress_quest_status = 0                                        # Quest:    0 - unbestimmt; 1 - akzeptiert; 2 - verneint

    def nach(self, richtung):
        if richtung in self.position.richtungen:
            neuer_ort = self.position.richtungen[richtung]
            self.position = neuer_ort
            print(f"Neuer Ort: {self.position.name}.\n")

            if (self.position.name == "Holzfäller" and 
                self.user_activ_missions < 2):
                self.holzfaeller_quest()

            if (self.position.name == "Variort" and
                self.user_activ_missions < 2 and
                self.holzfaeller_quest_done == 0 and
                self.holzfaeller_quest_status == 1):
                self.stress_quest()

        else:
            print("Du kannst nicht in diese Richtung gehen.")

    def status(self):
        print(f"\nCharakter: {self.name}")
        print(f"Gesundheit: {self.health} HP")
        print(f"Reputation: {self.user_reputation}")
        print(f"Position: {self.position.name.split()[0]}")

    def console(self):
        print(f"{self.user_holzfaeller_quest_score}")
        print(f"{self.holzfaeller_quest_done}")
        print(f"{self.holzfaeller_quest_status}")
        print(f"{self.stress_quest_win}")
        print(f"{self.user_stress_quest_score}")
        print(f"{self.stress_quest_done}")
        print(f"{self.stress_quest_status}")

#   Holzfäller Quest
    def holzfaeller_quest(self):
        if self.user_holzfaeller_quest_score == 0 and self.holzfaeller_quest_done == 0 and (self.holzfaeller_quest_status == 0 or self.holzfaeller_quest_status == 1):  #   Quest Reaktion + Quest abgeschlossen + Quest abgelehnt Prüfungen
            while True:
                antwort = input("Ein Holzfäller bemerkt dich und kommt mit einer Axt auf dich zu.\nWähle: X - stehen oder A - laufen?").lower()     #   Abfrage: Stehen oder Laufen
                if antwort == "x":                                                                                                                  #            Stehen: Ausgang
                    print("Du hast beschlossen, stehen zu bleiben.")
                    dialog = [
                        "\n--------------Dialog mit Holzfäller--------------\n",
                        "Jemand: Hey du!",
                        "...",
                        f"{self.name}: (innerer Monolog): Das war einer der Holzfäller.",
                        "Holzfäller: Hey, was machst du hier? Bist du taub?",
                        f"{self.name} Äh... ich war nur auf der Durchre...",
                        "Holzfäller: Durchreise? Denkst du, ich glaube dir?",
                        f"{self.name}: (innerer Monolog): Warum ist er so aggressiv?",
                        f"{self.name}: Ich weiß nicht, aber ich möchte keinen Ärger. Ich hätte ein paar Fragen, wenn...",
                        "Holzfäller: Wenn du schon hier bist, *tfuee*",
                        "Unterbrach mich der Holzfäller",
                        "Holzfäller: bring mir Kräuter westlich des Flusses Oxas.",
                        "Holzfäller: Dann werde ich deine Fragen beantworten.",
                        "Holzfäller: Schaffst du das?",
                        f"{self.name}: (innerer Monolog): Warum braucht er plötzlich die Kräuter?",
                        f"{self.name}: (innerer Monolog): Warum holt er die selbst nicht?",
                        f"{self.name}: (innerer Monolog): Das klingt verdächtig, aber vielleicht hilft es, wenn ich akzeptiere?",
                        "Holzfäller: Bist du da eingeschlafen?"
                    ]

                    for zeile in dialog:
                        print(zeile)
                        time.sleep(1)                                                                                                               #   Ersetzen auf 2

                    antwort = input("Der Holzfäller braucht deine Hilfe.\nWähle: X - akzeptieren A - ablehnen?").lower()                            #   Abfrage: Akzeptieren oder Ablehnen
                    if antwort == "x":                                                                                                              #            Akzeptieren: Ausgang
                        print("Neue Quest freigeschaltet: Finde Kräuter für den Holzfäller.")
                        self.user_holzfaeller_quest_score =+ 1                                                                                      #   Quest bereit für die nächste Reaktion
                        self.holzfaeller_quest_status =+ 1                                                                                          #   (Holzfäller) Quest: Akzeptiert

                        dialog = [
                        f"{self.name}: Ok, ich mache das!",
                        f"{self.name}: (innerer Monolog): Vielleicht bekomme ich dann die Antworten.\n"
                    ]

                        for zeile in dialog:
                            print(zeile)
                            time.sleep(1)                                                                                                           #   Ersetzen auf 2
                        break

                    elif antwort == "a":                                                                                                            #   Quest: Abgelehnt
                        self.holzfaeller_quest_status =+ 2                                                                                          #   (Holzfäller) Quest: Abgelehnt
                        self.user_reputation  =- 10                                                                                                 #   Einfluss auf das Ende
                        self.user_ending_score =- 5                                                                                                 #   Einfluss auf das Handeln des Spielers in der Welt
                        print("Quest abgelehnt")
                        break
                    else:
                        print("Ungültige Antwort.\nWähle: X - akzeptieren A - ablehnen?")

                elif antwort == "a":                                                                                                                #            Laufen: Ausgang
                    print("Du hast beschlossen, wegzulaufen.")
                    self.position = fluss
                    break
                else:
                    print("Ungültige Antwort.\nWähle: X - stehen oder A - laufen?")

        elif self.user_holzfaeller_quest_score == 1 and self.holzfaeller_quest_done == 0 and (self.holzfaeller_quest_status == 0 or self.holzfaeller_quest_status == 1):    #   Quest Reaktion + Quest abgeschlossen + Quest abgelehnt Prüfungen
            while True:
                antwort = input("Wieder die vollbeschäftigten Holzfäller.\nWähle: X - reden oder A - vorbeilaufen?").lower()                        #   Abfrage: Reden oder Vorbeilaufen
                if antwort == "x":                                                                                                                  #            Reden: Ausgang
                    print("Der selbe Holzfäller beginnt mit dir zu sprechen.")
                    
                    dialog = [
                        "\n--------------Dialog mit Holzfäller--------------\n",
                        "Holzfäller: Wieder du?",
                        "Holzfäller: Hast du mir die Kräuter geholt?",
                        f"{self.name}: Äh... noch nicht.",
                        "Holzfäller: Hmm, *tfuee* dann was machst du hier? Hol mir die Kräuter, du Sack.",
                        "..."
                    ]

                    for zeile in dialog:
                        print(zeile)
                        time.sleep(2)
                    break

                elif antwort == "a":                                                                                                                #            Vorbeilaufen: Ausgang
                    print("Du hast beschlossen, nach Osten zu laufen.")
                    self.position = hoehle
                    break
                else:
                    print("Ungültige Antwort.\nWähle: X - reden oder A - vorbeilaufen?")
        
        elif self.user_holzfaeller_quest_score == 2 and self.holzfaeller_quest_done == 0 and (self.holzfaeller_quest_status == 0 or self.holzfaeller_quest_status == 1):    #   Quest Reaktion + Quest abgeschlossen + Quest abgelehnt Prüfungen
            while True:
                antwort = input("Wieder die vollbeschäftigten Holzfäller.\nWähle: X - reden oder A - vorbeilaufen?").lower()                        #   Abrage: Reden oder Vorbeilaufen
                if antwort == "x":                                                                                                                  #           Reden: Ausgang
                    antwort = input(f"{self.name}: (innerer Monolog): Ok, soll ich ihm vertrauen und alles erzählen oder nicht?\nWähle: X - alles oder A - nicht alles?").lower()   #   Abfrage: Alles oder Teil
                    if antwort == "x":                                                                                                              #   Alles erzählen: Ausgang
                        print("Du hast dich entschieden, dem Holzfäller alles zu erzählen.")
                        ###
                        dialog = [
                            "\n--------------Dialog mit Holzfäller--------------\n",
                            "Holzfäller: Wieder du?",
                            "Holzfäller: Hast du mir die Kräuter geholt?",
                            f"{self.name}: Ja, ich habe die Kräuter geholt, aber du kriegst sie erst, wenn du mir alles erzählst!",
                            "...",
                            f"{self.name}: Wusstest du, dass ich überfallen wurde?",
                            "...",
                            f"{self.name}: Wer bist du? Sag mir deinen Namen oder...",
                            "Plötzlich schlug der Holzfäller seine Axt in den umgestürzten Baum neben ihm.",
                            "Ich weiß nicht, was mich bewegte, aber ich griff nach der Axt.",
                            f"{self.name}: WER BIST DU",
                            "Holzfäller: Gut, ich erzähle es dir. Aber gib mir erst die Kräuter.",
                            f"{self.name}: Hier. Fang an",
                            "Einen Moment lang schaute mich der Holzfäller misstrauisch an.",
                            "Holzfäller: Na gut, Durchreisender. *tfuee*",
                            "Spuckte er wütend auf einen gefällten Baum neben sich.",
                            "Martin: Ich bin Martin und das hier sind meine Jungs.", 
                            "Martin: Ich wusste, dass es gefährlich sein könnte",
                            "Martin: Wir arbeiten, wie du hoffentlich sehen kannst, im Auftrag Seiner Majestät.",
                            "Martin: Der alte Mann ist völlig durcheinander, nachdem er seine Tochter verloren hat.",
                            "Martin: Vorhin hat er uns befohlen, sein ganzes Reich bis nach Jermitz im Süden und Birtag im Westen zu blockieren.",
                            "Martin: Und das alles, damit seine Tochter, die schon lange tot ist, schneller gefunden wird. *tfuee*",
                            f"{self.name}: Das waren viele Informationen über diese Welt, aber ich weiß immer noch nicht was ich hier zu suchen habe",
                            "Martin: Du bist aus dem Dorf südlich von hier? Ich kenne hier alle, aber wie heißt du eigentlich?",
                            "Für einen Moment dachte ich, es wäre besser zu lügen, aber dann sagte ich",
                            f"{self.name}: Ja, und mein Name ist {self.name}.",
                            f"Martin: {self.name}? Hmm, seltsamer Name. Egal, ich muss jetzt an die Arbeit, danke nochmal.",
                            "Ich hatte noch Fragen, aber Martin machte sich mit schnellen Schritten an die Arbeit.",
                            "Vielleicht macht es Sinn das Dorf südlich von hier zu besuchen."
                        ]

                        for zeile in dialog:
                            print(zeile)
                            time.sleep(2)
                        break

                    elif antwort == "a":                                                                                                            #   Nur Teil erzählen: Ausgang
                        print("Du hast dich entschieden, dem Holzfäller nicht alles zu erzählen.")
                        self.user_stress_quest_score += 1                                                                                           # Anderer Start bei der Stress-Quest
                        dialog = [
                            "\n--------------Dialog mit Holzfäller--------------\n",
                            "Holzfäller: Wieder du?",
                            "Holzfäller: Hast du mir die Kräuter geholt?",
                            f"{self.name}: Ja, hier sind die Kräuter, die du haben wolltest.",
                            "Holzfäller: Uh danke. Ich hoffe, es gab keine Probleme?",
                            "...",
                            f"{self.name}: Nein. Alles war gu...",
                            "Holzfäller: Gut, gib mir die Kräuter.",
                            "Unterbrach mich der Holzfäller und zog seine Hand zu mir."
                            f"{self.name}: Hier. Darf ich nun fragen, wer ihr seid, wo wir sind und was hier passiert ist?",
                            "Einen Moment lang schaute mich der Holzfäller misstrauisch an.",
                            "Holzfäller: Na gut, Durchreisender. *tfuee*",
                            "Spuckte er wütend auf einen gefällten Baum neben sich.",
                            "Martin: Ich bin Martin und das hier sind meine Jungs.", 
                            "Martin: Wir arbeiten, wie du hoffentlich sehen kannst, im Auftrag Seiner Majestät.",
                            "Martin: Der alte Mann ist völlig durcheinander, nachdem er seine Tochter verloren hat.",
                            "Martin: Vorhin hat er uns befohlen, sein ganzes Reich bis nach Jermitz im Süden und Birtag im Westen zu blockieren.",
                            "Martin: Und das alles, damit seine Tochter, die schon lange tot ist, schneller gefunden wird. *tfuee*",
                            f"{self.name}: Das waren viele Informationen über diese Welt, aber ich weiß immer noch nicht was ich hier zu suchen habe",
                            "Martin: Du bist aus dem Dorf südlich von hier? Ich kenne hier alle, aber wie heißt du eigentlich?",
                            "Für einen Moment dachte ich, es wäre besser zu lügen, aber dann sagte ich",
                            f"{self.name}: Ja, und mein Name ist {self.name}.",
                            f"Martin: {self.name}? Hmm, seltsamer Name. Egal, ich muss jetzt an die Arbeit, danke nochmal.",
                            "Ich hatte noch Fragen, aber Martin machte sich mit schnellen Schritten an die Arbeit.",
                            "Vielleicht macht es Sinn das Dorf südlich von hier zu besuchen."
                        ]

                        for zeile in dialog:
                            print(zeile)
                            time.sleep(2)
                        break

                    else:
                        print("Ungültige Antwort.\nWähle: X - reden oder A - vorbeilaufen?")

                    self.user_holzfaeller_quest_score =+ 1
                    self.user_activ_missions =- 1
                    self.user_reputation =+ 10
                    print("Quest Abgeschlossen: Du hast dem Holzfäller geholfen.")
                    break

                elif antwort == "a":
                    print("Du hast beschlossen, nach Osten zu laufen.")
                    self.position = hoehle
                    break
                else:
                    print("Ungültige Antwort.\nWähle: X - reden oder A - vorbeilaufen?")

        elif self.user_holzfaeller_quest_score >= 0 and self.stress_quest_status == 2:                                                              #   Quest abgelehnt Prüfung
            print("Holzfäller: Geh weg hier! Du hast hier nichts zu suchen!")



    def stress_quest(self):
        if self.user_holzfaeller_quest_score == 1 and self.stress_quest_win == 0:      #ANDERE QUEST: KRÄUTERSAMMLUNG INTEGRATION
            while True:
                antwort = input("Du stehst auf einer großen Wiese. Hier würden die Kräuter für den Holzfäller bestimmt stehen.\nWähle: X - Kräuter mitnehmen oder A - lassen und zurück?").lower()
                if antwort == "x":
                    print("Du hast beschlossen, die Kräuter mitzunehmen.")
                    time.sleep(2)
                    print(f"{self.name}: Ach, ich weiß nicht, warum ich das mache, anstatt den Ausgang zu suchen!")
                    time.sleep(2)
                    print("Plötzlich rennt jemand auf dich zu.")
                    time.sleep(2)
                    fight_guess(self)

                elif antwort == "a":
                    print("Du hast beschlossen, wegzulaufen.")
                    time.sleep(1)
                    print(f"{self.name}: Ich suche nach dem Ausgang.")
                    time.sleep(1)
                    print(f"{self.name}: Keine Zeit für diesen Schwachsinn. Ich sollte zum Fluss gehen, vielleicht finde ich dort etwas.")
                    self.position = fluss
                    self.user_reputation =- 10
                    break
                else:
                    print("Ungültige Antwort.\nWähle: X - Kräuter mitnehmen oder A - lassen und zurück?")

    def stress_quest2(self):
            if self.stress_quest_win == 1:
                self.user_reputation =+ 10
                self.user_stress_quest_score =+ 1
                print("\nQuest Update: Du hast die Kräuter für den Holzfäller gefunden.")
                time.sleep(1)

                dialog = [
                    "\n--------------Dialog mit dem besiegten Gegner--------------\n",
                    "Der besiegte Gegner lag regungslos am Boden und ich dachte, ich sollte ihm Fragen stellen.",
                    f"{self.name}: Warum hast du mich angegriffen?",
                    "Besiegter Gegner: Weil ich das immer mache. Das ist mein Schicksal.",
                    f"{self.name}: Ich verstehe nicht. Wer bist du? Was ist das für ein Ort?",
                    f"Besiegter Gegner: Keine Sorgen {self.name}, wir werden noch die Zeit haben, darüber zu reden.",
                    "Besiegter Gegner: Aber bedenke eines, vertraue niemandem!",
                    "Seine letzten Worte vor seinem Verschwinden jagten mir einen Schauer über den Rücken.",
                    "Woher kennt er meinen Namen? Und warum hat er mich angegriffen?",
                    "Ich hatte viele Fragen, aber er verschwand und wie er das gemacht hat, war eine meiner Fragen.",
                    "Ich sollte weitergehen, vielleicht erzählt mir der Holzfäller mehr."
                    ]

                for zeile in dialog:
                    print(zeile)
                    time.sleep(2)

            elif self.stress_quest_win == 0:
                self.user_reputation =- 10
                self.user_stress_quest_score =+ 1
                print("\nQuest Update: Quest fehlgeschlagen!")

#SPIEL 1
def fight_guess(self):
    meinezahl = random.randint(1, 100)
    versuche = 5

    print(f"Es ist ein Kampf um das Leben\n")
    print(f"\n--------------\n\n   Errate die Zahl des Gegners zwischen 1 und 100, um zu gewinnen. Du hast 5 Versuche.\n\n--------------\n")
    print(f"Cheats: {meinezahl}\n")

    while versuche > 0:
        deinezahl = int(input("Was ist deine Zahl: ")) 

        if deinezahl < meinezahl:
            print(f"\nMeine Zahl ist größer als {deinezahl}\n")
        elif deinezahl > meinezahl:
            print(f"\nMeine Zahl ist kleiner als {deinezahl}\n")
        else:
            print(f"\nDu hast gewonnen! Meine Zahl war {meinezahl}\n")
            self.stress_quest_win =+ 1
            self.stress_quest2()
            break

        versuche -= 1
        if versuche > 0:
            print(f"Du hast noch {versuche} Versuche übrig\n")
        else:
            input(f"Du hast verloren! Meine Zahl war {meinezahl}")
            self.stress_quest2()
            break

# ORTE
berg = Ort("Berg")
dorf = Ort("Dorf")
easter_egg = Ort("EasterEgg")
falle = Ort("Falle")
fluss = Ort("Fluss")
hoehle = Ort("Höhle")
holzfaeller = Ort("Holzfäller")
kampf = Ort("Kampf")
schloss = Ort("Schloss")
start = Ort("Start")
truhe = Ort("Truhe")
wald1 = Ort("Wald1")
wald2 = Ort("Wald2")
wald3 = Ort("Wald3")
wald4 = Ort("Wald4")
wald5 = Ort("Wald5")
variort = Ort("Variort")
wolfe = Ort("Wölfe")

# RICHTUNGEN
start.richtungen = {"norden": fluss, "osten": wald1, "süden": wald2, "westen": kampf}
berg.richtungen = {"norden": schloss, "süden": fluss, "westen": falle}
dorf.richtungen = {"norden": wolfe, "osten": wald5, "westen": wald4}
easter_egg.richtungen = {"westen": wald4}
falle.richtungen = {"osten": berg, "süden": kampf}
fluss.richtungen = {"norden": berg, "osten": holzfaeller, "süden": start, "westen": variort}
hoehle.richtungen = {"westen": berg}
holzfaeller.richtungen = {"westen": fluss}
kampf.richtungen = {"norden": falle, "osten": start}
schloss.richtungen = {"norden": hoehle}
truhe.richtungen = {"süden": wald3}
variort.richtungen = {"osten": fluss}
wald1.richtungen = {"norden": holzfaeller, "süden": wolfe, "westen": start}
wald2.richtungen = {"norden": start, "osten": wald4, "süden": dorf, "westen": start}
wald3.richtungen = {"norden": truhe, "süden": wald2}
wald4.richtungen = {"norden": hoehle, "süden": wald5, "westen": wald2}
wald5.richtungen = {"norden": wald4, "osten": dorf, "westen": easter_egg}
wolfe.richtungen = {"norden": wald1}

# SPIELER NAME
user_name = input("Begrüßen\n\nWie heißt du?\n").strip().capitalize()
charakter = Charakter(user_name, start)

# SPIEL LOOP
while True:
    aktion = input("N (Norden), O (Osten), S (Süden),  W (Westen) oder status eingeben: ").lower()

    if aktion == "status":
        charakter.status()
    elif aktion == "console":
        charakter.console()
    elif aktion in ["n", "s", "o", "w"]:
        richtungs_mapping = {"n": "norden", "s": "süden", "o": "osten", "w": "westen"}
        charakter.nach(richtungs_mapping[aktion])
    elif aktion == "beenden":
        print("Spiel beendet.")
        break
    else:
        print("Ungültige Eingabe.")
