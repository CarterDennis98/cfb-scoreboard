import time
from PIL import Image, ImageDraw, ImageFont
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from cfbd_api.game import scoreboard, GameScoreboard
from cfbd_api.team import ScoreboardTeam
from cfbd_api.team import all_teams


# Determine x starting point for drawing team name based on whether team is ranked or not
def get_draw_start(team: ScoreboardTeam) -> int:
    if not team.ranking:
        return 6
    elif len(str(team.ranking)) == 1:
        return 11
    else:
        return 16


def draw_scheduled_game(game: GameScoreboard):
    # Draw team names with colors
    draw.rectangle([(0, 0), (3, 6)], fill=game.home_team.main_color)
    draw.text(
        (5, -1),
        f"{game.home_team.ranking if game.home_team.ranking else ''}",
        font=font,
        fill=white_fill,
    )
    draw.text(
        (get_draw_start(game.home_team), -1),
        game.home_team.short_name,
        font=font,
        fill=white_fill,
    )
    draw.rectangle([(0, 7), (3, 13)], fill=game.away_team.main_color)
    draw.text(
        (5, 6),
        f"{game.away_team.ranking if game.away_team.ranking else ''}",
        font=font,
        fill=white_fill,
    )
    draw.text(
        (get_draw_start(game.away_team), 6),
        game.away_team.short_name,
        font=font,
        fill=white_fill,
    )

    # TODO: Draw team records

    # Draw game date and start time
    draw.text((0, 13), game.start_date, font=font, fill=white_fill)

    # Draw betting info
    draw.text((0, 20), game.get_betting(), font=font, fill=white_fill)

    # Draw logos
    logo_size = (32, 32)

    home_logo = Image.open(
        f"assets/logos/{game.home_team.classification}/{game.home_team.id}.png"
    )
    home_logo.thumbnail(logo_size)
    away_logo = Image.open(
        f"assets/logos/{game.away_team.classification}/{game.away_team.id}.png"
    )
    away_logo.thumbnail(logo_size)

    image.paste(home_logo, (0, 31))
    image.paste(away_logo, (32, 31))

    # Set image
    matrix.SetImage(image)


def draw_active_game(game: GameScoreboard):
    # TODO: write function
    print("Draw active game")


def draw_completed_game(game: GameScoreboard):
    # TODO: write function
    print("Draw completed game")


def run():
    # Get a list of all teams in order to get logos/colors based on id provided by /scoreboard endpoint
    teams = all_teams()

    curr_games = scoreboard(teams, classification="fbs", conference="sec")
    old_games = curr_games

    while True:
        if curr_games:
            for game, old_game in zip(curr_games, old_games):
                print(game)
                print(game.get_betting())

                # Draw screen based on game status
                if game.status == "scheduled":
                    draw_scheduled_game(game)
                elif game.status == "in_progress":
                    draw_active_game(game)
                elif game.status == "completed":
                    draw_completed_game(game)

                # Fade into new game
                for brightness in range(0, 80, 8):
                    matrix.brightness = brightness
                    matrix.SetImage(image)
                    time.sleep(0.025)

                time.sleep(5)

                # Fade out
                for brightness in range(80, 0, -8):
                    matrix.brightness = brightness
                    matrix.SetImage(image)
                    time.sleep(0.025)

                # Completely black out screen between games
                draw.rectangle([(0, 0), (63, 63)], fill=black_fill)

        old_games = curr_games
        curr_games = scoreboard(teams, classification="fbs", conference="sec")


if __name__ == "__main__":
    options = RGBMatrixOptions()
    options.rows = 64
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.gpio_slowdown = 1

    matrix = RGBMatrix(options=options)

    matrix.brightness = 80

    image = Image.new("RGB", (64, 64))

    draw = ImageDraw.Draw(image)

    font = ImageFont.load("assets/fonts/Tamzen5x9r.pil")

    white_fill = (255, 255, 255, 255)
    black_fill = (0, 0, 0, 255)

    run()
