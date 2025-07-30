#Správa pojištěnců (přidání, vyhledání, výpis)

from pojistenec import Pojistenec

class Evidence:
    def __init__(self):
        self.pojistenci = []

    def pridej_pojistence(self, jmeno, prijmeni, vek, telefon):
        pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.pojistenci.append(pojistenec)

    def vypis_vsechny(self):
        if not self.pojistenci:
            print("Žádní pojištěnci nejsou v evidenci.")
            return
        for p in self.pojistenci:
            print(p)

    def vyhledej_pojistence(self, jmeno, prijmeni):
        nalezeni = [p for p in self.pojistenci if p.jmeno.lower() == jmeno.lower() and p.prijmeni.lower() == prijmeni.lower()]
        if nalezeni:
            for p in nalezeni:
                print(p)
        else:
            print("Pojištěnec nenalezen.")

