class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):

        if self.m_score1 == self.m_score2:

            return self.if_even(self.m_score1)

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            
            minus_result = self.m_score1 - self. m_score2

            return self.if_a_player_has_4_or_more(minus_result)
        
        else:
            return self.if_other_score()


    def if_even(self, score):

        if score == 0:
                expression = "Love-All"
        elif self.m_score1 == 1:
            expression = "Fifteen-All"
        elif self.m_score1 == 2:
            expression = "Thirty-All"
        elif self.m_score1 == 3:
            expression = "Forty-All"
        else:
            expression = "Deuce"
        
        return expression

    def if_a_player_has_4_or_more(self, points):

        if points == 1:
            score = "Advantage player1"
        elif points == -1:
            score = "Advantage player2" 
        elif points >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"

        return score

    def if_other_score(self):

        score = ""
        temp_score = 0

        for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"
        return score