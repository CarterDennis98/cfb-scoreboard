from cfbd.rest import ApiException
from cfbd import GamesApi


def getGames(gamesAPI: GamesApi, classification=None, conference=None):
    try:
        response = gamesAPI.get_scoreboard(
            classification=classification, conference=conference
        )
    except ApiException as e:
        print("Exception when calling API: %s" % e)

    return response
