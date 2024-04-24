import random
import numpy as np
from copy import deepcopy

class Sudoku:
    def __init__(self):
        self.board = [[0]*9 for _ in range(9)]

    def generate(self):
        pass 

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- " * 11)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.board[i][j], end=" ")
            print()

    def is_valid_move(self, row, col, num):
        return self.is_valid_row(row, num) and self.is_valid_col(col, num) and self.is_valid_subgrid(row - row % 3, col - col % 3, num)

    def is_valid_row(self, row, num):
        return num not in self.board[row]

    def is_valid_col(self, col, num):
        return all(row[col] != num for row in self.board)

    def is_valid_subgrid(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if self.board[i + row][j + col] == num:
                    return False
        return True

    def solve(self):
        pass  

    def generate_full_board(self):
        pass  

    def remove_cells(self, num_cells_to_remove):
        pass  

def main():
    game = Sudoku()
    game.generate_full_board()
    game.remove_cells(50) 
    game.print_board()

    while True:
        row = int(input("Enter row (1-9): ")) - 1
        col = int(input("Enter column (1-9): ")) - 1
        num = int(input("Enter number (1-9): "))

        if game.is_valid_move(row, col, num):
            game.board[row][col] = num
            game.print_board()
        else:
            print("Invalid move. Try again.")

        if all(0 not in row for row in game.board):
            print("Congratulations! You solved the puzzle   .")
            break

if __name__ == "__main__":
    main()
