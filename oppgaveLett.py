import json # Importerer bibloteket for json
import random # Importerer biblotek for valg av tilfeldige ting
import colored # Importerer biblotek for farger

# Oppgave 1
with open('justJokes.json', 'r') as file: # Åpner justjokes json og lagrer det som ne variabel
    vitser = json.load(file)

# Oppgave 2
print("\nOppgave 2") # Skriver ut den første vitsen i json filen
print(vitser["1"])

# Oppgave 3
print("\nOppgave 3") # Skriver ut alle vitser
for vits in vitser: # Går gjennom alle vitsene, vits er en variabel og er vitsen du vil si
                    # vitser er en variabel og er json filen
    print(vitser[vits]) # Printer vitsen


# Oppgave 4
print("\nOppgave 4")
# Skriver ut en tilfeldig vits
vits=random.randint(1,10)
#print(vits)
print(vitser[str(vits)]) # Printer en tilfeldig vits

# Oppgave 5
while True:  # Løkke som kjører helt til brukeren velger å avslutte
    # Meny for valg av ting
    print("\nMeny for valg av ting")
    print("1. Vis en tilfeldig vits")
    print("2. Vis en bruker definert vits")
    print("3. Skrive ut alle vitser")   
    print("4. Avslutt programmet")

    # Spør bruker hva dem vil gjøre
    valg=input("\nVelg hva du hvil gjøre: ")

    if valg=="1": # Vis en tilfeldig vits
        vits=random.randint(1,10) # Setter vits til en tilfeldig verdi (vits)
        print(vitser[str(vits)])

    elif valg=="2": # Vis en bruker definert vits
        vits=input("Velg hvilken vits du vil vise (1-11): ") # Setter vits til en bruker definert verdi (vits)
        try:
            print(vitser[str(vits)])
        except KeyError: # Hvis bruker skriver noe annet enn 1-11 blir det ikke noen problemer
            print("Ugyldig valg. Velg et tall mellom 1 og 11.")

    elif valg=="3":
        for vits in vitser: # Skriver ut alle vitser
            print(vitser[vits])

    elif valg=="4": # Avslutter programmet
        print("Avslutter programmet")
        exit()
    
    else:
        print("Ugyldig valg. Vennligst velg 1-4.")
