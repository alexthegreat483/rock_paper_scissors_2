"""
Models for Rock Paper Scissors game
"""
import random
from .settings import PLAYER_LIVES, ENEMY_LIVES

class Player:
    """Player class"""
    def __init__(self, name, difficulty):
        self.name = name
        self.lives = PLAYER_LIVES[difficulty]
        self.score = 0
        
    def choose_move(self):
        """Get player's move"""
        while True:
            try:
                choice = int(input("\nChoose (1-Rock, 2-Paper, 3-Scissors): "))
                if choice == 1:
                    return "rock"
                elif choice == 2:
                    return "paper"
                elif choice == 3:
                    return "scissors"
                else:
                    print("Please enter 1, 2 or 3.")
            except ValueError:
                print("Please enter a number.")

class Enemy:
    """Enemy class"""
    def __init__(self, level, difficulty):
        self.level = level
        self.difficulty = difficulty
        
        if difficulty == "easy":
            self.lives = ENEMY_LIVES["easy"]
        elif difficulty == "normal":
            self.lives = level
        else:  
            self.lives = level * 2
    
    def choose_move(self):
        """Choose enemy's move"""
        return random.choice(["rock", "paper", "scissors"])