"""
Score handling for Rock Paper Scissors game
"""
from .settings import SCORE_FILE

def save_score(name, difficulty, level, score):
    """Save player's score"""
    try:
        with open(SCORE_FILE, "a") as file:
            file.write(f"{name},{difficulty},{score}\n")
        print(f"Score saved: {score} points")
    except Exception as e:
        print(f"Could not save score: {e}")

def show_scores():
    """Display high scores"""
    try:
        scores = []
        with open(SCORE_FILE, "r") as file:
            for line in file:
                if line.strip():
                    name, diff, level, score = line.strip().split(",")
                    scores.append((name, diff, int(level), int(score)))
    except FileNotFoundError:
        print("\nNo scores yet!")
        return
    except Exception as e:
        print(f"Error reading scores: {e}")
        return
        
    scores.sort(key=lambda x: x[3], reverse=True)
    
    print("\n===== HIGH SCORES =====")
    for i, (name, diff, level, score) in enumerate(scores[:5], 1):
        print(f"{i}. {name} - {diff} mode - Level {level} - {score} points")
    print("=====================")