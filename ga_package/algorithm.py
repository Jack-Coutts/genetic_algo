import math
import random


# Create individuals and moves for first generation
class GenerationOne:

    # Initiate constructor
    def __init__(self, generation_size, step_num):  # Input size of generation & move number
        self.xy = xy  # [x, y] coordinates
        self.x = xy[0]  # Can call x or y individually
        self.y = xy[1]
        self.size = diameter  # Diameter of circle
        self.move_history = []  # Each previous move made by circle
        self.generation = 0  # Which generation
