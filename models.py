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
        self.dij = 0
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
        elif menupont == 4:
            self.print_menu_lemondas()
        elif menupont == 5:
            self.kolcsonzesek_listazasa()
            self.print_fomenu()
        else:
            self.print_fomenu()


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
        print("Add meg a választott kerékpár számát, vagy írj 0-t a visszalépéshez!")
        bicikli_index = int(input("Kerékpár száma: "))

        if(bicikli_index == 0):
            self.print_fomenu()
            return

        bicikli = self.biciklik[bicikli_index - 1]

        datum_helyes = False

        while not datum_helyes:
            valasztott_datum = input("Kölcsönzés napja (pl. 2024-02-12): ")
            datum = datetime.datetime.strptime(valasztott_datum, "%Y-%m-%d").date()
            datum_helyes = self.datum_ellenorzese(datum)
            if not datum_helyes:
                print("A megadott dátumra nem adható le kölcsönzés!")

        foglalas_helyes = self.foglalas_ellenorzese(bicikli_index, datum)
        if foglalas_helyes:
            nev = input("Kölcsönző személy neve: ")
            uj_kolcsonzes = Kolcsonzes(szemely=nev, bicikli_index=bicikli_index, datum=datum)
            uj_kolcsonzes.dij = bicikli.ar
            self.kolcsonzesek.append(uj_kolcsonzes)
            print("A kölcsönzés rögzítve!")
            print(f"A kölcsönzési díj a választott kerékpárra: {uj_kolcsonzes.dij} Ft")


            self.print_fomenu()
            return
        else:
            print("A megadott kerékpár már le van foglalva erre a napra!")
            print("Válassz másik kerékpárt és/vagy dátumot!")
            self.print_menu_foglalas_hozzad()

    def print_menu_lemondas(self):
        print("[Kölcsönzés lemondása]")
        self.kolcsonzesek_listazasa(csak_lemondhato=True)
        print("Add meg a lemondandó kölcsönzés számát, vagy 0-t a visszalépéshez!")
        lemondando = int(input("Kölcsönzés száma: "))
        if lemondando == 0:
            self.print_fomenu()
            return

        self.kolcsonzesek[lemondando - 1].lemondva = True
        print("A kölcsönzés lemondásra került!")
        self.print_fomenu()
        return

    def biciklik_listazasa(self):
        print("[Kerékpárok]")
        print("ID\tTípus\tÁllapot\tSzín\tÁr")
        index = 0
        for bicikli in self.biciklik:
            index = index + 1
            print(f"#{index}\t{bicikli.tipus}\t{bicikli.allapot}\t{bicikli.szin}\t{bicikli.ar}")

    def kolcsonzesek_listazasa(self, csak_lemondhato = False):
        print("[Kölcsönzések]")
        print("ID\tDátum\tSzemély\tKerékpár típusa\tDíj\tLemondva?")
        index = 0
        for kolcsonzes in self.kolcsonzesek:
            index = index + 1
            bicikli = self.biciklik[kolcsonzes.bicikli_id-1]
            lemondas = "Igen" if kolcsonzes.lemondva else "Nem"

            mutat = True
            if csak_lemondhato:
                if kolcsonzes.lemondva or kolcsonzes.datum < datetime.date.today():
                    mutat = False

            if mutat:
             print(f"#{index}\t{kolcsonzes.datum}\t{kolcsonzes.szemely_neve}\t{bicikli.tipus}\t{kolcsonzes.dij} Ft\t{lemondas}")

    def foglalas_ellenorzese(self, bicikli_index, datum):
        for kolcsonzes in self.kolcsonzesek:
            if kolcsonzes.bicikli_id == bicikli_index and kolcsonzes.datum == datum and not kolcsonzes.lemondva:
                return False
        return True

    def datum_ellenorzese(self, datum):
        mai_datum = datetime.date.today()
        return datum >= mai_datum
