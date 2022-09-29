cifra = 5
variant = int(input("Introduce-ti cifra"))

while cifra != variant:
    if variant > cifra:
        print("Varianta e prea mare, mai incerca")
    else:
        print("Varianta e prea mica , mai incerca")

    variant = int(input("Introduce-ti cifra"))
print("Felicitari ati ghicit cifra")



