# Spuštění programu a uživatelské menu
from evidence import Evidence

# Správa pojištěnců (přidání, vyhledání, výpis)
def zadani_textu(text, povinne=True):
    while True:
        vstup = input(text).strip()
        if not vstup and povinne:
            print("Tato položka je povinná.")

        else:
            return vstup
# Spuštění programu a uživatelské menu
def main():
    evidence = Evidence()

    while True:
        print("\n---Evidence Pojištěnců---")
        print("1. Přidat pojištěnce")
        print("2. Vypsat všechny pojištěnce")
        print("3. Vyhledat pojištěnce")
        print("4. Konec")
        volba = input ("Zvol možnost 1-4: ").strip()

        if volba == "1":
            jmeno = zadani_textu("Zadejte jméno pojištěnce: ")
            prijmeni = zadani_textu("Zadejte příjmení pojištěnce: ")
            vek = zadani_textu("Zadejte věk pojištěnce: ")
            telefon = zadani_textu("Zadejte telefonní číslo: ")
            evidence.pridej_pojistence(jmeno, prijmeni, vek, telefon)
            print ("Pojištěnec přidán.")

        elif volba == "2":
            evidence.vypis_vsechny()

        elif volba == "3":
            jmeno = zadani_textu("Zadejte jméno: ")
            prijmeni = zadani_textu("Zadejte příjmení: ")
            evidence.vyhledej_pojistence(jmeno, prijmeni)

        elif volba == "4":
            print ("Konec programu.")
            break

        else:
            print ("Neplatná volba, zvolte 1-4.")

if __name__ == "__main__":
    main()

