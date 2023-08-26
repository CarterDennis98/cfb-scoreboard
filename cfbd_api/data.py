import requests
import os
from dotenv import load_dotenv

load_dotenv()

CFBD_KEY = os.getenv("CFBD_KEY")
HEADERS = {"Authorization": "Bearer " + CFBD_KEY}

BASE_URL = "https://api.collegefootballdata.com/"
SCOREBOARD_URL = BASE_URL + "scoreboard?classification={0}&conference={1}"
TEAMS_URL = BASE_URL + "teams?conference={0}"
CONFERENCES_URL = BASE_URL + "conferences"
RANKINGS_URL = BASE_URL + "rankings?year={0}&week={1}&seasonType={2}"
RECORDS_URL = BASE_URL + "records?year={0}&team={1}&conference={2}"


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


def get_conferences():
    try:
        data = requests.get(CONFERENCES_URL, headers=HEADERS)
        return data
    except requests.exceptions.RequestException as e:
        raise ValueError(e)


def get_rankings(year: int, week=None, seasonType=None):
    try:
        data = requests.get(
            RANKINGS_URL.format(year, week or "", seasonType or ""), headers=HEADERS
        )
        return data
    except requests.exceptions.RequestException as e:
        raise ValueError(e)


def get_records(year: int, team: str, conference=None):
    try:
        data = requests.get(
            RECORDS_URL.format(year, team, conference or ""), headers=HEADERS
        )
        print(data.json())
        return data
    except requests.exceptions.RequestException as e:
        raise ValueError(e)
