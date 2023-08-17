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

                draw.text((1,1), f"{game.home_team.short_name} vs {game.away_team.short_name}", font=font, fill=white_fill)
                matrix.SetImage(image)

                time.sleep(5)
                draw.rectangle([(0, 0),(63, 63)], fill=black_fill)

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

    font = ImageFont.truetype("assets/fonts/versa.otf", size=9)

    white_fill = (255, 255, 255, 255)
    black_fill = (0, 0, 0, 255)

    run()
