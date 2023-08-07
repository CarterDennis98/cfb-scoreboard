class Betting:
    def __init__(self, betting):
        self.spread = betting["spread"]
        self.over_under = betting["overUnder"]
        self.home_money_line = betting["homeMoneyline"]
        self.away_money_line = betting["awayMoneyline"]
