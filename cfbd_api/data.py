import requests
import os
from dotenv import load_dotenv

load_dotenv()

CFBD_KEY = os.getenv("CFBD_KEY")
HEADERS = {"Authorization": "Bearer " + CFBD_KEY}

BASE_URL = "https://api.collegefootballdata.com/"
SCOREBOARD_URL = BASE_URL + "scoreboard?classification={0}&conference={1}"
TEAMS_URL = BASE_URL + "teams?conference={0}"


def get_teams(conference=None):
    try:
        data = requests.get(TEAMS_URL.format(conference or ""), headers=HEADERS)
        return data
    except requests.exceptions.RequestException as e:
        raise ValueError(e)


def get_scoreboard(classification=None, conference=None):
    try:
        data = requests.get(
            SCOREBOARD_URL.format(classification or "", conference or ""),
            headers=HEADERS,
        )
        return data
    except requests.exceptions.RequestException as e:
        raise ValueError(e)
