import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)
    

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("maito",2)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),1)


    def test_yhden_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        olut = Tuote("olut",2)
        self.kori.lisaa_tuote(olut)
        self.assertEqual(self.kori.hinta(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        olut = Tuote("olut",2)
        self.kori.lisaa_tuote(olut)
        maito = Tuote("maito",2)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),2)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hinta(self):
        olut = Tuote("olut",2)
        self.kori.lisaa_tuote(olut)
        piima = Tuote("piima",4)
        self.kori.lisaa_tuote(piima)
        self.assertEqual(self.kori.hinta(), 6)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("maito",2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),2)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hinta(self):
        olut = Tuote("olut",2)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(olut)
        self.assertEqual(self.kori.hinta(), 4)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        # testaa että metodin palauttaman listan pituus 1

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]    
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)
        
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        piima = Tuote("piima", 3)
        self.kori.lisaa_tuote(piima)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)
        # testaa että metodin palauttaman listan pituus 2

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):    
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]    
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_kahden_tuotteen_lisaamisen_ja_toisen_poistamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        suklaa = Tuote("Suklaa", 3)
        self.kori.lisaa_tuote(suklaa)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        # testaa että metodin palauttaman listan pituus 1

    def test_tuotteen_lisaaminen_ja__poistamisen_jalkeen_kori_on_tyhja(self):
        suklaa = Tuote("Suklaa", 3)
        self.kori.lisaa_tuote(suklaa)
        self.kori.poista_tuote(suklaa)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)

    def test_korit_tyhjennetaa_kaikesta(self):
        suklaa = Tuote("Suklaa", 3)
        self.kori.lisaa_tuote(suklaa)
        self.kori.lisaa_tuote(suklaa)
        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)
