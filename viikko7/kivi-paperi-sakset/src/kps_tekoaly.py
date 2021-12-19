from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self, tekoalyvaihtoehto):
       
        self.tekoaly = tekoalyvaihtoehto

    def _toisen_siirto(self, ensimmaisen_siirto):
        tekoalyn_siirto = self.tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tekoalyn_siirto}")

        self.tekoaly.aseta_siirto(ensimmaisen_siirto)

        return tekoalyn_siirto

        
