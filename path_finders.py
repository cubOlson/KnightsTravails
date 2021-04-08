from tree import Node 

class KnightPathFinder(Node):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self._root = Node(coordinates)
        self._considered_positions = {self._root}

    def get_valid_moves(self, pos):
        valid = []
        board = [(x,y) for x in range(0,8) for y in range(0,8)]   
        for square in board:
            res = tuple(map(lambda i, j: abs(i - j), pos, square))
            if res == (1,2) or res == (2,1):
                valid.append(square)
        return valid

# a = (10, 7)
# b = (11, 5)

# res = tuple(map(lambda i, j: abs(i - j), a, b))

# print(res)

node1 = KnightPathFinder((0,0))
print(node1.get_valid_moves((2,2)))