class PlayerStats():

    def __init__(self, reader):
        self.reader = reader

    
    def top_scorers_by_nationality(self,nat:str):
        national_list = []
        players = self.reader.get_players()


        players.sort(key=lambda x: x.score, reverse=True)
        for player in players:
            if player.nationality == nat:      
                national_list.append(player)

        return national_list