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
            file.write(f"{name},{mode},{level},{score}\n")
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
    """Display high scores"""
    scores = load_scores()
    
    if not scores:
        print("\nNo scores yet!")
        return
    
    scores.sort(key=lambda x: x[3], reverse=True)
    
    print(f"\n===== TOP {MAX_RECORDS_NUMBER} SCORES =====")
    print(f"{'#':<3}{'Name':<15}{'Mode':<10}{'Level':<8}{'Score':<8}")
    print("-" * 40)
    
    for i, (name, mode, level, score) in enumerate(scores[:MAX_RECORDS_NUMBER], 1):
        print(f"{i:<3}{name:<15}{mode:<10}{level:<8}{score:<8}")
    
    print("=" * 40)