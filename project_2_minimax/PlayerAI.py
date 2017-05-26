from BaseAI import BaseAI
from ComputerAI import ComputerAI
from Node import Node

class PlayerAI(BaseAI):
    def getMove(self, grid):
        tree = self.build_tree(grid.clone())
        return 0

    def build_tree(self, grid):
        source = Node(None, grid)
        enqueued_nodes = [source]

        a = 0
        while len(enqueued_nodes) > 0:
            parent = enqueued_nodes.pop()

            if parent.depth == 5: continue

            a += 1
            for move in parent.grid.getAvailableMoves():
                # Do not forget to ignore nodes depth > N

                grid = self.next_grid(parent, move)

                if grid:
                    node = Node(parent, grid)
                    enqueued_nodes.append(node)

        print a
        return source

    def next_grid(self, node, person_move):
        available_cells = node.grid.getAvailableCells()
        lowest_heuristic = None
        computer_moved_grid = None

        for cell in available_cells:
            for i in [2,4]:
                temp_grid = node.grid.clone()
                temp_grid.insertTile(cell, i)
                temp_grid.move(person_move)

                heuristic = self.calculate_heuristic(temp_grid)

                if lowest_heuristic == None or heuristic < lowest_heuristic:
                    computer_moved_grid = temp_grid
                    lowest_heuristic = heuristic

        return computer_moved_grid

    def calculate_heuristic(self, grid):
        return len(grid.getAvailableCells()) + grid.getMaxTile()


