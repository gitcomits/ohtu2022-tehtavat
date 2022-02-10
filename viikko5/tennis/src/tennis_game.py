class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.even_board = {0 : "Love-All", 1 : "Fifteen-All", 2 : "Thirty-All", 3 : "Forty-All"}
        self.advantage_board = {1 : "Advantage player1", -1 : "Advantage player2", 2 : "Win for player1", 3 : "Win for player1", 4 : "Win for player1"}
        self.score_board = {0 : "Love", 1 : "Fifteen", 2 : "Thirty", 3 : "Forty"}

    def won_point(self, player_name):
        
        if player_name == self.player1_name: 
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):

        if self.m_score1 == self.m_score2:
            return self.even_board.get(self.m_score1, "Deuce")
        
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            difference = self.m_score1 - self.m_score2
            return self.advantage_board.get(difference, "Win for player2")

        else:
            return self.score_board.get(self.m_score1) + "-" + self.score_board.get(self.m_score2)    
            