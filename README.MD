# JSON Oppgave

Dette er et python-prosjekt som demonstrerer bruk av JSON-filer for å lagre og manipulere vitser. Programmet lar brukeren:
- Se en tilfeldig vits
- Velge en spesifikk vits
- Se alle vitser
- Vis forklaring av vits
- Avslutte programmet

Filstruktur:
- `oppgaveLett.py`: Hovedprogram som inneholder menysystem og vitsfunksjonalitet (bruker justJokes.json)
- `oppgaveVanskelig.py`: Hovedprogram som inneholder menysystem og vitsfunksjonalitet (bruker jokes.json)
- `justJokes.json`: JSON-fil som inneholder samlingen av vitser formatert som: `"n": "Vits tekst"`
- `jokes.json`: JSON-fil som inneholder samlingen av vitser formatert som: `"jokes": [{"id": "n", "joke": "Vits tekst"}]`
- `jokesExplanation.json`: JSON-fil som inneholder forklaring av hvorfor hver vits er morsom

Krav:
- En eller annen python versjon, men jeg brukte 3.13

Bruk:
Kjør programmet ved å skrive følgende kommando i terminalen:
```bash
python oppgaveLett.py
```
eller
```bash
python oppgaveVanskelig.py
```

Bruk menyen for å velge en av disse:
1. Vis en tilfeldig vits
2. Vis en bruker definert vits (velg tall mellom 1-11)
3. Skriv ut alle vitser
4. Vis forklaring av vits
5. Avslutt programmet