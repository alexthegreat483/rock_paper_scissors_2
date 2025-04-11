"""
Game logic for Rock Paper Scissors game
"""
from .models import Player, Enemy
from .score import save_score

class Game:
    """Game class"""
    def __init__(self, player_name, difficulty):
        self.player = Player(player_name, difficulty)
        self.difficulty = difficulty
        self.enemy_level = 1
        self.enemy = Enemy(self.enemy_level, difficulty)
    
    def start(self):
        """Start the game"""
        print(f"\nStarting game on {self.difficulty} mode")
        print(f"You have {self.player.lives} lives")
        print(f"Enemy has {self.enemy.lives} lives")
        
        while self.player.lives > 0:
            self._play_round()
            
        print("\nGAME OVER!")
        print(f"You reached enemy level {self.enemy_level}")
        print(f"Final score: {self.player.score}")
        
        save_score(
            self.player.name,
            self.difficulty,
            self.enemy_level,
            self.player.score
        )
    
    def _play_round(self):
        """Play one round"""
        print(f"\n--- Round ---")
        print(f"Your lives: {self.player.lives} | Score: {self.player.score}")
        print(f"Enemy level: {self.enemy_level} | Lives: {self.enemy.lives}")
    
        player_choice = self.player.choose_move()
        enemy_choice = self.enemy.choose_move()
        print(f"You chose: {player_choice}")
        print(f"Enemy chose: {enemy_choice}")
        
        if player_choice == enemy_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and enemy_choice == "scissors") or \
             (player_choice == "paper" and enemy_choice == "rock") or \
             (player_choice == "scissors" and enemy_choice == "paper"):
            print("You win this round!")
            self.enemy.lives -= 1
            self.player.score += 10
            
            if self.enemy.lives <= 0:
                bonus = self.enemy_level * 20
                self.player.score += bonus
                print(f"You defeated enemy level {self.enemy_level}!")
                print(f"Bonus points: +{bonus}")
                
                self.enemy_level += 1
                self.enemy = Enemy(self.enemy_level, self.difficulty)
                print(f"Next enemy (level {self.enemy_level}) has {self.enemy.lives} lives")
        else:
            print("You lose this round!")
            self.player.lives -= 1