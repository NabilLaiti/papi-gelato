import time


Bolsmaak = 1
Smaken = ["A", "C", "V", "a", "c", "v", "Aardbei", "Chocolade", "Vanille", "aardbei", "chocolade", "vanille"]
aantalbolletjes = 0
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
    if aantalbolletjes <= 3:
        if input(f"Wilt u deze {aantalbolletjes} bolletjes in een hoorntje(A) of een bakje(B)? : ") == "A":
            time.sleep(1)
            print(f"Hier is uw hoorntje met {aantalbolletjes} bollen!")
        else:
            time.sleep(1)
            print(f"Hieur is uw bakje met {aantalbolletjes} bollen!")

Bolsmaak = 1
while Bolsmaak <= aantalbolletjes:
    print()
    Smaak = input('Welke smaak wilt u voor bolletje nummer '+ str(Bolsmaak) +'? A) Aardbei, C) Chocolade of V) Vanille? ')
    if Smaak in Smaken:
        Bolsmaak += 1
    else:
        smaak()

if aantalbolletjes == 4 and 5 and 6 and 7 and 8:
    print(f"Dan krijgt u een bakje met {aantalbolletjes} bolletje's!")
    time.sleep(1)



smaak()


if input("Wilt u nog meer bestellen? (J/N) : ") == "N":
    print("Bedankt en tot ziens!")
else:
    bollenA()

