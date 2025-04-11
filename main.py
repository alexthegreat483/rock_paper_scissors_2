#!/usr/bin/env python3
"""
Rock Paper Scissors Game - Main Script
"""
from game.game import Game

def main():
    print("\n===== ROCK PAPER SCISSORS GAME =====")
    
    name = input("Enter your name: ")
    
    print("\nChoose difficulty:")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")
    choice = input("Enter choice (1-3): ")
    
    if choice == "3":
        difficulty = "hard"
    elif choice == "2":
        difficulty = "normal"
    else:
        difficulty = "easy"
    
    game = Game(name, difficulty)
    game.start()
    
    from game.score import show_scores
    show_scores()
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()