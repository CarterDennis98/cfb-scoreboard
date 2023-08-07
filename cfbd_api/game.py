from cfbd_api.team import ScoreboardTeam
from cfbd_api.weather import Weather
from cfbd_api.betting import Betting
from cfbd_api.data import get_scoreboard


class GameScoreboard:
    def __init__(self, game):
        self.start_date = game["startDate"]
        self.quarter = game["period"]
        self.clock = game["clock"]
        self.possession = game["possession"]
        self.home_team = ScoreboardTeam(game["homeTeam"])
        self.away_team = ScoreboardTeam(game["awayTeam"])
        self.weather = Weather(game["weather"])
        self.betting = Betting(game["betting"])

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name}\n{self.home_team.points or 0} - {self.away_team.points or 0}"


def scoreboard(classification=None, conference=None):
    games = []
    data = get_scoreboard(classification, conference)
    for x in data.json():
        games.append(GameScoreboard(x))
    return games
