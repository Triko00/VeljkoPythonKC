# Domaci rad Informatika - Logicki operatori
# Autor: Veljko Trajkovic
# Datum: 9. april 2020

print("Zvog virusa COVID-19 vreme kretanja je ograniceno.")
godine = int(input("Unesite koliko imate godina: "))
if godine <= 65: 
    cas = int(input("Unesite cas BEZ minuta: "))
    if cas in range(5,17):
        print("Mozete da se krecete.")
    else:
        print("Ne mozete da se krecete.")
        
else:
    print("Ne mozete da se krecete zbog starosti. Ostanite kod kuce!")
