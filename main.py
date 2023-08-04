from dotenv import load_dotenv
import os
import cfbd
from games import getGames

load_dotenv()


def apiConfig() -> cfbd.Configuration:
    CFBD_KEY = os.getenv("CFBD_KEY")

    # Set up API key auth
    config = cfbd.Configuration()
    config.api_key["Authorization"] = CFBD_KEY
    config.api_key_prefix["Authorization"] = "Bearer"

    return config


def run():
    config = apiConfig()

    # Create instance of Games API class
    gamesAPI = cfbd.GamesApi(cfbd.ApiClient(config))

    # Games API params
    classification = "fbs"
    conference = "b12"

    currGames = getGames(gamesAPI, classification, conference)

    print(currGames)


if __name__ == "__main__":
    run()
