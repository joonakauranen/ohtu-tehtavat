from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        
        maara = 0

        if len(self.ostokset) == 0:
            return 0

        for ost in self.ostokset:
            maara = maara + ost.lukumaara()
        
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0

        if len(self.ostokset) == 0:
            return 0

        for ost in self.ostokset:
            hinta = hinta + ost.hinta()
        
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):

        lisattavan_nimi = lisattava.nimi()

        for ost in self.ostokset:
            if ost.tuotteen_nimi() == lisattavan_nimi:
                ost.muuta_lukumaaraa(1)
                return

        
        self.ostokset.append(Ostos(lisattava))
        

    def poista_tuote(self, poistettava: Tuote):
        
        lisattavan_nimi = poistettava.nimi()

        onko = True

        for ost in self.ostokset:
            if ost.tuotteen_nimi() == lisattavan_nimi and ost.lukumaara() >= 1:
                ost.muuta_lukumaaraa(-1)
                onko = False
                return
        if onko:
            self.ostokset.remove(Ostos(poistettava))

    def tyhjenna(self):
        self.ostokset.clear()

    def ostokset_palauta(self):
        return self.ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
