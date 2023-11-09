class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.score = 0
        
    def increase_score(self, points):
        self.score += points
        
    def __str__(self):
        return F"{self.name} ({self.position}) - Score: {self.score}"


class Team:
    def __init__(self, name, captain):
        self.name = name
        self.captain = captain
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)
        
    def __str__(self):
        team_info = F"Team: {self.name}\nCaptain: {self.captain}\nPlayers:"
        for player in self.players:
            team_info += f"\n{player}"
        return team_info
    
    
class VolleyballGame:
    def __init__(self, team1, team2, location, date):
        self.team1 = team1
        self.team2 = team2
        self.location = location
        self.date = date
        self.score_team1 = 0
        self.score_team2 = 0
        
    def get_winner(self):
        if self.score_team1 > self.score_team2:
            return self.team1
        elif self.score_team1 < self.score_team2:
            return self.team2
        else:
            return "It's a tie!"
        
    def __str__(self):
        return F"Volletball Game\nLocation: {self.location}\nDate: {self.date}\n{self.team1} vs. {self.team2}\n" \
            F"Score: {self.score_team1} - {self.score_team2}"