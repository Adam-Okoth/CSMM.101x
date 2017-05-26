from node import Node

class NodeHeuristic(Node):
    def __init__(self, board, parent, move):
        Node.__init__(self, board, parent, move)
        self.calculate_distance_to_goal()

    def calculate_distance_to_goal(self):
        if hasattr(self, 'distance_to_goal'): return self.distance_to_goal

        total_distance = self.depth - 1 # Steps walked so far
        current_pos = 0

        for tile in self.board:
            tile = int(tile)
            if tile != 0:
                # Check how many ups and downs
                current_row = current_pos / 3
                expected_row = tile / 3
                total_distance += abs(expected_row - current_row)

                # Check how many lefts and rights
                current_column = current_pos % 3
                expected_column = tile % 3
                total_distance += abs(expected_column - current_column)

            current_pos += 1

        self.distance_to_goal = total_distance

    def __cmp__(self, other):
        if other:
            compare_distance = cmp(self.distance_to_goal, other.distance_to_goal)
            if compare_distance == 0:
                return cmp(self.depth, other.depth)
            else:
                return compare_distance;
        else:
            return 1
