# ukol-07

class Auto:
    def __init__(self, registracni_znacka: str, typ_vozidla: str, najete_km: int):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.stav_tachometru = 0
        self.dostupne = True
    
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji půjčení vozidla"
        else:
            return "Vozidlo není k dispozici"
    
    def get_info(self):
        return f"Registrační značka: {self.registracni_znacka}, Typ vozidla: {self.typ_vozidla}"
    
    def vrat_auto(self, stav_tachometru_vraceni, pocet_dni):
        self.stav_tachometru_vraceni = stav_tachometru_vraceni
        self.najete_km += stav_tachometru_vraceni - self.stav_tachometru
        self.stav_tachometru = stav_tachometru_vraceni
        self.pocet_dni = pocet_dni
        self.dostupne = True
        if pocet_dni < 7:
            cena = pocet_dni * 400
            return f"Cena zapůjčení vozidla {self.typ_vozidla} na {pocet_dni} dní je celkem {cena} Kč."
        else:
            cena = pocet_dni * 300
            return f"Cena zapůjčení vozidla {self.typ_vozidla} na {pocet_dni} dní je celkem {cena} Kč."

Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

print(Peugeot.get_info())
print(Skoda.get_info())

print(Peugeot.pujc_auto())
#Potvrzuji půjčení vozidla
print(Peugeot.pujc_auto())
#Vozidlo není k dispozici
print(Peugeot.vrat_auto(47600, 4))
#Cena zapůjčení vozidla Peugeot 403 Cabrio na 4 dní je celkem 1600 Kč.
print(Peugeot.pujc_auto())
#Potvrzuji půjčení vozidla

auta = {"Škoda": Skoda, "Peugeot": Peugeot}

vyber_auto = input("Jaké auto si přejete půjčit? (Peugeot/Škoda) ")

print(auta[vyber_auto].get_info())
print(auta[vyber_auto].pujc_auto())

#if vyber_auto == "Škoda":
#    print(Skoda.get_info())
#    print(Skoda.pujc_auto())
#elif vyber_auto == "Peugeot":
#    print(Peugeot.get_info())
#    print(Peugeot.pujc_auto())
#else:
#    print("Takové auto nemáme.")