from cfbd_api.data import get_teams
from cfbd_api.rankings import Rankings


class Team:
    def __init__(self, team):
        self.id = team["id"]
        self.school = team["school"]
        self.short_name = team["alt_name2"]
        self.logo = team["logos"]
        self.main_color = team["color"]
        self.alt_color = team["alt_color"]
        self.classification = team["classification"]


class ScoreboardTeam:
    def __init__(self, team: Team, teams: list[Team], rankings: Rankings):
        self.id = team["id"]
        self.classification = get_team_by_id(self.id, teams).classification
        self.full_name = team["name"]
        self.school = get_team_by_id(self.id, teams).school
        self.short_name = get_team_by_id(self.id, teams).short_name
        self.logo = get_team_by_id(self.id, teams).logo
        self.main_color = get_team_by_id(self.id, teams).main_color
        self.alt_color = get_team_by_id(self.id, teams).alt_color
        self.points = team["points"]
        self.ranking = get_team_ranking(self.school, rankings)


def all_teams(conference=None) -> list[Team]:
    teams = []
    data = get_teams(conference)
    for team in data.json():
        teams.append(Team(team))

    return teams


def fbs_fcs_teams() -> list[Team]:
    teams = all_teams()
    teams = [
        team
        for team in teams
        if (team.classification == "fbs" or team.classification == "fcs")
    ]

    return teams


def get_team_by_id(id: str, teams: list[Team]) -> Team:
    return [team for team in teams if team.id == id][0]


def get_team_ranking(school: str, rankings: Rankings) -> int:
    return next((rank.rank for rank in rankings.ranks if rank.school == school), "")
