class Weather:
    def __init__(self, weather):
        self.temperature = weather["temperature"]
        self.description = weather["description"]
        self.wind_speed = weather["windSpeed"]
        self.wind_direction = weather["windDirection"]
