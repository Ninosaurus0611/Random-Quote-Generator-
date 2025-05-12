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
import json

with open("quotes.json", 'r') as json_file:
    quotes = json.load(json_file)

category = sorted({q['category'] for q in quotes})

print("Beschikbare categorieën:", category)

random_quote = random.choice(quotes)

print("\nRandom Quote: ")
print('"'+random_quote["quote"]+'"', "-" , random_quote["author"])
print("Category:", random_quote["category"])


