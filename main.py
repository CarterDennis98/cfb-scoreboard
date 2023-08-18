import time
from PIL import Image, ImageDraw, ImageFont
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from cfbd_api.game import scoreboard
from cfbd_api.team import all_teams


def run():
    # Get a list of all teams in order to get logos/colors based on id provided by /scoreboard endpoint
    teams = all_teams()

    curr_games = scoreboard(teams, classification="fbs", conference="b12")
    old_games = curr_games

    while True:
        if curr_games:
            for game, old_game in zip(curr_games, old_games):
                print(game)
                print(game.get_betting())

                draw.rectangle([(0,0), (3,8)], fill=game.home_team.main_color)
                draw.text((5, 0), game.home_team.short_name, font=font, fill=white_fill)
                draw.rectangle([(0,9), (3, 17)], fill=game.away_team.main_color)
                draw.text((5, 9), game.away_team.short_name, font=font, fill=white_fill)
                matrix.SetImage(image)

                # Fade into new game
                for brightness in range(0, 100, 10):
                    matrix.brightness = brightness
                    matrix.SetImage(image)
                    time.sleep(.025)

                time.sleep(5)

                # Fade out
                for brightness in range(100, 0, -10):
                    matrix.brightness = brightness
                    matrix.SetImage(image)
                    time.sleep(.025)

                # Completely black out screen between games
                draw.rectangle([(0, 0), (63, 63)], fill=black_fill)

        old_games = curr_games
        curr_games = scoreboard(teams, classification="fbs", conference="b12")


if __name__ == "__main__":
    options = RGBMatrixOptions()
    options.rows = 64
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.gpio_slowdown = 1

    matrix = RGBMatrix(options=options)

    image = Image.new("RGB", (64, 64))

    draw = ImageDraw.Draw(image)

    font = ImageFont.load("assets/fonts/Tamzen5x9r.pil")

    white_fill = (255, 255, 255, 255)
    black_fill = (0, 0, 0, 255)

    run()
