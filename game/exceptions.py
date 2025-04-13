"""
Exceptions for Rock Paper Scissors game
"""

class GameError(Exception):
    """Base exception for all game errors"""
    pass


class InvalidChoiceError(GameError):
    """Raised when player makes an invalid choice"""
    pass