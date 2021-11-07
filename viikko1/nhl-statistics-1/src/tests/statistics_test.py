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

    def test_loytaa_pelaajan(self):
        pelaaja = self.statistics.search("Semenko")

        tulostus = str(pelaaja)


        self.assertEqual(tulostus, "Semenko EDM 4 + 12 = 16")

    def test_palauttaa_oikein_jos_pelaajaa_ei_ole(self):
        pelaaja = self.statistics.search("Semmenko")

        self.assertEqual(pelaaja, None)

    def test_loytaa_listan_tiimin_mukaan(self):
        joukkue = self.statistics.team("EDM")

        onko = isinstance(joukkue, list)

        self.assertEqual(onko, True)

    def test_loytaa_top_scorer(self):
        joukkue = self.statistics.top_scorers(1)

        nimi = str(joukkue[0])

        self.assertEqual(nimi, "Gretzky EDM 35 + 89 = 124")
