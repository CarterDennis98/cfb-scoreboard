from cfbd_api.data import get_rankings
from datetime import datetime


class Rankings:
    def __init__(self, rankings):
        self.poll = rankings["poll"]
        self.ranks = [Rank(rank) for rank in rankings["ranks"]]


class Rank:
    def __init__(self, rank):
        self.rank = rank["rank"]
        self.school = rank["school"]


def all_rankings() -> list[Rankings]:
    rankings = []
    data = get_rankings(datetime.now().year)
    for ranking in data.json():
        for poll in ranking["polls"]:
            rankings.append(Rankings(poll))

    return rankings


def get_poll(poll_name: str) -> Rankings:
    polls = all_rankings()
    poll = next((poll for poll in polls if poll.poll == poll_name), None)
    return poll
