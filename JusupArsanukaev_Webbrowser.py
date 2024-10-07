import webbrowser

def openbrowser():
    url = "www.google.de"
    webbrowser.open(url)

if input("Schreibe browser hier: ").lower() == "browser":
    openbrowser()
