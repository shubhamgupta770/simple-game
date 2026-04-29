"""
utils/input_handler.py
Handles all user input and validation.
"""

from game.logic import CHOICES, EMOJI


def get_player_choice() -> str:
    """
    Prompt the user to enter their choice and validate it.

    Returns:
        A valid lowercase choice: 'stone', 'paper', or 'scissors'
    """
    options_display = "  |  ".join(
        f"{EMOJI[c]} {c.capitalize()}" for c in CHOICES
    )

    while True:
        print(f"\n  Choices:  {options_display}")
        choice = input("  Enter your choice: ").strip().lower()

        if choice in CHOICES:
            return choice
        else:
            print(f"\n  ⚠️  Invalid input '{choice}'.")
            print(f"     Please enter one of: {', '.join(CHOICES)}")


def get_menu_choice(valid_options: list) -> str:
    """
    Prompt the user for a menu option and validate it.

    Args:
        valid_options: List of acceptable string inputs

    Returns:
        A validated menu choice string
    """
    while True:
        choice = input("  Enter option: ").strip()
        if choice in valid_options:
            return choice
        print(f"  ⚠️  Please enter one of: {', '.join(valid_options)}")
