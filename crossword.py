# Crossword Created by Group 3 Computer Science Students

import random

class CrosswordGenerator:
    def __init__(self, words):
        self.words = words
        self.max_len = max(len(word) for word in words)
        self.grid_size = self.max_len + 2
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
    
    def place_word(self, word, direction, start_row, start_col):
        if direction == 'horizontal':
            for i, letter in enumerate(word):
                self.grid[start_row][start_col + i] = letter
        elif direction == 'vertical':
            for i, letter in enumerate(word):
                self.grid[start_row + i][start_col] = letter
    def can_place_word(self, word, direction, start_row, start_col):
        if direction == 'horizontal':
            if start_col + len(word) >= self.grid_size:
                return False
            for i in range(len(word)):
                if self.grid[start_row][start_col + i] != ' ':
                    return False
        elif direction == 'vertical':
            if start_row + len(word) >= self.grid_size:
                return False
            for i in range(len(word)):
                if self.grid[start_row + i][start_col] != ' ':
                    return False
        return True
    def generate_crossword(self):
        random.shuffle(self.words)
        for word in self.words:
            placed = False
            while not placed:
                direction = random.choice(['horizontal', 'vertical'])
                if direction == 'horizontal':
                    start_row = random.randint(1, self.grid_size - 2)
                    start_col = random.randint(1, self.grid_size - len(word) - 1)
                elif direction == 'vertical':
                    start_row = random.randint(1, self.grid_size - len(word) - 1)
                    start_col = random.randint(1, self.grid_size - 2)
                
                if self.can_place_word(word, direction, start_row, start_col):
                    self.place_word(word, direction, start_row, start_col)
                    placed = True
        
        self.fill_random_letters()
    def fill_random_letters(self):
        for r in range(1, self.grid_size - 1):
            for c in range(1, self.grid_size - 1):
                if self.grid[r][c] == ' ':
                    self.grid[r][c] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

   def print_grid(self): 
        print("   ", end="") 
        for col in range(self.grid_size): 
            print(f"{col:2}", end=" ") 
        print() 
        for row in range(self.grid_size): 
            print(f"{row:2} ", end="") 
            for col in range(self.grid_size): 
                print(f"{self.grid[row][col]}  ", end="") 
            print()
if name == 'main': 
    words = ['PYTHON', 'CROSSWORD', 'PUZZLE', 'GRID', 'WORDS'] 
    generator = CrosswordGenerator(words) 
    generator.generate_crossword() 
    generator.print_grid()
