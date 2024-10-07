def chat():
    name = ""
    alter = ""

    while True:
        user_input = input("Nachricht schreiben: ").lower().strip()

        if "mein name ist" in user_input:
            name = user_input.split("mein name ist ")[1].capitalize()
            print(f"Hallo {name}, schön dich kennenzulernen! Wie alt bist du?\n")

        elif "ich heiße" in user_input:
            name = user_input.split("ich heiße ")[1].capitalize()
            print(f"Hallo {name}, schön dich kennenzulernen! Wie alt bist du?\n")

        elif user_input in ["hallo", "hi", "hey", "hey ada"] and name:
            print(f"Hey {name}!\n")

        elif user_input in ["hallo", "hi", "hey", "hey ada"]:
            print("Hallo!\n")

        elif user_input in ["wie heißt du", "wie heißt du?", "was ist dein name", "was ist dein name?"] and name:
            print(f"Ich heiße Ada. Und dein Name ist {name} :)\n")

        elif user_input in ["wie heißt du", "wie heißt du?", "was ist dein name", "was ist dein name?"]:
            print("Ich heiße Ada. Und wie heißt du?\n")

        elif ("wie heiße ich" in user_input or "was ist mein name" in user_input) and name:
            print(f"Dein Name ist {name}, aber wie alt bist du denn?\n")

        elif "wie heiße ich" in user_input or "was ist mein name" in user_input:
            print("Ich weiß es noch nicht. Wie heißt du denn?\n")

        elif "wie alt bist du" in user_input:
            print("Ich bin erst 1 Tag alt, und du?\n")
                
        elif "ich bin" in user_input:
            parts = user_input.split("ich bin ")
            if len(parts) > 1:
                alter = parts[1]
                print(f"Wow, du bist {alter} Jahre alt? Ich bin erst 1 Tag alt :)\n")
            else:
                print("Ich weiß noch nicht. Wie alt bist du denn?\n")

        elif user_input in ["beenden", "stopp", "tschuess"]:
            exit_input = input("Willst du den Chat beenden?\n").strip().lower()
            if exit_input == "ja":
                print("Bye :)\n")
                break
            else:
                print("Ok, lass uns dann weiter reden :)\n")
chat()
