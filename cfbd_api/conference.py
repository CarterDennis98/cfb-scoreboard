from data import get_conferences


class Conference:
    def __init__(self, conference):
        self.id = conference["id"]
        self.name = conference["name"]
        self.short_name = conference["short_name"]
        self.abbreviation = conference["abbreviation"]
        self.classification = conference["classification"]


def all_conferences() -> list[Conference]:
    conferences = []
    data = get_conferences()
    for conference in data.json():
        conferences.append(Conference(conference))

    return conferences


def fbs_fcs_conferences() -> list[Conference]:
    conferences = all_conferences()
    conferences = [
        conf
        for conf in conferences
        if (conf.classification == "fbs" or conf.classification == "fcs")
    ]

    return conferences


data = fbs_fcs_conferences()
for conf in data:
    print(f"{conf.name} ({conf.abbreviation}) - {conf.classification}")
