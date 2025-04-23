"""
Settings file for Rock Paper Scissors game
this is where u can customize the game and do what u want with it
"""

MODE_NORMAL = 'Normal'
MODE_HARD = 'Hard'
MODES = {
    '1': MODE_NORMAL,
    '2': MODE_HARD
}

PLAYER_LIVES = 2  
POINTS_FOR_FIGHT = 1  
POINTS_FOR_KILLING = 5  
MAX_RECORDS_NUMBER = 5  
HARD_MODE_MULTIPLIER = 2  

SCORE_FILE = 'scores.txt'

PAPER = 'Paper'
STONE = 'Stone'
SCISSORS = 'Scissors'

WIN = 1
DRAW = 0
LOSE = -1

ALLOWED_ATTACKS = {
    '1': PAPER,
    '2': STONE,
    '3': SCISSORS
}

ATTACK_PAIRS_OUTCOME = {
    (PAPER, PAPER): DRAW,
    (PAPER, STONE): WIN,
    (PAPER, SCISSORS): LOSE,
    (STONE, PAPER): LOSE,
    (STONE, STONE): DRAW,
    (STONE, SCISSORS): WIN,
    (SCISSORS, PAPER): WIN,
    (SCISSORS, STONE): LOSE,
    (SCISSORS, SCISSORS): DRAW
}

class SettingsManager:
    def __init__(self):
        self.player_lives = PLAYER_LIVES
        self.points_for_fight = POINTS_FOR_FIGHT
        self.points_for_killing = POINTS_FOR_KILLING

    def show(self):
        print("\nCurrent Game Settings:")
        print(f"1. Player Lives: {self.player_lives}")
        print(f"2. Points for Winning a Round: {self.points_for_fight}")
        print(f"3. Points for Killing an Enemy: {self.points_for_killing}")
        print("4. Exit settings")

    def update(self):
        while True:
            self.show()
            choice = input("Enter setting number to change or 4 to exit: ")
            try:
                if choice == "1":
                    new_lives = int(input("Enter new number of lives: "))
                    self.player_lives = new_lives
                elif choice == "2":
                    new_fight_score = int(input("Enter new points for winning a round: "))
                    self.points_for_fight = new_fight_score
                elif choice == "3":
                    new_kill_score = int(input("Enter new points for killing an enemy: "))
                    self.points_for_killing = new_kill_score
                elif choice == "4":
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

