"""
Models for Rock Paper Scissors game
Contains Player and Enemy classes
"""
import random
from .settings import (
    PLAYER_LIVES, HARD_MODE_MULTIPLIER, ALLOWED_ATTACKS,
    ATTACK_PAIRS_OUTCOME, WIN, LOSE, DRAW, MODE_HARD
)
from .exceptions import InvalidChoiceError


class Player:
    """Player class representing the human player"""
    
    def __init__(self, name, mode, lives=PLAYER_LIVES):
        self.name = name
        self.mode = mode
        self.lives = lives
        self.score = 0

    
    def choose_attack(self):
        """Get player's attack choice"""
        print("\nChoose your attack:")
        for key, attack in ALLOWED_ATTACKS.items():
            print(f"{key}. {attack}")
            
        choice = input("Enter choice: ")
        
        if choice in ALLOWED_ATTACKS:
            return ALLOWED_ATTACKS[choice]
        else:
            raise InvalidChoiceError("Invalid choice. Please try again.")
    
    def add_score(self, points):
        """Add points to player's score"""
        self.score += points
        return self.score


class Enemy:
    """Enemy class representing the computer opponent"""
    
    def __init__(self, level, mode):
        self.level = level
        self.mode = mode
        
        self.lives = level
        if mode == MODE_HARD:
            self.lives *= HARD_MODE_MULTIPLIER
    
    def choose_attack(self):
        """Choose a random attack"""
        return random.choice(list(ALLOWED_ATTACKS.values()))


def determine_outcome(player_attack, enemy_attack):
    """
    Determine the outcome of an attack
    
    Returns:
        WIN, LOSE, or DRAW constant
    """
    attack_pair = (player_attack, enemy_attack)
    return ATTACK_PAIRS_OUTCOME.get(attack_pair, DRAW)  