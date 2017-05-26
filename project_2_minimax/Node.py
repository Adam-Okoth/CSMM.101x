class Node:
    def __init__(self, parent, grid):
        self.parent = parent
        self.grid = grid

        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0
