from tree import Node


class KnightPathFinder(Node):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        if coordinates < (0, 0) or coordinates > (8, 8):
            self._root = Node((0.0))
        self._root = Node(coordinates)
        self._considered_positions = {coordinates}

    def get_valid_moves(self, pos):
        valid = []
        board = [(x, y) for x in range(0, 8) for y in range(0, 8)]
        for square in board:
            res = tuple(map(lambda i, j: abs(i - j), pos, square))
            if res == (1, 2) or res == (2, 1):
                valid.append(square)
        return valid

    def new_move_positions(self, pos):
        res = set(self.get_valid_moves(pos))
        newMoves = res - self._considered_positions
        self._considered_positions.update(res)
        return newMoves

    def build_move_tree(self):
        queue = [self._root]
        while len(queue):
            currentNode = queue.pop(0)
            moves = self.new_move_positions(currentNode.value)
            for move in moves:
                newNode = Node(move)
                currentNode.add_child(newNode)
                queue.append(newNode)


finder = KnightPathFinder((0, 0))
# Expected outcome: {(1, 2), (2, 1)}
# print(finder.new_move_positions((0, 0)))
finder.build_move_tree()
# print(finder._root._value)
print(finder._root.children)
