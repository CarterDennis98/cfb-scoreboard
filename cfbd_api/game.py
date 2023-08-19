from cfbd_api.team import ScoreboardTeam
from cfbd_api.weather import Weather
from cfbd_api.betting import Betting
from cfbd_api.data import get_scoreboard
from datetime import datetime, timezone
from cfbd_api.rankings import get_poll


class GameScoreboard:
    def __init__(self, game, teams, rankings):
        self.start_date = format_time(game["startDate"]).strftime("%-m/%-d %-I:%M%p")
        self.status = game["status"]
        self.quarter = game["period"]
        self.clock = game["clock"]
        self.possession = game["possession"]
        self.home_team = ScoreboardTeam(game["homeTeam"], teams, rankings)
        self.away_team = ScoreboardTeam(game["awayTeam"], teams, rankings)
        self.weather = Weather(game["weather"])
        self.betting = Betting(game["betting"])

    def __str__(self):
        return f"{self.home_team.short_name} vs {self.away_team.short_name}\n{self.home_team.points or 0} - {self.away_team.points or 0}"

    def get_betting(self):
        if self.betting.spread is None:
            return ""
        else:
            return f"{self.home_team.short_name}{'' if self.betting.spread.startswith('-') else '+'}{self.betting.spread}"


def format_time(time: str):
    # Convert ISO 8601 time to Central Time
    utc = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
    return utc.replace(tzinfo=timezone.utc).astimezone(tz=None)


def scoreboard(
    teams: list, classification=None, conference=None
) -> list[GameScoreboard]:
    games = []
    scoreboards = get_scoreboard(classification, conference)
    rankings = get_poll("AP Top 25")
    for scoreboard in scoreboards.json():
        games.append(GameScoreboard(scoreboard, teams, rankings))

    return games
