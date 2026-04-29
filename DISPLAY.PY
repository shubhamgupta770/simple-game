"""
utils/display.py
Handles all display/UI output for the game.
"""


def print_banner() -> None:
    """Print the game welcome banner."""
    print("\n" + "=" * 40)
    print("   🪨  STONE · PAPER · SCISSORS  ✂️")
    print("=" * 40)
    print("   Welcome! Beat the computer to win.\n")


def print_menu() -> None:
    """Display the main menu options."""
    print("\n" + "-" * 40)
    print("           🎮  MAIN MENU")
    print("-" * 40)
    print("  1. Play a Round")
    print("  2. View Scoreboard")
    print("  3. Reset Scores")
    print("  4. How to Play")
    print("  5. Quit")
    print("-" * 40)


def print_round_result(result: str, player: str, computer: str, formatted: str) -> None:
    """Display the outcome of a single round."""
    messages = {
        "win":  "🎉  You WIN this round!",
        "lose": "💀  You LOSE this round!",
        "draw": "🤝  It's a DRAW!",
    }
    print("\n" + "~" * 40)
    print("         ⚔️   ROUND RESULT")
    print("~" * 40)
    print(formatted)
    print()
    print(f"  ➜  {messages[result]}")
    print("~" * 40)


def print_how_to_play() -> None:
    """Display the rules of the game."""
    print("\n" + "=" * 40)
    print("         📖  HOW TO PLAY")
    print("=" * 40)
    print("  🪨  Stone  crushes  ✂️  Scissors")
    print("  ✂️  Scissors cuts   📄  Paper")
    print("  📄  Paper  covers   🪨  Stone")
    print()
    print("  Enter your choice when prompted.")
    print("  The computer picks randomly.")
    print("  Most wins at the end wins!")
    print("=" * 40)


def print_goodbye() -> None:
    """Print exit message."""
    print("\n" + "=" * 40)
    print("  👋  Thanks for playing! Goodbye!")
    print("=" * 40 + "\n")
