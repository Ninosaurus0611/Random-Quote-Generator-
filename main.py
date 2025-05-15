#miss nog doen??
#UI -> site of scherm dat zich opent om de quote te zien (miss met een knop)

# Random Quote Generator
#imports
import random
import json

#json file lezen
with open("quotes.json", 'r') as json_file:
    quotes = json.load(json_file)

#categorien toekennen
category = sorted({q['category'] for q in quotes})

#vraag user specifieke categorie of niet en print random quote of quote uit de categorie
specifieke_categorie_ja_of_nee = input("Wilt u een specifieke categorie? Zo wel, typ ja. Zo niet, druk Enter.\n")
if specifieke_categorie_ja_of_nee.strip().lower() == "ja":
    print("\nBeschikbare categorieën: ", "\n - " + "\n - ".join(category))
    gekozen_categorie = input("\nUit welke van de bovenstaande categoriën wilt u een quote zien?\n").strip().lower()

    gefilterde_quotes = [q for q in quotes if q['category'].lower() == gekozen_categorie]

    if gefilterde_quotes:
        quote = random.choice(gefilterde_quotes)
        print("\nQuote uit de categorie '{}':".format(gekozen_categorie))
        print('"' + quote["quote"] + '"', "-", quote["author"])

    else:
        print("\nGeen quotes gevonden voor de categorie '{}'. Controleer je invoer.".format(gekozen_categorie))

else:
    random_quote = random.choice(quotes)
    print("\nRandom Quote: ")
    print('"'+random_quote["quote"]+'"', "-" , random_quote["author"])
    print("Category:", random_quote["category"])


