"""
game/logic.py
Core game logic for Stone-Paper-Scissors.
"""

import random

CHOICES = ["stone", "paper", "scissors"]

WINNING_RULES = {
    "stone": "scissors",     # stone crushes scissors
    "scissors": "paper",     # scissors cuts paper
    "paper": "stone",        # paper covers stone
}

EMOJI = {
    "stone": "🪨",
    "paper": "📄",
    "scissors": "✂️",
}


def get_computer_choice() -> str:
    """Randomly select computer's choice from available options."""
    return random.choice(CHOICES)


def get_result(player: str, computer: str) -> str:
    """
    Determine the result of one round.

    Args:
        player: Player's choice (stone/paper/scissors)
        computer: Computer's choice (stone/paper/scissors)

    Returns:
        'win', 'lose', or 'draw'
    """
    if player == computer:
        return "draw"
    elif WINNING_RULES[player] == computer:
        return "win"
    else:
        return "lose"


def format_choices(player: str, computer: str) -> str:
    """Return a formatted string showing both choices with emojis."""
    return (
        f"  You    : {EMOJI[player]}  {player.capitalize()}\n"
        f"  Computer: {EMOJI[computer]}  {computer.capitalize()}"
    )


def validate_choice(choice: str) -> bool:
    """Return True if the choice is valid."""
    return choice.lower() in CHOICES
