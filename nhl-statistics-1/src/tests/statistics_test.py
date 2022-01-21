import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_hae_pelaaja(self):
        p = self.statistics.search("Semenko")
        self.assertEqual(p.name ,"Semenko")
        
        p = self.statistics.search("NoName")
        self.assertEqual(p, None)

    def test_tiimi_pelaajat(self):
        p = self.statistics.search("Semenko")
        t = self.statistics.team(p.team)
        self.assertEqual(len(t),3)

    def test_eniten_maaleja(self):
        l = self.statistics.top_scorers(3)
        self.assertEqual(len(l),4)