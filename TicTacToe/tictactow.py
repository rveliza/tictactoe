from random import randint
import os

greeting_message = """
***********************************************************************
*     *****  *****  *****   ***** ***** *****   ***** ***** *****     * 
*       *      *    *         *   *   * *         *   *   * *         *
*       *      *    *         *   ***** *         *   *   * ***       *
*       *      *    *         *   *   * *         *   *   * *         *
*       *    *****  *****     *   *   * *****     *   ***** *****     *
***********************************************************************
                       Welcome to the game!  
"""


class Player:
    def __init__(self, name: str, tile: str):
        self.name = name
        self.tile = tile
        self.points = 0
        self.is_active_player = False
    
    def __repr__(self):
        return f"{self.name} is playing '{self.tile}' and has {self.points} points. Active player: {self.is_active_player}"
    
    def add_point(self):
        self.points += 1
    
    def switch_active(self):
        if self.is_active_player == False:
            self.is_active_player = True
        else:
            self.is_active_player = False
    
    def reset_points(self):
        self.points = 0


class Game:
    def __init__(self, player_1: object, player_2: object):
        self.board = [
    [" ", "|", " ", "|", " "],
    ["-", "-", "-", "-", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "-", "-", "-", "-"],
    [" ", "|", " ", "|", " "]
]
        self.player_1 = player_1
        self.player_2 = player_2
        self.players = [player_1, player_2]

        self.available_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    def __repr__(self):
        return "Tic Tac Toe Game Class"
    
    def print_board(self):
        print("\n")
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print("\n")

    def add_tile(self, player: object, position: str):
        position = int(position)
        if position == 7:
            self.board[0][0] = player.tile
            self.available_positions.remove(str(position))
        if position == 8:
            self.board[0][2] = player.tile
            self.available_positions.remove(str(position))
        if position == 9:
            self.board[0][4] = player.tile
            self.available_positions.remove(str(position))
        if position == 4:
            self.board[2][0] = player.tile
            self.available_positions.remove(str(position))
        if position == 5:
            self.board[2][2] = player.tile
            self.available_positions.remove(str(position))
        if position == 6:
            self.board[2][4] = player.tile
            self.available_positions.remove(str(position))
        if position == 1:
            self.board[4][0] = player.tile
            self.available_positions.remove(str(position))
        if position == 2:
            self.board[4][2] = player.tile
            self.available_positions.remove(str(position))
        if position == 3:
            self.board[4][4] = player.tile
            self.available_positions.remove(str(position))
        

    def check_if_full_board(self):
        if len(self.available_positions) == 0:
            return True
        return False
    
    def check_if_winner(self, tile: str):
        # Top Row
        if self.board[0][0] == tile and self.board[0][2] == tile and self.board[0][4] == tile:
            return True
        # Middle Row
        if self.board[2][0] == tile and self.board[2][2] == tile and self.board[2][4] == tile:
            return True
        # Bottom Row
        if self.board[4][0] == tile and self.board[4][2] == tile and self.board[4][4] == tile:
            return True
        # Left Col
        if self.board[0][0] == tile and self.board[2][0] == tile and self.board[4][0] == tile:
            return True
        # Middle Col
        if self.board[0][2] == tile and self.board[2][2] == tile and self.board[4][2] == tile:
            return True
        # Right Col
        if self.board[0][4] == tile and self.board[2][4] == tile and self.board[4][4] == tile:
            return True
        # Diag 1
        if self.board[0][0] == tile and self.board[2][2] == tile and self.board[4][4] == tile:
            return True
        # Diag 2
        if self.board[4][0] == tile and self.board[2][2] == tile and self.board[0][4] == tile:
            return True
        return False
    
    def check_if_tie(self):
        full_board = self.check_if_full_board()
        winner = self.check_if_winner
        if full_board and not winner:
            return True
        return False
    
    def reset_board(self):
        self.board = [
    [" ", "|", " ", "|", " "],
    ["-", "-", "-", "-", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "-", "-", "-", "-"],
    [" ", "|", " ", "|", " "]
]
    def clear_screen(self):
        os.system('clear')

    def random_player(self):
        random_number = randint(0, 1)
        if random_number == 0:
            self.player_1.is_active_player = True
        else:
            self.player_2.is_active_player = True

    def show_score(self):
        st_desc = f"{self.player_1.name}: {self.player_1.points} vs {self.player_2.name}: {self.player_2.points}"
        if self.player_1.points == self.player_2.points:
            st_desc += ". Tie"
        elif self.player_1.points > self.player_2.points:
            st_desc += f". {self.player_1} winning!"
        else:
            st_desc += f". {self.player_2} winning!"
        print(st_desc)

    def select_active_player(self):
        for player in self.players:
            if player.is_active_player:
                return player

    def show_active_player(self, player):
        print(f"{player.name}'s turn, using '{player.tile}'")

    def show_available_moves(self):
        return input(f"Choose an available space: {self.available_positions} ")
        
    
            
######### INITIAL SETUP ################
os.system('clear')
print(greeting_message)

# Create Players
x_player_name = input("Name for player playing 'X': ")
player_1 = Player(x_player_name, "X")

y_player_name = input("Name for player playing 'O': ")
player_2 = Player(y_player_name, "O")

# Create Game
ttt = Game(player_1, player_2)

# Randomly Choose First Player
ttt.random_player()

# First Move
ttt.clear_screen()
ttt.show_score()
ttt.print_board()
active_player = ttt.select_active_player()
ttt.show_active_player(active_player)

selected_position = ttt.show_available_moves()
ttt.add_tile(active_player, selected_position)
ttt.clear_screen()
ttt.print_board()

# Check if winner 

# If winner:
    # Add point to active player
    # Ask if continue playing
    # if yes
        # Reset Board
        # clear screen
        # random player
        # print score
        # print board
    # if no:
        # Exit game
        # print exit message and score
# If no winner:
    # clear screen
    # reverse players
    # print score
    # print board

# If Tie:
    # Ask if continue playing
    # If yes:
        # Reset Board
        # clear screen
        # random player
        # print score
        # print board
    # If no:
        # exit game
        # print exit message and score
# If no Tie:
    # clear screen
    # reverse players
    # print score
    # print board


