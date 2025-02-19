import random

class RockPaperScissors:
    def __init__(self, rounds):
        self.rounds = rounds  # total number of rounds
        self.current_round = 1  # start at the first round
        self.player_wins = 0  # player wins counter
        self.computer_wins = 0  # computer wins counter

    def get_computer_choice(self):
        """Generate a random choice for the computer (rock, paper, or scissors)."""
        return random.choice(['rock', 'paper', 'scissors'])

    def find_winner(self, player_choice, computer_choice):
        """Determine the winner of the current round."""
        if player_choice == computer_choice:
            return "It's a tie!"
        
        # Determine winner based on game rules
        if (player_choice == 'rock' and computer_choice == 'scissors') or \
           (player_choice == 'paper' and computer_choice == 'rock') or \
           (player_choice == 'scissors' and computer_choice == 'paper'):
            self.player_wins += 1
            return "Player wins this round!"
        else:
            self.computer_wins += 1
            return "Computer wins this round!"

    def check_game_winner(self):
        """Check if the game has a winner or is still ongoing."""
        if self.player_wins > self.computer_wins:
            return "Player wins the game!"
        elif self.computer_wins > self.player_wins:
            return "Computer wins the game!"
        elif self.current_round > self.rounds:
            if self.player_wins == self.computer_wins:
                return "It's a tie game!"
            return "It's still ongoing, but no more rounds left."
        else:
            return "Game is still ongoing."

    def play_round(self, player_choice):
        """Play a round of the game."""
        if self.current_round > self.rounds:
            return "Game over! All rounds have been played."
        
        # Get computer's choice
        computer_choice = self.get_computer_choice()
        
        # Find the winner of the current round
        round_result = self.find_winner(player_choice, computer_choice)
        
        # Increment current round
        self.current_round += 1
        
        # Return round result
        return round_result

    def get_game_status(self):
        """Return the current status of the game."""
        return {
            "Round": self.current_round - 1,
            "Player Wins": self.player_wins,
            "Computer Wins": self.computer_wins,
            "Rounds Remaining": self.rounds - (self.current_round - 1)
        }

# Example usage
game = RockPaperScissors(5)  # 5 rounds
print(game.play_round('rock'))  # Example round
print(game.get_game_status())
print(game.check_game_winner())  # Check if someone has won the game
