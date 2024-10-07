import random

counter = 0

def wuerfeln(counter):
    if counter < 5:
        zufallszahl = random.randint(1, 6)
        print("Die Zufallszahl ist: " + str(zufallszahl))
        counter += 1
        print("Anzahl der Würfe: " + str(counter))
        wuerfeln(counter)

        input("")
        
wuerfeln(0)
