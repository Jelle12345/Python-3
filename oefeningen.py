contacten = {}

def main():
    keuzemenu = input("m: maak nieuw contact" + "\n" + "t: toon je contactenlijst" + "\n" + "s: stop je programma" + "\n" + "v: verwijder contact" + "\n" + "a: contact aanpassen" + "\n" + "o: contact opslaan")
    while keuzemenu != 's':
        if keuzemenu == 'm':
            nieuw_contact()
        elif keuzemenu == 't':
            toon_contacten()
        elif keuzemenu == 'v':
            verwijder_contact()
        elif keuzemenu == 'a':
            contact_aanpassen()
        elif keuzemenu == 'o':
            contact_opslaan()

def toon_contacten():
    print(contacten)
    main()

def verwijder_contact():
    verwijderen = input("noem het contact dat je wil verwijderen")
    del contacten[verwijderen]
    main()

def nieuw_contact():
    naam = input("geef een naam voor je contact")
    nummer = input("geef het telefoonnummer van je contact")
    print("dit is je contact " + naam + " " + nummer)
    contacten[naam] = nummer
    main()

def contact_aanpassen():
    print(contacten)
    aanpas = input("geef de naam van je contact dat je wil aanpassen")
    if aanpas in contacten:
        mobielnummer = input("geef je nieuwe telefoonnummer")
        contacten[aanpas] = mobielnummer;
        print(contacten)
        main()
    else: main()

def contact_opslaan():
    for contact in contacten:
        print(contact)
    with open("contact.txt","w+") as f:
        contacten1 = "".join(contacten)
        for contact in contacten:
            f.write(contact + " " + contacten[contact] + "\n")
        f.close()
        print("je lijst is opgeslagen in contact.txt")
        main()


main()