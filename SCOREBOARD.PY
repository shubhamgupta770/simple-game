"""
game/scoreboard.py
Manages and displays the score across rounds.
"""


class Scoreboard:
    """Tracks wins, losses, and draws for the session."""

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0

    @property
    def total_rounds(self) -> int:
        return self.wins + self.losses + self.draws

    def update(self, result: str) -> None:
        """Update score based on round result."""
        if result == "win":
            self.wins += 1
        elif result == "lose":
            self.losses += 1
        elif result == "draw":
            self.draws += 1

    def display(self) -> None:
        """Print the current scoreboard."""
        print("\n" + "=" * 35)
        print("         📊  SCOREBOARD")
        print("=" * 35)
        print(f"  ✅  Wins   : {self.wins}")
        print(f"  ❌  Losses : {self.losses}")
        print(f"  🤝  Draws  : {self.draws}")
        print(f"  🎮  Total  : {self.total_rounds}")
        print("=" * 35)

    def reset(self) -> None:
        """Reset all scores to zero."""
        self.wins = 0
        self.losses = 0
        self.draws = 0
        print("\n  🔄  Scoreboard has been reset!\n")
