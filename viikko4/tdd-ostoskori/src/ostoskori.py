from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self): 
        self.tuotekori = {}
        
    def tavaroita_korissa(self):
        n = 0
        for tavara in self.tuotekori.values():
            n += tavara.lukumaara()
        return n 
 
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for tavara in self.tuotekori.values():
            summa += tavara.hinta()
        
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
    #    self.tuotekori.append(Tuote) 
        if lisattava.nimi in self.tuotekori:
            self.tuotekori[lisattava.nimi].muuta_lukumaaraa(1)
        else:
            self.tuotekori[lisattava.nimi] = Ostos(lisattava)
            
        # lisää tuotteen
        pass

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        L = []
        for tavara in self.tuotekori.values():
            L.append(tavara)
        return L
 




        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
