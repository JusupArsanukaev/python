import random

counter = 0
max_wuerfe = 30

while counter < max_wuerfe:
    zufallszahl = random.randint(1, 6)
    print("Die Zufallszahl ist: " + str(zufallszahl))
    counter += 1
    print("Anzahl der Würfe: " + str(counter))

input("")