# 6
class Xodim:
    def __init__(self, ism, lavozim):
        self.ism = ism
        self.__lavozim = lavozim

    def lavozim_kor(self):
        return self.__lavozim

    def lavozim_ozgartir(self, yangi):
        self.__lavozim = yangi


# 7
class Eksponat:
    def __init__(self, nom, yil):
        self.nom = nom
        self.yil = yil

class Muzey:
    def __init__(self):
        self.eksponatlar = []

    def eksponat_qosh(self, eksponat):
        self.eksponatlar.append(eksponat)

    def yil_eksponatlari(self, yil):
        return [e.nom for e in self.eksponatlar if e.yil == yil]


# 8
class Soat:
    def __init__(self, soat, minut):
        self.soat = soat
        self.minut = minut

    def vaqt_korsat(self):
        return f"{self.soat:02d}:{self.minut:02d}"

    def minut_qosh(self, m):
        self.minut += m
        self.soat += self.minut // 60
        self.minut %= 60
        self.soat %= 24


# 9
class Oyin:
    def __init__(self, jamoa1, jamoa2, hisob):
        self.jamoa1 = jamoa1
        self.jamoa2 = jamoa2
        self.hisob = hisob

class Stadion:
    def __init__(self):
        self.oyinlar = []

    def oyin_qosh(self, oyin):
        self.oyinlar.append(oyin)

    def oyinlar_royxati(self):
        return [(o.jamoa1, o.jamoa2, o.hisob) for o in self.oyinlar]


# 10
class Mashina:
    def __init__(self, nom, yil, yuk=0):
        self.nom = nom
        self.yil = yil
        self.yuk = yuk

    def yuk_qosh(self, miqdor):
        self.yuk += miqdor

    def malumot(self):
        return self.nom, self.yil, self.yuk
