import re


def max_game_colours(game):
    greens = [int(x) for x in re.findall(r"\d+(?= green)", game)]
    reds = [int(x) for x in re.findall(r"\d+(?= red)", game)]
    blues = [int(x) for x in re.findall(r"\d+(?= blue)", game)]
    scores = {"green": max(greens), "red": max(reds), "blue": max(blues)}
    return scores


possibles = []
with open("input2", "r") as input_games:
    for i, game in enumerate(input_games.readlines()):
        score = max_game_colours(game)
        if not (score["green"] > 13 or score["red"] > 12 or score["blue"] > 14):
            possibles.append(i+1)
print(possibles)
print(f"The sum is {sum(possibles)}")
