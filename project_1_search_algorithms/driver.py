import sys
import time
import resource
import Queue
from node import Node
from node_heuristic import NodeHeuristic
from tree import Tree

def ast(board_state):
    'Uses A* to search for solution'

    startTime = time.time()
    tree = Tree()
    tree.add(NodeHeuristic(board_state, None, None))
    tree.frontier = Queue.PriorityQueue()
    tree.frontier.put(tree.find(board_state))

    result = None

    while tree.frontier.empty() == False:
        current_node = tree.frontier.get()

        if current_node.reached_goal():
            tree.result = current_node
            break

        children = current_node.children()

        for child in children:
            if tree.already_added(child) == False:
                tree.add(child)
                tree.frontier.put(child);

        tree.expanded.append(current_node)

    elapsed_time = time.time() - startTime

    tree.total_time = elapsed_time
    build_file(tree)

def bfs(board_state):
    'Uses Breadth First Search to search for solution'

    startTime = time.time()
    tree = Tree()
    tree.add(Node(board_state, None, None))
    tree.frontier.append(tree.find(board_state))

    result = None

    while tree.has_frontier():
        current_node = tree.frontier.pop(0)

        if current_node.reached_goal():
            tree.result = current_node
            break

        children = current_node.children()

        for child in children:
            if tree.already_added(child) == False:
                tree.add(child)
                tree.frontier.append(child);

        tree.expanded.append(current_node)

    elapsed_time = time.time() - startTime

    tree.total_time = elapsed_time
    build_file(tree)

def dfs(board_state):
    'Uses Depth First Search to search for solution'

    startTime = time.time()
    tree = Tree()
    tree.add(Node(board_state, None, None))
    tree.frontier.append(tree.find(board_state))

    result = None

    while tree.has_frontier():
        current_node = tree.frontier.pop(0)

        if current_node.reached_goal():
            tree.result = current_node
            break

        children = current_node.children()

        for child in children[::-1]:
            if tree.already_added(child) == False:
                tree.add(child)
                tree.frontier.insert(0, child)

        tree.expanded.append(current_node)

    elapsed_time = time.time() - startTime

    tree.total_time = elapsed_time
    build_file(tree)

def build_file(tree):
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
    file = open('output.txt', 'w')
    path_to_goal = tree.path_to_goal()

    file.write('path_to_goal: %s\n' % map(lambda node: node.move, path_to_goal))
    file.write('cost_of_path: %s\n' % len(path_to_goal))
    file.write('nodes_expanded: %s\n' % len(tree.expanded))
    file.write('search_depth: %s\n' % tree.result.depth)
    file.write('max_search_depth: %s\n' % tree.max_depth)
    file.write('running_time: %s\n' % tree.total_time)
    file.write('max_ram_usage: %s\n' % memory_usage)

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2].split(','))
