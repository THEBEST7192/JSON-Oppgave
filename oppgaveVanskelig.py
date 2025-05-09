import json # Importerer bibloteket for json
import random # Importerer biblotek for valg av tilfeldige ting
from termcolor import colored # Importerer biblotek for farger

# Oppgave 1
with open('jokes.json', 'r') as file: # Åpner jokes.json
    vitser = json.load(file)

# Set to track used jokes
used_jokes = set()

# Oppgave 2
print("\nOppgave 2") # Skriver ut den første vitsen i json filen
print(colored("Vits 1: ", "white") + colored(f"{vitser['jokes'][0]['joke']}", "green")) # Tallene starter på 0 og ikke 1 det er derfor det er derfor det står 0 istedenfor 1

# Oppgave 3
print("\nOppgave 3") # Skriver ut alle vitser
for i, vits in enumerate(vitser['jokes'], start=1): # Går gjennom alle vitsene
    print(colored(f"Vits {i}: ", "white") + colored(f"{vits['joke']}", "green")) # Printer vitsen

# Oppgave 4
print("\nOppgave 4")
# Skriver ut en tilfeldig vits
vits=random.randint(0,10)
print(colored(f"Vits {vits+1}: ", "white") + colored(f"{vitser['jokes'][vits]['joke']}", "green")) # Printer en tilfeldig vits

# Oppgave 5
while True:  # Løkke som kjører helt til brukeren velger å avslutte
    # Meny for valg av ting
    print("\nMeny for valg av ting")
    print("1. Vis en tilfeldig vits")
    print("2. Vis en tilfeldig vits som ikke har blitt vist før")        
    print("3. Vis en bruker definert vits")
    print("4. Skrive ut alle vitser") 
    print("5. Vis forklaring av vits")  
    print("6. Avslutt programmet")


    # Spør bruker hva dem vil gjøre
    valg=input("\nVelg hva du hvil gjøre: ")

    if valg=="1": # Vis et tilfeldig vits
        vits=random.randint(0,10) # Setter vits til en tilfeldig verdi (vits)
        print(colored(f"Vits {vits+1}: ", "white") + colored(f"{vitser['jokes'][vits]['joke']}", "green")) # Printer en tilfeldig vits


    elif valg=="2": # Vis en tilfeldig vits som ikke har blitt vist før
        available_jokes = [i for i in range(len(vitser['jokes'])) if i not in used_jokes]
        if not available_jokes:
            print(colored("Alle vitser har blitt vist. Vil du starte på nytt?", "yellow"))
            if input(colored("Trykk q for å starte på nytt: ")).lower() in ("q", "quit"):
                used_jokes.clear()
                continue
            else:
                continue
        
        vits = random.choice(available_jokes)
        used_jokes.add(vits)
        print(colored(f"Vits {vits+1}: ", "white") + colored(f"{vitser['jokes'][vits]['joke']}", "green")) # Printer en tilfeldig vits



    elif valg=="3": # Vis en bruker definert vits
        try:
            index = int(input("Velg hvilken vits du vil vise (1-11): ")) - 1
            if 0 <= index < len(vitser['jokes']):
                print(colored(f"Vits {index+1}: ", "white") + colored(f"{vitser['jokes'][index]['joke']}", "green"))
            else:
                raise ValueError
        except (ValueError, KeyError):
            print(colored("Ugyldig valg. Velg et tall mellom 1 og 11.", "red"))


    elif valg=="4": # Skriver ut alle vitser
        for i, vits in enumerate(vitser['jokes'], start=1):
            print(colored(f"Vits {i}: ", "white") + colored(f"{vits['joke']}", "green"))


    elif valg=="5": # Vis forklaring av vits
        with open('jokesExplanation.json', 'r') as file:
            whyHaHa = json.load(file)
        vits = input("Velg hvilken vits du vil vise forklaringen til (1-11): ")
        try:
            index = int(vits) - 1
            if 0 <= index < len(vitser['jokes']):
                print(colored(f"Vits {vits}: ", "white") + colored(f"{whyHaHa['jokes'][index]['joke']}", "green"))
                print(colored("Forklaring: ", "white") + colored(f"{whyHaHa['jokes'][index]['whyHaHa']}", "yellow"))
            else:
                print(colored("Ugyldig valg. Velg et tall mellom 1 og 11.", "red"))
        except (ValueError, KeyError):
            print(colored("Ugyldig valg. Velg et tall mellom 1 og 11.", "red"))


    elif valg in ("6", "exit", "Exit", "stop", "Stop"): # Avslutter programmet
        print(colored("Avslutter programmet", "red"))
        exit()


    else: # Starter på nytt hvis bruker skriver noe annet enn 1-6
        print(colored("Ugyldig valg. Vennligst velg 1-6.", "red"))