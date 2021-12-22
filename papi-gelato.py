import time

Bolsmaak = 1
Smaken = ["A", "C", "V", "a", "c", "v", "Aardbei", "Chocolade", "Vanille", "aardbei", "chocolade", "vanille"]
aantalbolletjes = 0
Hoorntje = 0
Bakje = 0
Bolprijs = float(1.10 *1)
Hoornprijs = float(1.25 *1)
Bakjeprijs = float(0.75 *1)
prijsSlagroom = float(0.50 *1)
prijsSprinkles = float(0.30 *1)
prijsCaramelSausH = float(0.60 * 1)
prijsCaramelSausB = float(0.90 * 1)
CaramelH = 0
CaramelB = 0
aantaltopping = 0
slagroom = 0
sprinkles = 0

print("Welkom bij Papi Gelato")
time.sleep(1)

def bollenA():
    global aantalbolletjes
    aantalbolletjes = int(input("Hoeveel bolletjes ijs wilt u ? : "))
    time.sleep(1)
    
    
bollenA()

if aantalbolletjes >= 9:
    print("Sorry, zulke grote bakken verkopen wij niet!")
    time.sleep(1)
    if input("Wilt u nog meer bestellen? (J/N) : ") == "N":
        print("Bedankt en tot ziens!")
        exit(1)
    else:
        bollenA()



def smaak():
    global CaramelH
    global CaramelB
    global Hoorntje
    global Bakje
    if aantalbolletjes <= 3:
        if input(f"Wilt u deze {aantalbolletjes} bolletjes in een hoorntje(A) of een bakje(B)? : ") == "A":
            time.sleep(1)
            print(f"Hier is uw hoorntje met {aantalbolletjes} bollen!")
            Hoorntje += 1
            if toppingsInput == 'D':
                CaramelH += 1
        else:
            time.sleep(1)
            print(f"Hieur is uw bakje met {aantalbolletjes} bollen!")
            Bakje += 1
            if toppingsInput == 'D':
                CaramelB += 1
    
if aantalbolletjes >=4 <=8:
    Bakje += 1
    print(f"Dan krijgt u een bakje met {aantalbolletjes} bolletje's!")
    time.sleep(1)
    if toppingsInput == 'D':
        CaramelB += 1



Bolsmaak = 1
while Bolsmaak <= aantalbolletjes:
    print()
    Smaak = input('Welke smaak wilt u voor bolletje nummer '+ str(Bolsmaak) +'? A) Aardbei, C) Chocolade of V) Vanille? ')
    if Smaak in Smaken:
        Bolsmaak += 1
    else:
        smaak()

def toppings():
    global toppingsInput
    global aantaltopping
    while True:
        toppingsInput = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ')
        if toppingsInput == 'A':
            return
        if toppingsInput == 'B':
            global slagroom
            slagroom += 1
            aantaltopping += 1
            return 'Slagroom'
        if toppingsInput == 'C':
            global sprinkles
            sprinkles = sprinkles + 1
            aantaltopping += 1
            return 'Sprinkels'
        if toppingsInput == 'D':
            aantaltopping += 1
            return'Caramel'

toppings()


smaak()


time.sleep(1)

def bon():
    if input("Wilt u een bon erbij?(J/N)? : ") == "J":
        print("----------[Papi Gelato]----------")
        if aantalbolletjes >= 1: 
            print(f"Bolletje(s)   :  {aantalbolletjes} x €1.10 = €{aantalbolletjes * Bolprijs}")
        if Hoorntje >= 1:
            print(f"Hoorentje(s)  :  {Hoorntje} x €{Hoornprijs} = €{Hoorntje * Hoornprijs}")
        if Bakje >= 1:
            print(f"Bakje(s)      :  {Bakje} x €{Bakjeprijs} = €{Bakje * Bakjeprijs}")
        if aantaltopping >= 1:
            print(f"Topping(s)    :  1 x €{slagroom * prijsSlagroom + sprinkles * prijsSprinkles + CaramelB * prijsCaramelSausB + CaramelH * prijsCaramelSausH} = €{slagroom * prijsSlagroom + sprinkles * prijsSprinkles + CaramelB * prijsCaramelSausB + CaramelH * prijsCaramelSausH}")
        print("                    ----------- +")
        print(f"Totaal        :  = €{aantalbolletjes * Bolprijs + Hoorntje * Hoornprijs + Bakje * Bakjeprijs + slagroom * prijsSlagroom + sprinkles * prijsSprinkles + CaramelB * prijsCaramelSausB + CaramelH * prijsCaramelSausH}")
    else:
        print()
bon()

if input("Wilt u nog meer bestellen? (J/N) : ") == "J":
    print("Start het proces opnieuw op doormiddel van het klikken op het strat button!")
else:
    time.sleep(1)
    print("Bedankt en tot ziens!")



time.sleep(1)