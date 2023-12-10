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


class Kolcsonzo:
    def __init__(self):
        self.nev = ""
        self.biciklik = []
        self.kolcsonzesek = []

    def kolcsonzes_leadasa(self):
        pass

    def kolcsonzes_lemondas(self):
        pass

class Kolcsonzes:
    def __init__(self, szemely, tipus):
        self.szemely_neve = szemely
        self.bicikli_tipusa = tipus
        self.datum = ""