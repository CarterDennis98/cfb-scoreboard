from cfbd_api.data import get_teams


class ScoreboardTeam:
    def __init__(self, team, teams):
        self.id = team["id"]
        self.full_name = team["name"]
        self.school = get_team_by_id(self.id, teams).school
        self.short_name = get_team_by_id(self.id, teams).short_name
        self.logo = get_team_by_id(self.id, teams).logo
        self.main_color = get_team_by_id(self.id, teams).main_color
        self.alt_color = get_team_by_id(self.id, teams).alt_color
        self.points = team["points"]


class Team:
    def __init__(self, team):
        self.id = team["id"]
        self.school = team["school"]
        self.short_name = team["alt_name2"]
        self.logo = team["logos"]
        self.main_color = team["color"]
        self.alt_color = team["alt_color"]


def all_teams(conference=None) -> list:
    all_teams = []
    data = get_teams(conference)
    for x in data.json():
        all_teams.append(Team(x))

    return all_teams


def get_team_by_id(id: str, teams: list[Team]):
    return [x for x in teams if x.id == id][0]
