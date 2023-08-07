import time
from cfbd_api.game import scoreboard
from cfbd_api.team import all_teams


def run():
    # Get a list of all teams in order to get logos/colors based on id provided by /scoreboard endpoint
    teams = all_teams()

    curr_games = scoreboard(teams, classification="fbs", conference="b12")
    old_games = curr_games

    while True:
        if curr_games:
            for game, old_game in zip(curr_games, old_games):
                print(game)

                time.sleep(5)

        old_games = curr_games
        curr_games = scoreboard(classification="fbs", conference="b12")


if __name__ == "__main__":
    run()
