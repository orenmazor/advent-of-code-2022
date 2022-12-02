"""Day 2 puzzle: evaluate rock-paper-scissors.

but this time the second hand is the outcome.

I could merge this with the original file for part1

but who cares. I can do that if we come back to the card game
"""
from typing import Tuple


def normalize_hand(hand: str) -> Tuple[str, str]:
    """Receive a hand, such as A X, and return Rock Rock."""
    their_hand, expected_condition = hand.split()

    hand_mapping = {"Rock": ["A", "X"], "Paper": ["B", "Y"], "Scissors": ["C", "Z"]}

    their_hand = [k for k, v in hand_mapping.items() if their_hand in v][0]

    assert their_hand in hand_mapping.keys()

    expected_condition_mapping = {"X": "Lose", "Y": "Draw", "Z": "Win"}
    return (their_hand, expected_condition_mapping[expected_condition])


def find_needed_hand(normalized_hand: Tuple[str, str]) -> str:
    """Receive a normalized hand and find out which hand won."""
    win_over = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
    lose_to = {v: k for k, v in win_over.items()}

    if normalized_hand[1] == "Draw":
        return normalized_hand[0]

    if normalized_hand[1] == "Win":
        return win_over[normalized_hand[0]]

    if normalized_hand[1] == "Lose":
        return lose_to[normalized_hand[0]]

    # leave this here on purpose to make logic errors clearer
    raise Exception("how did you get here.")


def evaluate_hand(normalized_hand: Tuple[str, str]) -> int:
    """Receive a normalized hand and calculate score."""
    victory_condition = normalized_hand[1]

    my_hand = find_needed_hand(normalized_hand)

    score_mapping = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
        "Draw": 3,
        "Win": 6,
        "Lose": 0,
    }

    return score_mapping[my_hand] + score_mapping[victory_condition]


def apply_strategy_guide(list_of_hands: str) -> int:
    """Receive a series of hands and find out the total score."""
    score = 0
    for hand in list_of_hands.split("\n"):
        if hand:
            score += evaluate_hand(normalize_hand(hand))

    return score
