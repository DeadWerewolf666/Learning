"""
#zobrazení_datoveho_typu
a = 6
print("pro číslo", a ,"je datový typ", type(a))
a = 6.0
print("pro číslo", a ,"je datový typ", type(a))

#operátory
print("operátor % je zbytek po celočíselném dělení: (10 % 6) =", (10 % 6))
print("operátor / je dělení: (10 / 6) =", (10 / 6))
print("operátor * je násobení: (10 * 6) =", (10 * 6))
print("operátor ** je mocnina: (10 ** 6) =", (10 ** 6))
print("operátor + je sčítání: (10 + 6) =", (10 + 6))
print("operátor - je odečítání: (10 - 6) =", (10 - 6))

#absolutní_hodnota
print("abosolutní hodnota z čísla -2 je:", abs(-2))

#pravdivostní_hodnoty
pravdicka = True
print("pravdivost hodnota True je:", pravdicka)
print("negace hodnoty True je:", not(pravdicka))
print("True and False je:", pravdicka and not(pravdicka))
print("True or False je:", pravdicka or not(pravdicka))

#práce_řetězci
retez = "\moje\notes"
print("Výpis řetězce bez opravy", retez)
retez = r"\moje\notes"
print("Výpis řetězce s opravou", retez)

#procvicovani_1
print("\nNaučili jsme se mnoho věcí o stringu")
print("Spojení"+" "+"stringu"+" "+"děláme"+" "+"pomocí"+" "+"znaménka"+" "+'"+"')
print("Také jsme použili print('nějaý text')")
print("První řádek\nDruhý řádek se dělá pomocí lomíta a n")

#procvičování_2
city = input("\nKde bydlíš\n")
print("Bydlím ve městě " + city)

#procvičování_3
print("\nVýtejte v aplikaci na generování vtipných jmen")
name = input("Jké je tvé křestní jméno?\n")
description = input("jaká je tvá typická vlastnost? Napiš ji s velkým písmenem.\n")
print("Tvoje jméno je " + name + " " + description)

#procvičování_4
number = input("Napište dvoumístné číslo:\n")
result = int(number[0]) + int(number[1])
print(result)

#procvičování_5
height = input("Zadejte svou výšku v m\n")
wight = input("Zadejte svou váhu v kg\n")
result = (float(wight)/(float(height)**2))
print("Vaše BMI je:", round(result, 2))

#procvičování_6
age = input("Kolik je vám let?\n")
years = 90 - int(age)
months = years * 12
weeks = years * 52
days = years * 365
print(f"Zbývá vám {years} let\n{months} měsíců\n{weeks} týdnů\n{days} dnů")

#procvičování_7
print("Vítejte v kalkulátoru na výpočet plateb")
pay = int(input("Kolik míte celkem zapltati?\n"))
proc = int(input("Kolik chcete dát propitného (v %)\n"))
count = int(input("Mezi kolik lidí se má rozdělit částka?\n"))
result = ((pay + (pay * (proc*0.01)))/count)
result = "{:.2f}".format(result)
print(f"Každý člověk, by měl zaplatit {result} kč")

#procvčování_8
age = int(input("Jaký je váš věk?\n"))
if age >= 18:
    print("Jste dospělý")
else:
    print("Ještě nejste dospělý")

#procvičování_9
status = input("Jste student? (ano/ne)\n")
if status == "ano":
    print("Cena lístku je 120Kč")
else:
    print("Cena lístku je 150Kč")

#procvičování_10
print("Výtejte na horské dráze")
height = int(input("Jaká je vaš výška v cm\n"))
cost = 0
if height >= 87:
    print("Můžete jet na horské dráze.")
    age = int(input("Kolik vám je let?\n"))
    if age >= 18:
        print("Cena lístku je 150Kč")
        cost += 150
    elif age > 12:
        print("Cena lístku je 100Kč")
        cost += 100
    else:
        print("Cena lístku je 50Kč")
        cost += 50
    photo = input("Chcete fotku? (ano/ne)\n")
    if photo == "ano":
        cost += 40
    print(f"Celková cena je {cost}Kč")
else:
    print("Omlouváme se, ale na horské dráze jet nemůžete.")

#procvičování_11
height = input("Zadejte svou výšku v m\n")
wight = input("Zadejte svou váhu v kg\n")
result = (float(wight)/(float(height)**2))
if result < 18.5:
    print(f"Vaše BMI je: {round(result, 2)}, máte podváhu")
elif result >= 18.5 and result <= 29.9:
    print(f"Vaše BMI je: {round(result, 2)}, jste v normálu")
elif result >= 25.0 and result <= 29.9:
    print(f"Vaše BMI je: {round(result, 2)}, jste nadváhu")
elif result >= 30.0 and result <= 34.9:
    print(f"Vaše BMI je: {round(result, 2)}, jste obézní")
else:
    print(f"Vaše BMI je: {round(result, 2)}, jste extrémě obézní")

#procvičování_12
year = int(input("Zadej rok\n"))
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"{year} je přestupný rok.")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} je přestupný rok.")
else:
    print(f"{year} není přestupný rok.")

#procvičování_13
cost = 0
size = input("Zvolte veliost pizzy (S, M, L).\n")

if size == "S":
    print("Částka činí 100Kč")
    cost += 100
elif size == "M":
    print("Částka činí 150Kč")
    cost += 150
else:
    print("Částka činí 200Kč")
    cost += 200

feferony = input("Chcete feferonky? (ano/ne)\n")

if feferony == "ano":
    if size == "S":
        cost += 20
    else:
        cost += 30

cheese = input("Chcete sýr? (ano/ne)\n")

if cheese == "ano":
    cost += 15

print(f"Celková čáska činí {cost}Kč")

#provičování_14
print(''' 
|        |  ------------\    ,---.  /------------  |        |
|        |   ---------.  `-./  "\.-'  .---------   |        |
|  ,--.  |     --------\   .         /--------     |  ,--.  |
| ( >< ) |        ------`-.|      .-'------        | ( >< ) |
|  `--'  |             ---/ `/"\  \---             |  `--'  |
|      . |                `//_-_\\'         Ojo 98 |        |
| : .  ! |                (.'   ',)                | . : . :|
| ! ! .| |                                         | : | ! .|
| |_| ;|_|                  .                      |_| !_| !|
`-' `-^'                     \o                      `-' `-^'
           \__________________T>_________________/
           `-=--=--=--=--=--=---=--=--=--=--=--=-'
            ] _] _] _] _] _] _L] _] _] _] _] _] _
           `-------------------------------------'
           `u---u---u---u---u---u---u---u---u---u'
''')

#provičování_15
import random
import math

num = math.ceil(random.randint(0, 1))

if num == 0:
    print("Halava")
else:
    print("Orel")

#provičování_16
set1 = ["©️", "©️", "©️"]
set2 = ["©️", "©️", "©️"]
set3 = ["©️", "©️", "©️"]
all_sets = [set1, set2, set3]
print(f"{set1}\n{set2}\n{set3}")
position = input("Zadejte souřadnice ")
pos1 = int(position[0])
pos2 = int(position[1])
all_sets[pos1][pos2] = "X"
print(f"{set1}\n{set2}\n{set3}")

#provičování_17
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

all_list = [rock, paper, scissors]

random_choice = random.randint(0, 2)
choice = int(input("Co si vyberete? Napište 0 pokud kámen, 1 pro papír a 2 pro nůžky "))

pc_pic = all_list[random_choice]
us_pic = all_list[choice]

print(f"Uživatel si vybral:\n{us_pic}")
print(f"Počítač si vybral:\n{pc_pic}")

if random_choice == 0 and choice == 1:
    print("Uživatel vyhrál, Počítač prohrál")
elif random_choice == 0 and choice == 2:
    print("Uživatel prohrál, Počítač vyhrál")
elif random_choice == 1 and choice == 0:
    print("Uživatel prohrál, Počítač vyhrál")
elif random_choice == 1 and choice == 2:
    print("Uživatel vyhrál, Počítač prohrál")
elif random_choice == 2 and choice == 0:
    print("Uživatel vyhrál, Počítač prohrál")
elif random_choice == 2 and choice == 1:
    print("Uživatel prohrál, Počítač vyhrál")
elif random_choice == choice:
    print("Remíza")

#provičování_18
num = input("Vložte výšky lidí oddělené čárkou a mazerou\n")
height = num.split(", ")
count = 0
for i in height:
     count += int(i)
final_count = (count / len(height))
print(f"Průměrná výška je: {final_count}")

#provičování_19
score = input("Zadejte score jednotlivých studentů oddělené čárkou a mazerou:\n")
score_list = score.split(", ")
min = int(score_list[0])
max = int(score_list[0])
for i in score_list:
     if int(i) > max:
          max = int(i)
     if int(i) < min:
          min = int(i)
print(f"min: {min}\nmax: {max}")
print(type(min))

#provičování_20
suma = 0
for i in range(0, 101, 2):
     suma += i
print(f"suma: {suma}")

#provičování_21
for i in range(1, 101):
     if i % 3 == 0 and i % 5 != 0:
          print("Fizz")
     elif i % 3 != 0 and i % 5 == 0:
          print("Buzz")
     elif i % 3 == 0 and i % 5 == 0:
          print("Fizz Buzz")
     else:
          print(i)

#provičování_22
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

let = int(input("Kolik písmen chcete mít ve svém heslu"))
num = int(input("Kolik čísel chcete mít ve svém heslu"))
spec = int(input("Kolik znaků chcete mít ve svém heslu"))
pass_list = []
password = ""
for i in range(let):
    pass_list.append(letters[random.randint(0, len(letters) - 1)])
for i in range(num):
    pass_list.append(numbers[random.randint(0, len(numbers) - 1)])
for i in range(spec):
    pass_list.append(special_char[random.randint(0, len(special_char) - 1)])


translator = ""
for i in range(0, 10):
    ran_i_1 = random.randint(0, len(pass_list) - 1)
    ran_i_2 = random.randint(0, len(pass_list) - 1)

    translator = pass_list[ran_i_2]
    pass_list[ran_i_2] = pass_list[ran_i_1]
    pass_list[ran_i_1] = translator

random.shuffle(pass_list)
for i in pass_list:
    password += i

print(password)

#provičování_23
import math

def walls_color(height, weight):
    res = (height * weight) / 5
    result = math.ceil(res)
    print(f"Budete potřebovat {result} plechovek barvy")

walls_color(height=int(input("Výška zdi: ")), weight=int(input("Šířa zdi: ")))

#provičování_24
def prvocisco(number):
    if number % 2 == 0 and number != 2 or number % 3 == 0 and number != 3 or number % 5 == 0 and number != 5:
        print(f"Číslo {number} není prvočíslo")
    else:
        print(f"Číslo {number} je prvočíslo")
while True:
    prvocisco(number=int(input("Zadej číslo ")))

#provičování_25
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_list = []
h = 0
length = []
code = ""
hovno = input("Zadej slovo k zašifrování:\n")
k = int(input("Zadej posun"))
def find(hovno, h):
    for i in alphabet:
        if hovno != i:
            h += 1
        else:
            return h
def word(word, code):
    for i in word:
        word_list.append(i)
    print(word_list)
    for i in word_list:
        length.append(find(i, h))
    print(length)
    for i in range(0, len(hovno)):
        if length[i]+k <= len(alphabet)-1:
            word_list[i] = alphabet[length[i]+k]
        else:
            u = length[i]+k-len(alphabet)
            word_list[i] = alphabet[u]
    print(word_list)
    for i in word_list:
        code += i
    print(code)

word(hovno, code)
#DODĚLAT!

#provičování_26
it_dictionary = {
    "Integer": "Celé číslo",
    "String": "Text",
    "Float": "Desetinné číslo",
    "Boolean": "Pravdivostní hodnota"
}

for i in it_dictionary:
    print(it_dictionary[i])

#provičování_27
students_results = {
  "Harry": 85,
  "Ron": 71,
  "Hermione": 98,
  "Draco": 69
}


# Stupnice
# 91 až 100 = "Excelentní"
# 81 až 90 = "Vynikající"
# 71 až 80 = "Splněno"
# méně jak 71 = "Nesplněno"

new_dictionary = {}

for i in students_results:
    if students_results[i] >= 91 and students_results[i] <= 100:
        new_dictionary[i] = "Excelentní"
    elif students_results[i] >= 81 and students_results[i] <= 90:
        new_dictionary[i] = "Vynikající"
    elif students_results[i] >= 71 and students_results[i] <= 80:
        new_dictionary[i] = "Splněno"
    else:
        new_dictionary[i] = "Nesplněno"
print(new_dictionary)

#provičování_28
travel_diary = {
    "Spain": {"visited_cities": ["Madrid", "Leon", "Valencia"], "visits": 5},
    "France": {"visited_cities": ["Paris", "Nice", "Rennes"], "visits": 2}

}
print(travel_diary["Spain"]["visited_cities"][0])

travel_diary = [
    {
        "country": "Spain",
        "visited_cities": ["Madrid", "Leon", "Valencia"],
        "visits": 5,
    },
    {
        "country": "France",
        "visited_cities": ["Paris", "Nice", "Rennes"],
        "visits": 2,
    }
]
print(travel_diary[1]["visited_cities"][0])

#provičování_28
travel_diary = [
    {
        "country": "Spain",
        "visited_cities": ["Madrid", "Leon", "Valencia"],
        "visits": 5,
    },
    {
        "country": "France",
        "visited_cities": ["Paris", "Nice", "Rennes"],
        "visits": 2,
    }
]

def travel(country, visited_cities, visits):
    travel_diary.append({"country": country,
                         "visited_cities": visited_cities,
                         "visits": visits})

country = input("Zadej název státu\n")
visited_cities = []
for i in range(0, 3):
    visited_cities.append(input("Zadej města, teré jsi navštívil\n"))
visits = int(input("Zadej kolikrát si zde byl\n"))
travel(country, visited_cities, visits)
print(travel_diary)

#provičování_29
auction_logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
'''

auction_directory = {}

def log_in(name, money):
    auction_directory[name] = money
def final(auction_directory):
    winner = 0
    name_of_winner = ""
    for i in auction_directory:
        if auction_directory[i] > winner:
            winner = auction_directory[i]
            name_of_winner = i
    print(f"Vítězem je: {name_of_winner} s nabídkou {winner} USD")
print(auction_logo)
print("Vítejte v programu pro tichou dražbu.")
while(True):
    log_in(name=input("Zadejte své jméno\n"), money=int(input("Zadejte počrt peněz (USD)\n")))
    next = input("Je tam ještě někdo? (ano/ne)\n")
    if next == "ne":
        break
final(auction_directory=auction_directory)

#provičování_30
def year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

pravdicka = year(int(input("Zadej rok ")))

month = input("Zadej měsíc ")
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month_dictionary = {
    "leden": days_in_month[0],
    "únor": days_in_month[1],
    "březen": days_in_month[2],
    "duben": days_in_month[3],
    "květen": days_in_month[4],
    "červen": days_in_month[5],
    "červenec": days_in_month[6],
    "srpen": days_in_month[7],
    "září": days_in_month[8],
    "říjen": days_in_month[9],
    "listopad": days_in_month[10],
    "prosinec": days_in_month[11],
}
if month != "únor":
    print(month_dictionary[month])
else:
    if pravdicka:
        print(month_dictionary[month]+1)
    else:
        print(month_dictionary[month])

#provičování_31
symbol = "+-*/Zvolte jednu operaci výše: "

def plus(cislo1, cislo2):
    print(f"{cislo1} + {cislo2} = {cislo1 + cislo2}")
    return cislo1 + cislo2
def minus(cislo1, cislo2):
    print(f"{cislo1} - {cislo2} = {cislo1 - cislo2}")
    return cislo1 - cislo2
def krat(cislo1, cislo2):
    print(f"{cislo1} * {cislo2} = {cislo1 * cislo2}")
    return cislo1 * cislo2
def deleno(cislo1, cislo2):
    print(f"{cislo1} / {cislo2} = {cislo1 / cislo2}")
    return cislo1 / cislo2
def calculator():
    while True:
        cislo1 = int(input("Zadejte první číslo? "))
        while True:
            operator = input(symbol)
            cislo2 = int(input("Jaké je druhé číslo? "))
            if operator == "+":
                cislo1 = plus(cislo1, cislo2)
            elif operator == "-":
                cislo1 = minus(cislo1, cislo2)
            elif operator == "*":
                cislo1 = krat(cislo1, cislo2)
            elif operator == "/":
                if cislo2 == 0:
                    print("Nelze dělit nulou")
                else:
                    cislo2 = deleno(cislo1, cislo2)
            else:
                print("Neznámí operátor")
            pokracovat = input("Napište ano, pokud chcete pokračovat. Napište ne, pokud chcete novou alkulaci: ")
            if pokracovat == "ne":
                break
calculator()

#provičování_32
import random
logo = 
 _____                     _                                          
|  __ \                   (_)                                        
| |  \/_   _  ___  ___ ___ _ _ __   __ _    __ _  __ _ _ __ ___   ___
| | __| | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \\
| |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/
 \____/\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___|
                                    __/ |   __/ |                    
                                   |___/   |___/                      
Výtejte ve hře Guess secret number. Porazte počítač.
Myslím si číslo od 1 do 100

secret_number = random.randint(1, 100)
dificulty = input("Vyberte obtížnost, Napište 'easy' nebo 'hard': ")
vyhra = False
if dificulty == "easy":
    lives = 10
else:
    lives = 5
while lives:
    tip = int(input(f"Váš počrt zbývajících pokusů je {lives}\nTipněte si číslo: "))
    if tip < secret_number:
        print("Příliš nízké")
    elif tip > secret_number:
        print("příliš vysoké")
    else:
        vyhra = True
        break

    lives -= 1
if vyhra:
    print("Počítač prohrál. Vyhráli jste!!")
else:
    print("Počítač vyhrál. Prohráli jste!!")

#provičování_33
# Debugging (ladění, hladní chyb)


# Popiš problém
# def test_function():
#   for number in range(1, 11):
#     if number == 10:
#       print("Vše je správně")
# test_function()


# Občas funguje a občas ne
# import random
# all_dice_numbers = ["1", "2", "3", "4", "5", "6"]
# dice_number = random.randint(0, 5)
# print(all_dice_numbers[dice_number])


# Mysli jako počítač
# year = int(input("Jaký je váš rok narození?"))
# if year > 1980 and year < 1994:
#   print("Jste millenial.")
# elif year >= 1994:
#   print("Jste generace Z.")


# Oprav hned chyby
# age = int(input("Kolik je vám let?"))
# if age >= 18:
#     print(f"Ve věku {age} můžete kupovat alkohol.")

#provičování_34
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

import random

#provičování_35
data = [
    {
        'name': 'Instagram',
        'follower_count': 501,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Facebook',
        'follower_count': 4,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 436,
        'description': 'Fotbalový hráč',
        'country': 'Portugal'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 161,
        'description': 'Herec a wrestler',
        'country': 'USA'
    },
    {
        'name': 'Harry Potter film',
        'follower_count': 8,
        'description': 'Film',
        'country': 'USA'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 307,
        'description': 'Podnikatelka',
        'country': 'USA'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 324,
        'description': 'Fotbalista',
        'country': 'Argentina'
    },
    {
        'name': 'Neymar',
        'follower_count': 158,
        'description': 'Fotbalista',
        'country': 'Brazilie'
    },
    {
        'name': 'Eminem',
        'follower_count': 40,
        'description': 'Hudebník',
        'country': 'USA'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 193,
        'description': 'Hudebník',
        'country': 'Canada'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 111,
        'description': 'Herečka',
        'country': 'Francie'
    }
]
a_random = random.randint(0, 10)
body = 0
while True:
    b_random = random.randint(0, 10)
    a = f"{data[a_random]['name']}, {data[a_random]['description']}, {data[a_random]['country']}"
    b = f"{data[b_random]['name']}, {data[b_random]['description']}, {data[b_random]['country']}"
    a_fol = data[a_random]['follower_count']
    b_fol = data[b_random]['follower_count']
    if a != b:
        print(f"A: {a}\nB: {b}")
        #print(f"A: {a_fol}\nB: {b_fol}")
        tip = input("Kdo má více sledujících na instagramu? ")
        if tip == "A":
            if a_fol > b_fol:
                body += 1
                print(f"Uhádli jste. Vaše skóre je {body}")
            else:
                break
        elif tip == "B":
            if a_fol < b_fol:
                a_random = b_random
                body += 1
                print(f"Uhádli jste. Vaše skóre je {body}")
            else:
                break

print(f"To je špatně. Vaše konečné skóre je {body}")

#provičování_36
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 40,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 60,
    }
}
resources = {
    "water": 400,
    "milk": 300,
    "coffee": 150,
}
def dostatek_surovin(druh):
    if resources["water"] - MENU[druh]["ingredients"]["water"] >= 0 and resources["milk"] - MENU[druh]["ingredients"]["milk"] >= 0 and resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"] >= 0:
        print(f"Máme dostatek surovin na přípravu {druh}")
        return True
    else:
        print(f"Nemáme dostatek surovin na přípravu {druh}")
        return False
def odecet_vody(druh):
    return resources["water"] - MENU[druh]["ingredients"]["water"]
def odecet_mleka(druh):
    return resources["milk"] - MENU[druh]["ingredients"]["milk"]
def odecet_kavy(druh):
    return resources["coffee"] - MENU[druh]["ingredients"]["coffee"]
def penize(druh):
    print(f'Cena je {MENU[druh]["cost"]}Kč\nProsím, vložte mince 1, 2, 5, 10, 20, 50')
    kc1 = int(input("Kolik 1Kč chcete vložit?: "))
    kc2 = int(input("Kolik 2Kč chcete vložit?: "))
    kc5 = int(input("Kolik 5Kč chcete vložit?: "))
    kc10= int(input("Kolik 10Kč chcete vložit?: "))
    kc20 = int(input("Kolik 20Kč chcete vložit?: "))
    kc50 = int(input("Kolik 50Kč chcete vložit?: "))
    celkem = kc1 * 1 + kc2 * 2 + kc5 * 5 + kc10 * 10 + kc20 * 20 + kc50 * 50
    vraceno = celkem - MENU[druh]["cost"]
    if vraceno >= 0:
        print(f"Celkem jste vložily: {celkem}Kč\nNápoj se připravuje.\nZde jsou peníze na zpět: {vraceno}Kč")
    else:
        print("Nemáte dostatek peněz")
while True:
    vyber_kafe = input("Co byste si dal? (espresso/latte/cappuccino): ")
    #print(vyber_kafe)
    if vyber_kafe == "espresso" or vyber_kafe == "latte" or vyber_kafe == "cappuccino":
        dost = dostatek_surovin(vyber_kafe)
        if dost:
            resources["water"] = odecet_vody(vyber_kafe)
            resources["milk"] = odecet_mleka(vyber_kafe)
            resources["coffee"] = odecet_kavy(vyber_kafe)
            penize(vyber_kafe)
        else:
            break
    elif vyber_kafe == "report":
        print(f'Voda: {resources["water"]}\n'
              f'Mléko: {resources["milk"]}\n'
              f'Káva: {resources["coffee"]}')

    else:
        print("Neznámá volba. Zkuste to znovu")
"""
#provičování_37