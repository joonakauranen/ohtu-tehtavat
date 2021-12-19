from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from tekoaly import Tekoaly
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tekoaly_parannettu import TekoalyParannettu

class Pelitehdas:
    def ihminen():
        return KPSPelaajaVsPelaaja()
    
    def tekoaly():
        return KPSTekoaly(Tekoaly())

    def parempi_tekoaly():
        return KPSTekoaly(TekoalyParannettu(10))