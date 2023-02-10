# Úkol-04: SMS zprávy

# Fce pro ověření tel. čísla:

def over_tel(tel_cislo: str) -> bool:
    """
    Fce ověří platnost telefonního čísla zadaného uživatelem.
    1 povinný parametr = tel. číslo (str)
    1. Odstraní možné mezery v tel. čísle
    2. Ověří délku tel. čísla - 9 znaků
    3. Pokud je číslo delší, ověří zda má předvolbu +420 (13 znaků) nebo 00420 (14 znaků)
    4. Vrátí True (=platné číslo) nebo False (=neplatné číslo)
    """
    tel_cislo = tel_cislo.replace(" ", "")
    if len(tel_cislo) == 9:
        return True
    elif tel_cislo.startswith("+420") == True and len(tel_cislo) == 13:
        return True
    elif tel_cislo.startswith("00420") == True and len(tel_cislo) == 14:
        return True
    else:
        return False

# Funkce pro výpočet ceny SMS zprávy:

def cena_SMS(sms: str) -> int:
    """
    Fce vypočítá cenu SMS zprávy na základě její délky.
    1 povninný parametr = SMS zpráva (str)
    Cena SMS = 3 CZK za každých započatých 180 znaků.
    Vrátí cenu za SMS.
    """
    cena_180 = 3
    delka_SMS = len(sms)
    if delka_SMS % 180 != 0:
        pocet = (delka_SMS // 180) + 1
    else:
        pocet = delka_SMS // 180
    cena_SMS = pocet * cena_180
    return cena_SMS

# Uživatel zadá tel. číslo a pomocí fce se ověří jeho platnost. Pokud je číslo platné, uživatel může zadat SMS zprávu a vypíše se cena zprávy:

tel_cislo_uzivatele = input("Zadejte telefonní číslo: ")

if over_tel(tel_cislo_uzivatele) == False:
    print("Neplatné telefonní číslo.")
else:
    SMS_zprava = input("Napište SMS zprávu: ")
    print(f"Cena SMS zprávy je {cena_SMS(SMS_zprava)} Kč.")