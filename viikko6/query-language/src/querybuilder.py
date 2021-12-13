from matchers import *

class QueryBuilder:
    def ___init__(self, matcher = All()):
        self.matcherrr = matcher
    
    def playsIn(self, team):
        return QueryBuilder(And(self.matcherrr, PlaysIn(team)))

    def build(self):
        return self.matcher