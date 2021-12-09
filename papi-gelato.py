import time

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
time.sleep(1)

def bollenA():
    aantalbolletjes = int(input("Hoeveel bolletjes ijs wilt u ? : "))
    time.sleep(1)
    if aantalbolletjes <= 3:
        if input(f"Wilt u deze {aantalbolletjes} bolletjes in een hoorntje(a) of een bakje(b)? : ") == "a":
            time.sleep(1)
            print(f"Hier is uw hoorntje met {aantalbolletjes} bollen!")
        else:
            print(f"Hier is uw bakje met {aantalbolletjes} bollen!")
            time.sleep(1)
        if input("Wilt u nog meer bestellen? (J/N) : ") == "N":
            print("Bedankt en tot ziens!")
        else:
            bollenA()
    if aantalbolletjes <= 8:
        print(f"Dan krijgt u van mij een bakje met {aantalbolletjes} bolletjes")
        time.sleep(1)
        if input("Wilt u nog meer bestellen? (J/N) : ") == "N":
            print("Bedankt en tot ziens!")
        else:
            bollenA()
    if aantalbolletjes >= 8:
        print("Sorry, zulke grote bakken hebben we niet")
        time.sleep(1)
        if input("Wilt u nog meer bestellen? (J/N) : ") == "N":
            print("Bedankt en tot ziens!")
        else:
            bollenA()


bollenA()

