class Node:
    def __init__(self, board, parent, move):
        self.board = board
        self.parent = parent
        self.move = move
        self.id = ','.join(map(str, board))

        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    def find_zero_pos(self):
        if getattr(self, 'tile_zero_pos', None) != None:
            return self.tile_zero_pos

        index = 0
        for value in self.board:
            if int(value) == 0:
                self.tile_zero_pos = index
                return self.tile_zero_pos
            index += 1

    def reached_goal(self):
        return self.id == '0,1,2,3,4,5,6,7,8'

    def valid_moves(self):
        zero_pos = self.find_zero_pos()
        valid_moves = ['Up', 'Down', 'Left', 'Right'] # Just for test
        column_pos = zero_pos % 3

        # Left Side of the board
        if column_pos == 0: valid_moves.remove('Left')
        # Right Side of the board
        if column_pos == 2: valid_moves.remove('Right')
        # Top of the board
        if (zero_pos - 3) < 0: valid_moves.remove('Up')
        # Bottom of the board
        if (zero_pos + 3) > 8: valid_moves.remove('Down')

        return valid_moves

    def children(self):
        zero_pos = self.find_zero_pos()
        children = []

        for move in self.valid_moves():
            new_board = list(self.board)

            if move == 'Up':
                value_up = new_board[zero_pos - 3]
                new_board[zero_pos - 3] = new_board[zero_pos]
                new_board[zero_pos] = value_up

            if move == 'Down':
                value_down = self.board[zero_pos + 3]
                new_board[zero_pos + 3] = new_board[zero_pos]
                new_board[zero_pos] = value_down

            if move == 'Left':
                value_left = self.board[zero_pos - 1]
                new_board[zero_pos - 1] = new_board[zero_pos]
                new_board[zero_pos] = value_left

            if move == 'Right':
                value_right = self.board[zero_pos + 1]
                new_board[zero_pos + 1] = new_board[zero_pos]
                new_board[zero_pos] = value_right

            children.append(self.__class__(new_board, self, move))

        return children
