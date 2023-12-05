from pprint import  pp

def card_breakdown(card):
    segments = card.split(":")[1].split("|")
    winning_nums = [int(x) for x in segments[0].split()]
    your_nums = [int(x) for x in segments[1].split()]
    return [winning_nums, your_nums]


def check_for_wins(card_num, cards):
    card_score = 0
    winning_nums, your_nums = card_breakdown(cards[card_num])
    match_nums = 0
    for winning_num in winning_nums:
        if winning_num in your_nums:
            match_nums += 1
    if match_nums >= 1:
        card_score += sum([check_for_wins(x, cards) for x in range((card_num+1), (card_num+match_nums+1))])

    return card_score+1


with open("input4", "r") as input:
    score = 0
    cards = input.readlines()
    for i, card in enumerate(cards):
        print(f"Card Number: {i+1}")
        score += check_for_wins(i, cards)
        print(f"Score so far: {score}",
              end="\n----------------------------------------------------\n")
print(score)
