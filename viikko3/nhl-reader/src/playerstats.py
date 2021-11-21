from player import Player
from playerreader import PlayerReader
#from playerreader import playerreader as default_reader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, maa):
        playerlist = self.reader.get_players()
        playerlistbynationality = []

        for pelaaja in playerlist:
            if pelaaja.nationality == maa:
                playerlistbynationality.append(pelaaja)
        
        playerlistbynationality.sort(key=lambda player: player.points, reverse=True)

        for pelaaja in playerlistbynationality:
            print(pelaaja)

