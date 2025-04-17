"""
Rock Paper Scissors Game - Main Script
"""
from game.game import Game
from game.score import show_scores
from game.settings import MODES


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 40)
    print("ROCK PAPER SCISSORS ADVENTURE")
    print("=" * 40)
    print("1. Start New Game")
    print("2. View High Scores")
    print("3. Settings")
    print("4. Exit")  
    print("=" * 40)


def select_mode():
    """Let the player select a game mode"""
    print("\nSelect Mode:")
    for key, mode in MODES.items():
        print(f"{key}. {mode}")
    
    while True:
        choice = input("Enter choice: ")
        if choice in MODES:
            return MODES[choice]
        print("Invalid choice. Please try again.")


def main():
    """Main function to run the game"""
    while True:
        display_menu()
        
        choice = input("\nEnter choice (1-4): ")

        if choice == '1':
            name = input("\nEnter your name: ")
            mode = select_mode()

            from game.settings import SettingsManager
            if 'settings' not in globals():
                global settings
                settings = SettingsManager()

            game = Game(name, mode, settings)
            game.start()


        elif choice == '2':
            show_scores()

        elif choice == '3':
            from game.settings import SettingsManager
            settings = SettingsManager()
            settings.update()

        elif choice == '4':
            print("\nThanks for playing! Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()