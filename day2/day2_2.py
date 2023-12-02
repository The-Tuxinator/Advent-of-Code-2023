import re


def max_game_colours(game):
    greens = [int(x) for x in re.findall(r"\d+(?= green)", game)]
    reds = [int(x) for x in re.findall(r"\d+(?= red)", game)]
    blues = [int(x) for x in re.findall(r"\d+(?= blue)", game)]
    scores = {"green": max(greens), "red": max(reds), "blue": max(blues)}
    return scores


powers = []
with open("input2", "r") as input_games:
    for i, game in enumerate(input_games.readlines()):
        score = max_game_colours(game)
        powers.append(score["green"] * score["red"] * score["blue"])

print(powers)
print(f"The sum is {sum(powers)}")
