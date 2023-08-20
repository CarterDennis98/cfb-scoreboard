import sys
sys.path.append("/home/carter/Documents/GitHub/cfb-scoreboard")

import time
from PIL import Image, ImageDraw, ImageFont
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from cfbd_api.game import scoreboard, GameScoreboard
from cfbd_api.team import ScoreboardTeam
from cfbd_api.team import all_teams


# Determine x starting point for drawing certain features
def get_draw_start(team: ScoreboardTeam, feature: str) -> int:
    if feature == "rank":
        if not team.ranking:
            return 6
        if (
            str(team.ranking).startswith("2")
            or str(team.ranking).startswith("4")
            or str(team.ranking).startswith("5")
            or str(team.ranking).startswith("8")
        ):
            return 6
        else:
            return 5
    if feature == "name":
        if not team.ranking:
            return 6
        elif len(str(team.ranking)) == 1:
            if str(team.ranking).startswith("1"):
                return 11
            else:
                return 12
        else:
            if str(team.ranking).startswith("1"):
                return 16
            else:
                return 17
    elif feature == "score":
        if len(str(team.points or 0)) == 1:
            return 59
        elif len(str(team.points or 0)) == 2:
            return 54


def get_poss(game: GameScoreboard, y: str) -> int:
    if game.possession or "Vanderbilt" == game.home_team.school:
        if y == "y1":
            return 0
        else:
            return 6
    elif game.possession == game.away_team.school:
        if y == "y1":
            return 7
        else:
            return 13


def draw_scheduled_game(game: GameScoreboard):
    # Draw team names, rankings with colors
    draw.rectangle([(0, 0), (3, 6)], fill=game.home_team.main_color)
    draw.text(
        (get_draw_start(game.home_team, "rank"), -1),
        f"{game.home_team.ranking if game.home_team.ranking else ''}",
        font=font,
        fill=white_fill,
    )
    draw.text(
        (get_draw_start(game.home_team, "name"), -1),
        game.home_team.short_name,
        font=font,
        fill=white_fill,
    )
    draw.rectangle([(0, 7), (3, 13)], fill=game.away_team.main_color)
    draw.text(
        (get_draw_start(game.home_team, "rank"), 6),
        f"{game.away_team.ranking if game.away_team.ranking else ''}",
        font=font,
        fill=white_fill,
    )
    draw.text(
        (get_draw_start(game.away_team, "name"), 6),
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
    # Draw team names, rankings with colors
    draw.rectangle([(0, 0), (3, 6)], fill=game.home_team.main_color)
    draw.text(
        (get_draw_start(game.home_team, "rank"), -1),
        f"{game.home_team.ranking if game.home_team.ranking else ''}",
        font=font,
        fill=white_fill,
    )
    draw.text(
        (get_draw_start(game.home_team, "name"), -1),
        game.home_team.short_name,
        font=font,
        fill=white_fill,
    )
    draw.rectangle([(0, 7), (3, 13)], fill=game.away_team.main_color)
    draw.text(
        (get_draw_start(game.home_team, "rank"), 6),
        f"{game.away_team.ranking if game.away_team.ranking else ''}",
        font=font,
        fill=white_fill,
    )
    draw.text(
        (get_draw_start(game.away_team, "name"), 6),
        game.away_team.short_name,
        font=font,
        fill=white_fill,
    )

    # Draw possession indicator
    if game.possession:
        draw.line(
            [(4, get_poss(game, "y1")), (4, get_poss(game, "y2"))], fill=yellow_fill
        )

    # Draw score
    draw.text(
        (get_draw_start(game.home_team, "score"), -1),
        game.home_team.points or "0",
        font=font,
        fill=white_fill,
    )
    draw.text(
        (get_draw_start(game.away_team, "score"), 6),
        game.away_team.points or "0",
        font=font,
        fill=white_fill,
    )

    # Draw quarter and clock
    draw.text((0, 13), f"{game.quarter or 1}Q", font=font, fill=white_fill)
    draw.text((10, 13), game.clock or "15:00", font=font, fill=white_fill)

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


def draw_completed_game(game: GameScoreboard):
    # Draw team names, rankings with colors
    draw.rectangle([(0, 0), (3, 6)], fill=game.home_team.main_color)
    draw.text(
        (get_draw_start(game.home_team, "rank"), -1),
        f"{game.home_team.ranking if game.home_team.ranking else ''}",
        font=font,
        fill=white_fill,
    )
    draw.text(
        (get_draw_start(game.home_team, "name"), -1),
        game.home_team.short_name,
        font=font,
        fill=white_fill,
    )
    draw.rectangle([(0, 7), (3, 13)], fill=game.away_team.main_color)
    draw.text(
        (get_draw_start(game.home_team, "rank"), 6),
        f"{game.away_team.ranking if game.away_team.ranking else ''}",
        font=font,
        fill=white_fill,
    )
    draw.text(
        (get_draw_start(game.away_team, "name"), 6),
        game.away_team.short_name,
        font=font,
        fill=white_fill,
    )

    # Draw final scores
    draw.text(
        (get_draw_start(game.home_team, "score"), -1),
        game.home_team.points or "0",
        font=font,
        fill=white_fill,
    )
    draw.text(
        (get_draw_start(game.away_team, "score"), 6),
        game.away_team.points or "0",
        font=font,
        fill=white_fill,
    )

    # Draw "Final"
    draw.text((0, 13), "FINAL", font=font, fill=white_fill)

    # Draw Logos
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


def run():
    # Get a list of all teams in order to get logos/colors based on id provided by /scoreboard endpoint
    teams = all_teams()

    curr_games = scoreboard(teams, classification="fbs", conference="sec")
    old_games = curr_games

    while True:
        if curr_games:
            for game, old_game in zip(curr_games, old_games):
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

    matrix = RGBMatrix(options=options)

    matrix.brightness = 80

    image = Image.new("RGB", (64, 64))

    draw = ImageDraw.Draw(image)

    font = ImageFont.load("assets/fonts/Tamzen5x9r.pil")

    white_fill = (255, 255, 255, 255)
    black_fill = (0, 0, 0, 255)
    yellow_fill = (237, 205, 59, 255)

    run()
