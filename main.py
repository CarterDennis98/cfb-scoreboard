import time
from cfbd_api.game import scoreboard

def run():
    currGames = scoreboard(classification="fbs", conference="b12")
    oldGames = currGames

    while True:
        for game in currGames:
            print(game)

            time.sleep(5)

        oldGames = currGames
        currGames = scoreboard(classification="fbs", conference="b12")


if __name__ == "__main__":
    run()
