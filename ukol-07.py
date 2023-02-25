# ukol-07

class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    
    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            return "Potvrzuji půjčení vozidla"
        else:
            return "Vozidlo není k dispozici"
    
    def get_info(self):
        return f"Registrační značka: {self.registracni_znacka}, Typ vozidla: {self.typ_vozidla}"
    
    def vrat_auto(self, najete_km, pocet_dni):
        self.najete_km = najete_km
        self.pocet_dni = pocet_dni
        self.dostupne = True
        if pocet_dni < 7:
            cena = pocet_dni * 300
            return f"Cena zapůjčení vozidla {self.typ_vozidla} na {pocet_dni} dní je celkem {cena} Kč."
        else:
            cena = pocet_dni * 400
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
#Cena zapůjčení vozidla Peugeot 403 Cabrio na 4 dní je celkem 1200 Kč.
print(Peugeot.pujc_auto())
#Potvrzuji půjčení vozidla