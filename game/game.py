"""
Game logic for Rock Paper Scissors game
"""
from .models import Player, Enemy, determine_outcome
from .settings import SettingsManager
from .settings import (
    POINTS_FOR_FIGHT, POINTS_FOR_KILLING, 
    WIN, LOSE, DRAW
)
from .score import save_score
from .exceptions import InvalidChoiceError


class Game:
    """Main game class that controls the game flow"""
    
    def __init__(self, player_name, mode, settings):
        self.settings = settings
        self.player = Player(player_name, mode, self.settings.player_lives)
        self.mode = mode
        self.current_enemy_level = 1
        self.enemy = Enemy(self.current_enemy_level, mode)
    
    def start(self):
        """Start and run the game"""
        print(f"\nStarting game for {self.player.name} on {self.mode} mode")
        print(f"You have {self.player.lives} lives")
        print("Each round, choose your attack using the number keys")

        game_running = True
        while game_running and self.player.lives > 0:
            user_input = input("\nPress Enter to play next round or type 'settings' to edit settings: ")
            if user_input.lower() == 'settings':
                self.settings.update()
            continue

        game_running = self.play_round()


        print("\nGAME OVER")
        print(f"You reached enemy level {self.current_enemy_level}")
        print(f"Final score: {self.player.score}")

        save_score(
            self.player.name,
            self.mode,
            self.current_enemy_level,
            self.player.score
        )

    

    
    def display_status(self):
        """Display current game status"""
        print("\n" + "-" * 40)
        print(f"Player: {self.player.name} | Lives: {self.player.lives} | Score: {self.player.score}")
        print(f"Enemy Level: {self.current_enemy_level} | Lives: {self.enemy.lives}")
        print("-" * 40)
    
    def play_round(self):
        """Play a single round of the game"""
        self.display_status()
        
        try:
            player_attack = self.player.choose_attack()
            enemy_attack = self.enemy.choose_attack()
            
            print(f"\nYou chose: {player_attack}")
            print(f"Enemy chose: {enemy_attack}")
            
            outcome = determine_outcome(player_attack, enemy_attack)
            
            if outcome == WIN:
                print("You win this round!")
                self.enemy.lives -= 1
                self.player.add_score(self.settings.points_for_fight)
                
                if self.enemy.lives <= 0:
                    enemy_bonus = self.settings.points_for_killing * self.current_enemy_level
                    self.player.add_score(enemy_bonus)
                    print(f"\nYou defeated enemy level {self.current_enemy_level}!")
                    print(f"Bonus points: +{enemy_bonus}")
                    
                    self.current_enemy_level += 1
                    self.enemy = Enemy(self.current_enemy_level, self.mode)
                    print(f"Prepare to face enemy level {self.current_enemy_level}!")
                    
            elif outcome == LOSE:
                print("You lose this round!")
                self.player.lives -= 1
                
                if self.player.lives <= 0:
                    return False
                    
            else:  
                print("It's a tie!")
                
            return True
            
        except InvalidChoiceError as e:
            print(f"Error: {e}")
            return True  
    
    def start(self):
        """Start and run the game"""
        print(f"\nStarting game for {self.player.name} on {self.mode} mode")
        print(f"You have {self.player.lives} lives")
        print("Each round, choose your attack using the number keys")
        
        game_running = True
        while game_running and self.player.lives > 0:
            game_running = self.play_round()
            
        print("\nGAME OVER")
        print(f"You reached enemy level {self.current_enemy_level}")
        print(f"Final score: {self.player.score}")
        
        save_score(
            self.player.name,
            self.mode,
            self.current_enemy_level,
            self.player.score
        )