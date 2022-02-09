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
