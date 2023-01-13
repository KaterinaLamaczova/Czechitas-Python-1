jmeno = "Kateřina"
email = jmeno + "@czechitas.cz"
print(email)

#Bonus:
jmeno_a_prijmeni = input("Zadejte, prosím, Vaše jméno a příjmení: ")

print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())

jmeno_a_prijmeni = jmeno_a_prijmeni.split(" ")
krestni = jmeno_a_prijmeni[0]
prijmeni = jmeno_a_prijmeni[1]

print(krestni.capitalize() + " " + prijmeni.capitalize())

if len(krestni) > 5:
    print(krestni[0] + ". " + prijmeni.capitalize())
else:
    print(krestni.capitalize() + " " + prijmeni.capitalize())