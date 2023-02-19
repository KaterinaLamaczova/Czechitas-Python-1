# úkol-06

import re

# 1. Datum
datum_format = re.compile(r"\d\d?(.|. |\/)\d\d?(.|. |\/)\d{4}")

# 2. Adresa
adresa_format = re.compile(r"\d{3} \d{2} +(\w+ \w+ \w+|\w+ \w+|\w+)")

# 3. Bonus

jmeno = input("Zadejte přihlašovací jméno: ")

jmeno_format = re.compile(r"[a-zA-Z]{6,10}")
heslo_format = re.compile(r"[\w_\-.+=]{12,30}")
email_format = re.compile(r"([a-zA-Z0-9]+[\.\-\+_]?[\w]+|\"[a-zA-Z0-9]+\"|_+)@(\w+[\.-]?\w+\.([a-vx-z][a-df-z][ac-z]|[a-z]{2}|[a-z]{4,})|\[?\d{3}.\d{3}.\d{3}.\d{3}\]?)")

jmeno_ok = jmeno_format.fullmatch(jmeno)

if jmeno_ok:
    print("Uživatelské jméno je správně.")
    heslo = input("Zadejte heslo: ")
    heslo_ok = heslo_format.fullmatch(heslo)

    if heslo_ok:
        print("Heslo je správně.")
        email = input("Zadejte e-mail: ")
        email_ok = email_format.fullmatch(email)

        if email_ok:
            print("Email je správně.")
        else:
            print("Neplatný email.")

    else:
        print("Špatný formát hesla.")

else:
    print("Špatný formát uživatelského jména.")