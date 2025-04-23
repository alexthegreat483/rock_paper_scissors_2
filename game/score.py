"""
Score handling for Rock Paper Scissors game
"""
from .settings import SCORE_FILE, MAX_RECORDS_NUMBER


def save_score(name, mode, level, score):
    """
    Save player's score to the score file
    
    Args:
        name: Player's name
        mode: Game mode
        level: Enemy level reached
        score: Final score
    """
    try:
        with open(SCORE_FILE, "a") as file:
            file.write(f"{name:<15} | {mode:<8} | {level:<5} | {score:<5}\n")
        print(f"Score saved: {score} points")
    except Exception as e:
        print(f"Could not save score: {e}")


def load_scores():
    """
    Load scores from the score file
    
    Returns:
        List of score tuples (name, mode, level, score)
    """
    scores = []
    try:
        with open(SCORE_FILE, "r") as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(",")
                    if len(parts) >= 4:
                        name, mode, level, score = parts[:4]
                        try:
                            scores.append((name, mode, int(level), int(score)))
                        except ValueError:
                            continue
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error loading scores: {e}")
    
    return scores


def show_scores():
    """Display high scores in a structured format"""
    try:
        with open(SCORE_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("\nNo scores yet!")
        return

    if not lines:
        print("\nNo scores yet!")
        return

    print("\n===== GAME SCORE DATABASE =====")
    print(f"{'Player Name':<15} | {'Mode':<8} | {'Level':<5} | {'Score':<5}")
    print("-" * 45)
    for line in lines:
        print(line.strip())
    print("=" * 45)
