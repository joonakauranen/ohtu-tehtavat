import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_hinta_oikea(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        tupakka = Tuote("Tupakka", 10)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(tupakka)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeen_oikea_hinta(self):
        maito = Tuote("Maito", 3)
        tupakka = Tuote("Tupakka", 10)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(tupakka)
        self.assertEqual(self.kori.hinta(), 13)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_oikea_hinta(self):
        tupakka = Tuote("Tupakka", 10)
        self.kori.lisaa_tuote(tupakka)
        self.kori.lisaa_tuote(tupakka)
        self.assertEqual(self.kori.hinta(), 20)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        osto = len(self.kori.ostokset_palauta())

        self.assertEqual(osto, 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset_palauta()[0]
        nimi = ostos.tuotteen_nimi()

        self.assertEqual(nimi, "Maito")

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        tupakka = Tuote("Tupakka", 10)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(tupakka)
        osto = len(self.kori.ostokset_palauta())

        self.assertEqual(osto, 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_oikea_maara(self):
       
        tupakka = Tuote("Tupakka", 10)
        self.kori.lisaa_tuote(tupakka)
        self.kori.lisaa_tuote(tupakka)
        osto = len(self.kori.ostokset_palauta())

        self.assertEqual(osto, 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_oikea_hinta(self):
       
        tupakka = Tuote("Tupakka", 10)
        self.kori.lisaa_tuote(tupakka)
        self.kori.lisaa_tuote(tupakka)
        osto = len(self.kori.ostokset_palauta())

        ostos = self.kori.ostokset_palauta()[0]
        nimi = ostos.tuotteen_nimi()
        hinta = ostos.hinta()

        self.assertEqual(nimi, "Tupakka")

        self.assertEqual(hinta, 20)