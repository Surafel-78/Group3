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
