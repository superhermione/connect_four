from colors import MyColors
c = MyColors

class ConnectFour:
   
    def __init__(self):
        self.dimensions = ' 6 rows by 7 columns'
        self.cols_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g':6}
        self.board = {}
        self.game_history = []
        self.turn = 1
        for row in range(5, -1, -1):
            for col in range(7):
                self.board[int(str(row) + str(col))] = '.'


    def update_turn(self):
        self.turn *= -1
           
    def next_available(self, col):
        num_col = 50 + (self.cols_dict[col])
        for spot in range(num_col, num_col-60, -10):
            if self.board[spot] == '.':
                return spot
        return None
       
    def place_chip(self, letter_col):
        col = self.cols_dict[letter_col]
        spot = self.next_available(letter_col)
        if self.turn == 1:
            self.board[spot] = 'R'
            self.game_history.append((spot, 'R'))
        if self.turn == -1:
            self.board[spot] = 'Y'
            self.game_history.append((spot, 'Y'))
               
        self.turn *= -1
        
         
    def row_win(self):
        for row in range(0, 6):
            for col in range(0, 4):
                if self.board[int(str(row)+str(col))] != '.':
                    if self.board[int(str(row)+str(col))] == self.board[int(str(row)+str(col+1))] == self.board[int(str(row)+str(col+2))] == self.board[int(str(row)+str(col+3))]:
                        return True
        return False
       
    def col_win(self):
        for col in range(0,7):
            for row in range(0, 3):
                if self.board[int(str(row)+str(col))] != '.':
                    if self.board[int(str(row)+str(col))] == self.board[int(str(row+1)+str(col))]==self.board[int(str(row+2)+str(col))]==self.board[int(str(row+3)+str(col))]:
                        return True
        return False
       
    def diagonal_ur_win(self):
        starters = [30, 40, 31, 50, 41, 32, 51, 42, 33, 52, 43, 53]
        for start in starters:
            if self.board[start] != '.':
                if self.board[start] == self.board[start - 9] == self.board[start - 18] == self.board[start - 27]:
                    return True
        return False
       
    def diagonal_dr_win(self):
        starters = [20, 10, 21, 0, 11, 22, 1, 12, 23, 2, 13, 3]
        for start in starters:
            if self.board[start] != '.':
                if self.board[start] == self.board[start + 11] == self.board[start + 22] == self.board[start + 33]:
                    return True
        return False
       
    def on_board(num):
        return num in list(self.board.keys())
       
    def print_board(self):
        print("a  b  c  d  e  f  g")
        for row in range(6):
            for col in range(7):
                if col == 6:
                    if self.board[int(str(row) + str(col))] == 'R':
                        print(f"{c.red}{'o'}{c.end}", end="  ")
                    elif self.board[int(str(row) + str(col))] == 'Y':                    
                        print(f"{c.yellow}{'o'}{c.end}", end="  ")
                    else:
                        print(self.board[int(str(row)+str(col))], end="  ")
                    print("\n")

                else:
                    if self.board[int(str(row) + str(col))] == 'R':
                        print(f"{c.red}{'o'}{c.end}", end="  ")
                    elif self.board[int(str(row) + str(col))] == 'Y':                    
                        print(f"{c.yellow}{'o'}{c.end}", end="  ")
                    else:
                        print(self.board[int(str(row)+str(col))], end="  ")
    
    def valid_choice(self, selection):
        if selection.isnumeric():
            return False
        
        if len(selection) > 1:
            return False
        
        if selection not in list(self.cols_dict.keys()):
            return False
            
        if self.next_available(selection) is None:
            return False
        
        else:
            return True
    
    def connect_four(self):
        if self.col_win() or self.row_win() or self.diagonal_dr_win() or self.diagonal_ur_win():
            print("Connect Four!")
            return True
        else:
            return False
        
if __name__ == "__main__":
    
    game_over = False
    game = ConnectFour()
    game.print_board()
    while game_over is False:
        get_move = input("Choose a column to place a chip:  ")
        while game.valid_choice(get_move) is False: 
            get_move = input("Try an unfilled column from a to g:  ")
        game.place_chip(get_move)
        game.print_board()
        if game.connect_four():
            game_over = True
            game.update_turn()
            
    
    if game.turn == -1:
        print("Yellow won this time!")
    if game.turn == 1:
        print("Red won this time!")
