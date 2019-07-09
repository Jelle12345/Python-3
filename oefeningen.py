contacten = {}

def main():
    menu()
    keuze = input("Maak een keuze")
    while keuze != 's':
        if keuze == 'm':
            nieuw_contact()
        elif keuze == 't':
            toon_contacten()
        elif keuze == 'v':
            verwijder_contact()
        elif keuze == 'a':
            contact_aanpassen()
        elif keuze == 'o':
            contact_opslaan()
        menu()
        keuze = input("Maak een keuze")

def menu():
    print("m: maak nieuw contact")
    print("t: toon je contactenlijst")
    print("s: stop je programma")
    print("v: verwijder contact")
    print("a: contact aanpassen")
    print("o: contact opslaan")

def toon_contacten():
    print("-"*10)
    print("Uw contacten: ")
    print("-"*10)
    print('\n'.join("{}: {}".format(k, v) for k, v in contacten.items()))
    print("\n"*6)

def verwijder_contact():
    verwijderen = input("noem het contact dat je wil verwijderen")
    del contacten[verwijderen]

def nieuw_contact():
    naam = input("geef een naam voor je contact")
    nummer = input("geef het telefoonnummer van je contact")
    print("dit is je contact " + naam + " " + nummer)
    contacten[naam] = nummer

def contact_aanpassen():
    print("-"*10)
    print("Uw contacten: ")
    print("-"*10)
    print('\n'.join("{}: {}".format(k, v) for k, v in contacten.items()))
    print("\n"*6)
    aanpas = input("geef de naam van je contact dat je wil aanpassen")
    if aanpas in contacten:
        mobielnummer = input("geef je nieuwe telefoonnummer")
        contacten[aanpas] = mobielnummer;
        print("-" * 10)
        print("Uw contacten: ")
        print("-" * 10)
        print('\n'.join("{}: {}".format(k, v) for k, v in contacten.items()))
        print("\n" * 6)

def contact_opslaan():
    for contact in contacten:
        print("-" * 10)
        print("Uw contacten: ")
        print("-" * 10)
        print('\n'.join("{}: {}".format(k, v) for k, v in contacten.items()))
        print("\n" * 6)
    with open("contact.txt","w+") as f:
        contacten1 = "".join(contacten)
        for contact in contacten:
            f.write(contact + " " + contacten[contact] + "\n")
        f.close()
        print("je lijst is opgeslagen in contact.txt")

main()