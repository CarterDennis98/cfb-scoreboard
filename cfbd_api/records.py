from cfbd_api.data import get_records
from datetime import datetime


class Records:
    def __init__(self, records):
        self.records = [Record(record) for record in records]


class Record:
    def __init__(self, record):
        self.team = record["team"]
        self.games = record["total"]["games"]
        self.wins = record["total"]["wins"]
        self.losses = record["tota"]["losses"]


def all_records() -> Records:
    records = []
    data = get_records(datetime.today().year)
    for record in data:
        records.append(Record(record))

    return Records(records)