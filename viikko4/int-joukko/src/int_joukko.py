
class IntJoukko:
    def __init__(self, kapasiteetti=5,kasvatuskoko=5):
        if kapasiteetti < 0 or kasvatuskoko < 0:
            raise Exception("Väärä kapasiteetti")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.alkioiden_lkm = 0
        self.ljono = [0] * self.kapasiteetti

    def kuuluu(self, n):
        if self.ljono.count(n) != 0:
            return True        
        return False

    def lisaa(self, n):

        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm +=  1
            return True
    
        if not self.kuuluu(n):
          
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

            return True   

        return False

    def poista(self, n):
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                self.ljono[i] = 0
                
                for j in range(i, self.alkioiden_lkm - 1):
                    self.ljono[j],self.ljono[j + 1] = self.ljono[j + 1], self.ljono[j]
                self.alkioiden_lkm -= 1
                return True

        return False

    def kopioi_taulukko(self, a, b):
        for i,_ in enumerate(a):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            x.lisaa(i)

        for i in b_taulu:
            x.lisaa(i)
    
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i,_ in enumerate(a_taulu):
            if a_taulu.count(b_taulu[i]):
                y.lisaa(b_taulu[i])
                
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            z.lisaa(i)
        
        for i in b_taulu:
            z.poista(i)

        return z

    def __str__(self):

        s = "{"
        for i in self.ljono:
            if i != 0:
                s += ", " + str(i)
        s += "}"    
        s = s.replace(", ","",1)
        
        return s