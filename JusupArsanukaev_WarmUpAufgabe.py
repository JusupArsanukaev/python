while True:
    user_input = input("Gib etwas ein: ").lower()

    if user_input == "hallo" or user_input == "hi" or user_input == "hey":
        print("Hey\n")

    elif user_input == "bist du echt?":
        print("Yep\n")

    elif user_input == "wie gehts?" or user_input == "wie geht es dir?":
        print("Gut, danke und dir?\n")

    elif user_input == "erzähle mir was" or user_input == "geschichte" or user_input == "erzählen":
        print("Ich kenne eine kleine Geschichte...\ndie ist aber zu lang für jetzt...\n")

    else:
        print("Pff, ich habe keine Zeit dafür\n")
