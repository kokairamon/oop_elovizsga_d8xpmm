import datetime

class Bicikli:
    def __init__(self):
        self.tipus = ""
        self.ar = 0
        self.allapot = ""
        self.szin = ""


class OrszagutiBicikli(Bicikli):
    def __init__(self):
        self.tipus = "Országúti"



class HegyiBicikli(Bicikli):
    def __init__(self):
        self.tipus = "Hegyi"


class TandemBicikli(Bicikli):
    def __init__(self):
        self.tipus = "Tandem"


class Kolcsonzes:
    def __init__(self, szemely, bicikli_index, datum):
        self.szemely_neve = szemely
        self.bicikli_id = bicikli_index
        self.datum = datum
        self.lemondva = False

    def __str__(self):
        print(f"{self.datum} \t {self.szemely_neve} \t {self.bicikli_tipusa}")

class Kolcsonzo:
    def __init__(self):
        self.nev = ""
        self.cim = ""
        self.telefonszam = ""
        self.biciklik = list()
        self.kolcsonzesek = list()

    def kolcsonzes_leadasa(self, kolcsonzes):
        self.kolcsonzesek.append(kolcsonzes)

    def kolcsonzes_lemondasa(self, kolcsonzes):
        kolcsonzes.lemondva = True

    def kolcsonzesek_listazasa(self):
        for k in self.kolcsonzesek:
            print(k)

    def print_fomenu(self):
        print("--- FŐMENÜ ---")
        print("1 - új bicikli hozzáadása")
        print("2 - biciklik listázása")
        print("3 - új kölcsönzés hozzádása")
        print("4 - kölcsönzés lemondása")
        print("5 - kölcsönzések listázása")
        menupont = int(input("Válassz egy menüpontot: "))

        if menupont == 1:
            self.print_menu_bicikli_hozzad()
        elif menupont == 2:
            self.biciklik_listazasa()
            self.print_fomenu()
        elif menupont == 3:
            self.print_menu_foglalas_hozzad()


    def print_menu_bicikli_hozzad(self):
        print("[Bicikli hozzádása]")
        print("1 - Országúti")
        print("2 - Hegyi")
        print("3 - Tandem")
        print("0 - Vissza a főmenübe")
        menupont = int(input("Válassz egy típust: "))

        bicikli = Bicikli()

        if menupont == 1:
            bicikli = OrszagutiBicikli()
        elif menupont == 2:
            bicikli = HegyiBicikli()
        elif menupont == 3:
            bicikli = TandemBicikli()
        else:
            self.print_fomenu()
            return

        bicikli.allapot = input("Állapot (pl. kiváló, jó, általános): ")
        bicikli.szin = input("Szín: ")
        bicikli.ar = int(input("Kölcsönzési díj egy napra (forint): "))

        self.biciklik.append(bicikli)
        self.print_menu_bicikli_hozzad()

    def print_menu_foglalas_hozzad(self):
        print("[ Új kölcsönzés hozzáadása ]")
        self.biciklik_listazasa()
        bicikli_index = int(input("Add meg a választott kerékpár számát: "))

        datum_helyes = False

        while not datum_helyes:
            valasztott_datum = input("Kölcsönués napja (pl. 2024-02-12): ")
            datum = datetime.datetime.strptime(valasztott_datum, "%Y-%m-%d").date()
            datum_helyes = self.datum_ellenorzese(datum)
            if not datum_helyes:
                print("A megadott dátumra nem adható le kölcsönzés!")

        foglalas_helyes = self.foglalas_ellenorzese(bicikli_index, datum)
        if foglalas_helyes:
            uj_kolcsonzes = Kolcsonzes()
            uj_kolcsonzes.szemely_neve = input("Kölcsönző személy neve: ")
            uj_kolcsonzes.bicikli_id = bicikli_index
            uj_kolcsonzes.datum = datum
            self.kolcsonzesek.append(uj_kolcsonzes)
        else:
            print("A megadott kerékpár már le van foglalva erre a napra!")




    def biciklik_listazasa(self):
        print("[Kerékpárok]")
        print("ID\tTípus\tÁllapot\tSzín\tÁr")
        index = 0
        for bicikli in self.biciklik:
            index = index + 1
            print(f"#{index}\t{bicikli.tipus}\t{bicikli.allapot}\t{bicikli.szin}\t{bicikli.ar}")

    def foglalas_ellenorzese(self, bicikli_index, datum):
        for kolcsonzes in self.kolcsonzesek:
            if kolcsonzes.bicikli_id == bicikli_index and kolcsonzes.datum == datum and not kolcsonzes.lemondva:
                return False
        return True

    def datum_ellenorzese(self, datum):
        mai_datum = datetime.date.today()
        return datum >= mai_datum
