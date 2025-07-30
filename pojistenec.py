#Třída pojištěnec

class Pojistenec:
    def __init__(self,jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, Věk: {self.vek}, Telefon: {self.telefon}"
