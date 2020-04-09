print("Zbog virusa COVID-19 kretanje je dozvoljeno od 5 do 17h.")

godine = int(input("Koliko imate godina: "))

if godine <= 65: 

    cas = int(input("Unesi vreme u casovima (0-24): "))

    if cas in range(5,17):
        print("Kretanje je dozvoljeno.")
    else:
        print("Kretanje nije dozvoljeno.")

else:
    print("Kretanje nije dozvoljeno. Ostanite kod kuce!")
