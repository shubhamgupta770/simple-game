# 🪨 Stone Paper Scissors

A menu-driven terminal game built in Python following a clean **package architecture**.

---

## 📁 Project Structure

```
stone_paper_scissors/
│
├── main.py                   # Entry point — menu loop only
│
├── game/                     # Game logic package
│   ├── __init__.py
│   ├── logic.py              # Core game rules & random choice
│   └── scoreboard.py         # Score tracking class
│
├── utils/                    # Utility package
│   ├── __init__.py
│   ├── display.py            # All print/UI functions
│   └── input_handler.py      # Input prompts & validation
│
└── README.md
```

---

## 🚀 How to Run

```bash
cd stone_paper_scissors
python main.py
```

No external libraries required — uses only the Python standard library (`random`).

---

## 🎮 Features

| Feature | Detail |
|---|---|
| Menu-driven loop | `while True` loop in `main.py` |
| Random results | `random.choice()` in `game/logic.py` |
| Score tracking | `Scoreboard` class across rounds |
| Input validation | Re-prompts on invalid entry |
| Clean architecture | Logic never written directly in `main.py` |

---

## 📦 Package Architecture

| Package | Responsibility |
|---|---|
| `game/` | All game rules, random logic, score state |
| `utils/` | Display output and user input handling |
| `main.py` | Wires everything together via menu loop |

---

## 📋 Menu Options

```
1. Play a Round
2. View Scoreboard
3. Reset Scores
4. How to Play
5. Quit
```

---

## 🛠 Tech Stack

- **Language**: Python 3.x
- **Modules used**: `random` (standard library)
- **Architecture**: Package-based (no logic in main)
