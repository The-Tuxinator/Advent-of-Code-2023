from pprint import pp

def card_breakdown(card):
    segments = card.split(":")[1].split("|")
    winning_nums = [int(x) for x in segments[0].split()]
    your_nums = [int(x) for x in segments[1].split()]
    return [winning_nums, your_nums]
with open("input4", "r") as input:
    score = 0
    for card in input.readlines():
        winning_nums, your_nums = card_breakdown(card)
        match_nums = 0
        for winning_num in winning_nums:
            if winning_num in your_nums:
                match_nums += 1
        if match_nums >= 1:
            score += 2 ** (match_nums - 1)
print(score)
