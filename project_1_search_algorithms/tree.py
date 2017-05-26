from node import Node
from node_heuristic import NodeHeuristic

class Tree:
    def __init__(self):
        self.frontier = []
        self.expanded = []
        self.max_depth = 0
        self.nodes = {}

    def add(self, node):
        if self.max_depth < node.depth:
            self.max_depth = node.depth

        self.nodes[node.id] = node

    def find(self, board):
        id = ','.join(map(str, board))
        return self.nodes.get(id, None)

    def has_frontier(self):
        return len(self.frontier) > 0

    def already_added(self, node):
        return self.find(node.board) != None

    def path_to_goal(self):
        if self.result == None: return ''

        all_moves = []
        node = self.result

        while True:
            if node.parent == None: break
            all_moves.insert(0, node)
            node = node.parent

        return all_moves


