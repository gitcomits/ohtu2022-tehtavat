from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPS:
    def __init__(self,mode):
        self.mode = mode

    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = Tekoaly()
        if self.mode == "c":
            tekoaly = TekoalyParannettu(10)
        
        while True:
            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            
            if self.mode == "a":
                tokan_siirto = input("Toisen pelaajan siirto: ")

            if self.mode == "b" or self.mode == "c":
                tokan_siirto = tekoaly.anna_siirto()
                print(f"Tietokone valitsi: {tokan_siirto}")

            if self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
                tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
                print(tuomari)
            
            else:
                break

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
