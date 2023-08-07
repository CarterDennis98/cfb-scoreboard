from cfbd_api.team import ScoreboardTeam
from cfbd_api.weather import Weather
from cfbd_api.betting import Betting
from cfbd_api.data import get_scoreboard


class GameScoreboard:
    def __init__(self, game, teams):
        self.start_date = game["startDate"]
        self.quarter = game["period"]
        self.clock = game["clock"]
        self.possession = game["possession"]
        self.home_team = ScoreboardTeam(game["homeTeam"], teams)
        self.away_team = ScoreboardTeam(game["awayTeam"], teams)
        self.weather = Weather(game["weather"])
        self.betting = Betting(game["betting"])

    def __str__(self):
        return f"{self.home_team.short_name} vs {self.away_team.short_name}\n{self.home_team.points or 0} - {self.away_team.points or 0}"


def scoreboard(teams: list, classification=None, conference=None) -> list:
    games = []
    data = get_scoreboard(classification, conference)
    for x in data.json():
        games.append(GameScoreboard(x, teams))

    return games
