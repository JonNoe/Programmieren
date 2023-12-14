def faktorisieren(fak):
    if (fak == 1):
        return 1
    else:
        return fak * faktorisieren(fak-1)
        


fak=int(input("Welche Zahl möchten sie faktorisieren? \n Bitte geben sie einen Wert über null ein "))
print(f"Die Faktualisierung Ihrer Zahl {fak} ist {faktorisieren(fak)} ")
