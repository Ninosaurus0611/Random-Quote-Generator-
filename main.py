# Random Quote Generator

# benodigde onderdelen:
# lijst met Quotes (miss veranderen als mogelijk naar vanuit quote word bestand)
# functie die een random quote print
#UI -> site of scherm dat zich opent om de quote te zien (miss met een knop)

#imports??:
#import json
#import random


#Selectie -> random quote, specifiek genre, of autheur
#random quote kiezen
#quote tonen

import random

categories = ["self improvement", "power"]


specifieke_categorie = input("Wil je een quote van een bepaalde categorie? (of druk Enter voor willekeurig): ").strip()
if specifieke_categorie == "ja" or "Ja":
    print(f"Dit zijn de categoriën", categories)
else:
    print("Oké, hier is een random quote")
    print(quote)

