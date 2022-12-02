"""Day 2 puzzle: evaluate rock-paper-scissors."""
from typing import Tuple

score_mapping = {"Rock": 1, "Paper": 2, "Scissors": 3}

hand_mapping = {"Rock": ["A", "X"], "Paper": ["B", "Y"], "Scissors": ["C", "Z"]}


def normalize_hand(hand: str) -> Tuple[str, str]:
    """Receive a hand, such as A X, and return Rock Rock."""
    their_hand, my_hand = hand.split()

    their_hand = [k for k, v in hand_mapping.items() if their_hand in v][0]

    my_hand = [k for k, v in hand_mapping.items() if my_hand in v][0]

    assert their_hand in hand_mapping.keys()
    assert my_hand in hand_mapping.keys()

    return (their_hand, my_hand)


def find_winner(normalized_hand: Tuple[str, str]) -> str:
    """Receive a normalized hand and find out which hand won."""
    if "Rock" in normalized_hand and "Scissors" in normalized_hand:
        return "Rock"

    if "Rock" in normalized_hand and "Paper" in normalized_hand:
        return "Paper"

    if "Paper" in normalized_hand and "Scissors" in normalized_hand:
        return "Scissors"

    # the only way we get here is if its a tie and thats an implementation mistake

    raise Exception("how did you get here.")


def evaluate_hand(normalized_hand: Tuple[str, str]) -> int:
    """Receive a normalized hand and calculate score."""
    my_hand = normalized_hand[1]
    their_hand = normalized_hand[0]

    if my_hand == their_hand:
        return 3 + score_mapping[my_hand]

    winner = find_winner(normalized_hand)

    if my_hand == winner:
        return 6 + score_mapping[my_hand]
    elif their_hand == winner:
        return 0 + score_mapping[my_hand]


def apply_strategy_guide(list_of_hands: str) -> int:
    """Receive a series of hands and find out the total score."""
    score = 0
    for hand in list_of_hands.split("\n"):
        if hand:
            score += evaluate_hand(normalize_hand(hand))

    return score
