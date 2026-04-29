"""
main.py
Entry point for the Stone-Paper-Scissors game.
Runs a menu-driven infinite loop. All logic is delegated to packages.
"""

from game.logic import get_computer_choice, get_result, format_choices
from game.scoreboard import Scoreboard
from utils.display import (
    print_banner,
    print_menu,
    print_round_result,
    print_how_to_play,
    print_goodbye,
)
from utils.input_handler import get_player_choice, get_menu_choice


def play_round(scoreboard: Scoreboard) -> None:
    """Handle a single round of the game."""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = get_result(player_choice, computer_choice)
    formatted = format_choices(player_choice, computer_choice)
    print_round_result(result, player_choice, computer_choice, formatted)
    scoreboard.update(result)


def main() -> None:
    """Main function: runs the menu-driven game loop."""
    print_banner()
    scoreboard = Scoreboard()

    while True:
        print_menu()
        choice = get_menu_choice(["1", "2", "3", "4", "5"])

        if choice == "1":
            play_round(scoreboard)

        elif choice == "2":
            scoreboard.display()

        elif choice == "3":
            scoreboard.reset()

        elif choice == "4":
            print_how_to_play()

        elif choice == "5":
            scoreboard.display()
            print_goodbye()
            break


if __name__ == "__main__":
    main()
