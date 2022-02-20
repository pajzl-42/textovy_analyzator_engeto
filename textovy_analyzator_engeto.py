# vstupni promenne
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
oddelovac = 40 * "-"
TEXTS = {"1": '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

         "2": '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

         "3": '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''}

# vstup od uzivatele - login
user = input("LOGIN: ")
password = input("PASSWORD: ")

# kontrola uzivatelea hesla
if not user in users or not users[user] == password:
    print("Wrong login or password, terminating the program!")
    exit()

# privitani
print(oddelovac)
print(f"Login successfull, welcome {user}!")
print("We have three texts to be analyzed.")
print(oddelovac)

# vstup od uzivatele - cislo textu
cislo_textu = input("Please enter a number between 1 and 3: ")

# kontrola vstupu
if not cislo_textu.isnumeric() or not cislo_textu in TEXTS.keys():
    print("Wrong input, terminating the program!")
    exit()

# zpracovaní do podoby vhodne k analyze
text = TEXTS[cislo_textu]
slova = text.split()
upravena_slova = [slovo.strip(".,:") for slovo in slova]

# analyza
pocet_slov = len(upravena_slova)

title_slova = [slovo for slovo in upravena_slova if (slovo.istitle() or slovo.isupper()) and slovo.isalpha()]
pocet_title_slov = len(title_slova)

upper_slova = [slovo for slovo in title_slova if slovo.isupper()]
pocet_upper_slov = len(upper_slova)

lower_slova = [slovo for slovo in upravena_slova if slovo.islower() and slovo.isalpha()]
pocet_lower_slov = len(lower_slova)

cisla = [int(slovo) for slovo in upravena_slova if slovo.isnumeric()]
pocet_cisel = len(cisla)

soucet_cisel = sum(cisla)

histogram_delek = {}

for slovo in upravena_slova:
    if len(slovo) not in histogram_delek.keys():
        histogram_delek[len(slovo)] = 1
    else:
        histogram_delek[len(slovo)] += 1

delky_slov = list(histogram_delek.keys())
delky_slov.sort()

# vypis na obrazovku
print(oddelovac)
vypis_promennych = {pocet_slov: "words.",
                    pocet_title_slov: "titlecase words.",
                    pocet_upper_slov: "uppercase words.",
                    pocet_lower_slov: "lowercase words.",
                    pocet_cisel: "numeric strings.",
                    soucet_cisel: ""}

for key, value in vypis_promennych.items():
    print(f"There are {key} {value}") if key != soucet_cisel else print(
        f"The sum of all numbers equals to {soucet_cisel}.")
print(oddelovac)

hlavicka = "{: >5}{: ^20}{: <5}".format("LEN|", "OCCURANCES", "|NR:")
print(hlavicka)

for delka in delky_slov:
    hvezdy = "x" * histogram_delek[delka]
    print(f"{delka: >4}|{hvezdy: <20}|{histogram_delek[delka]}")
