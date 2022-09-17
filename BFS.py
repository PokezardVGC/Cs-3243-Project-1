import sys


# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    def __init__(self, piece_type, x, y, max_x, max_y):
        self.piece_type = piece_type
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y

    def get_coord(self):
        return chr(self.x + 97), self.y

    def get_numeric_coord(self):
        return self.y, self.x

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_max_x(self):
        return self.max_x

    def get_max_y(self):
        return self.max_y


class King(Piece):
    def __init__(self, x, y, max_x, max_y):
        super().__init__('King', x, y, max_x, max_y)

    def get_actions(self):
        ls = []
        right = King(self.get_x() + 1, self.get_y(), self.get_max_x(), self.get_max_y())
        ls.append(right)
        left = King(self.get_x() - 1, self.get_y(), self.get_max_x(), self.get_max_y())
        ls.append(left)
        down = King(self.get_x(), self.get_y() - 1, self.get_max_x(), self.get_max_y())
        ls.append(down)
        up = King(self.get_x(), self.get_y() + 1, self.get_max_x(), self.get_max_y())
        ls.append(up)
        diag_left_up = King(self.get_x() - 1, self.get_y() + 1, self.get_max_x(), self.get_max_y())
        ls.append(diag_left_up)
        diag_right_up = King(self.get_x() + 1, self.get_y() + 1, self.get_max_x(), self.get_max_y())
        ls.append(diag_right_up)
        diag_left_down = King(self.get_x() - 1, self.get_y() - 1, self.get_max_x(), self.get_max_y())
        ls.append(diag_left_down)
        diag_right_down = King(self.get_x() + 1, self.get_y() - 1, self.get_max_x(), self.get_max_y())
        ls.append(diag_right_down)
        return ls


class Rook(Piece):
    def __init__(self, x, y, max_x, max_y, grid):
        super().__init__('Rook', x, y, max_x, max_y)
        self.grid = grid

    def get_actions(self):
        ls = []

        for i in range(self.get_x() - 1, -1, -1):
            if self.grid[self.get_y()][i] == -1:
                break
            piece = Rook(i, self.get_y(), self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)

        for i in range(self.get_x() + 1, self.get_max_x()):
            if self.grid[self.get_y()][i] == -1:
                break
            piece = Rook(i, self.get_y(), self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)

        for i in range(self.get_y() - 1, -1, -1):
            if self.grid[i][self.get_x()] == - 1:
                break
            piece = Rook(self.get_x(), i, self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)

        for i in range(self.get_y() + 1, self.get_max_y()):
            if self.grid[i][self.get_x()] == - 1:
                break
            piece = Rook(self.get_x(), i, self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)
        return ls


class Bishop(Piece):
    def __init__(self, x, y, max_x, max_y, grid):
        super().__init__('Bishop', x, y, max_x, max_y)
        self.grid = grid

    def get_actions(self):
        ls = []

        counter_2 = 0
        for i in range(self.x - 1, - 1, -1):
            counter_2 -= 1
            if len(self.grid) > self.y + counter_2:
                if self.grid[self.y + counter_2][i] == - 1:
                    break
                piece = Bishop(i, self.y + counter_2, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)

        counter_1 = 0
        for i in range(self.x + 1, self.get_max_x()):
            counter_1 += 1
            if len(self.grid) > self.y + counter_1:
                if self.grid[self.y + counter_1][i] == - 1:
                    break
                piece = Bishop(i, self.y + counter_1, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)

        counter_3 = 0
        for i in range(self.y - 1, - 1, -1):
            counter_3 += 1
            if len(self.grid[0]) > self.x + counter_3:
                if self.grid[i][self.x + counter_3] == -1:
                    break
                piece = Bishop(self.x + counter_3, i, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)

        counter_4 = 0
        for i in range(self.y + 1, self.get_max_y()):
            counter_4 += 1
            if self.x - counter_4 >= 0:
                if self.grid[i][self.x - counter_4] == -1:
                    break
                piece = Bishop(self.x - counter_4, i, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)

        return ls


class Queen(Piece):
    def __init__(self, x, y, max_x, max_y, grid):
        super().__init__("Queen", x, y, max_x, max_y)
        self.grid = grid

    def get_actions(self):
        ls = []

        #rook like movement
        for i in range(self.get_x() - 1, -1, -1):
            if self.grid[self.get_y()][i] == -1:
                break
            piece = Rook(i, self.get_y(), self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)
        for i in range(self.get_x() + 1, self.get_max_x()):
            if self.grid[self.get_y()][i] == -1:
                break
            piece = Rook(i, self.get_y(), self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)
        for i in range(self.get_y() - 1, -1, -1):
            if self.grid[i][self.get_x()] == - 1:
                break
            piece = Rook(self.get_x(), i, self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)
        for i in range(self.get_y() + 1, self.get_max_y()):
            if self.grid[i][self.get_x()] == - 1:
                break
            piece = Rook(self.get_x(), i, self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)

        #bishop like movement
        counter_2 = 0
        for i in range(self.x - 1, - 1, -1):
            counter_2 -= 1
            if len(self.grid) > self.y + counter_2:
                if self.grid[self.y + counter_2][i] == - 1:
                    break
                piece = Bishop(i, self.y + counter_2, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)
        counter_1 = 0
        for i in range(self.x + 1, self.get_max_x()):
            counter_1 += 1
            if len(self.grid) > self.y + counter_1:
                if self.grid[self.y + counter_1][i] == - 1:
                    break
                piece = Bishop(i, self.y + counter_1, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)
        counter_3 = 0
        for i in range(self.y - 1, - 1, -1):
            counter_3 += 1
            if len(self.grid[0]) > self.x + counter_3:
                if self.grid[i][self.x + counter_3] == -1:
                    break
                piece = Bishop(self.x + counter_3, i, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)
        counter_4 = 0
        for i in range(self.y + 1, self.get_max_y()):
            counter_4 += 1
            if self.x - counter_4 >= 0:
                if self.grid[i][self.x - counter_4] == -1:
                    break
                piece = Bishop(self.x - counter_4, i, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)
        return ls


class Knight(Piece):
    def __init__(self, x, y, max_x, max_y):
        super().__init__('Knight', x, y, max_x, max_y)

    def get_actions(self):
        ls = []
        top_left = Knight(self.get_x() - 1, self.get_y() + 2, self.get_max_x(), self.get_max_y())
        ls.append(top_left)
        top_right = Knight(self.get_x() + 1, self.get_y() + 2, self.get_max_x(), self.get_max_y())
        ls.append(top_right)
        bottom_left = Knight(self.get_x() - 1, self.get_y() - 2, self.get_max_x(), self.get_max_y())
        ls.append(bottom_left)
        bottom_right = Knight(self.get_x() + 1, self.get_y() - 2, self.get_max_x(), self.get_max_y())
        ls.append(bottom_right)

        left_top = Knight(self.get_x() - 2, self.get_y() + 1, self.get_max_x(), self.get_max_y())
        ls.append(left_top)
        left_top = Knight(self.get_x() - 2, self.get_y() - 1, self.get_max_x(), self.get_max_y())
        ls.append(left_top)
        right_top = Knight(self.get_x() + 2, self.get_y() + 1, self.get_max_x(), self.get_max_y())
        ls.append(right_top)
        right_top = Knight(self.get_x() + 2, self.get_y() - 1, self.get_max_x(), self.get_max_y())
        ls.append(right_top)
        return ls


class Ferz(Piece):
    def __init__(self, x, y, max_x, max_y):
        super().__init__('Ferz', x, y, max_x, max_y)

    def get_actions(self):
        ls = []
        diag_left_up = King(self.get_x() - 1, self.get_y() + 1, self.get_max_x(), self.get_max_y())
        ls.append(diag_left_up)
        diag_right_up = King(self.get_x() + 1, self.get_y() + 1, self.get_max_x(), self.get_max_y())
        ls.append(diag_right_up)
        diag_left_down = King(self.get_x() - 1, self.get_y() - 1, self.get_max_x(), self.get_max_y())
        ls.append(diag_left_down)
        diag_right_down = King(self.get_x() + 1, self.get_y() - 1, self.get_max_x(), self.get_max_y())
        ls.append(diag_right_down)
        return ls


class Princess(Piece):
    def __init__(self, x, y, max_x, max_y, grid):
        super().__init__('Princess', x, y, max_x, max_y)
        self.grid = grid

    def get_actions(self):
        ls = []
        # Bishop like movement
        counter_2 = 0
        for i in range(self.x - 1, - 1, -1):
            counter_2 -= 1
            if len(self.grid) > self.y + counter_2:
                if self.grid[self.y + counter_2][i] == - 1:
                    break
                piece = Bishop(i, self.y + counter_2, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)
        counter_1 = 0
        for i in range(self.x + 1, self.get_max_x()):
            counter_1 += 1
            if len(self.grid) > self.y + counter_1:
                if self.grid[self.y + counter_1][i] == - 1:
                    break
                piece = Bishop(i, self.y + counter_1, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)
        counter_3 = 0
        for i in range(self.y - 1, - 1, -1):
            counter_3 += 1
            if len(self.grid[0]) > self.x + counter_3:
                if self.grid[i][self.x + counter_3] == -1:
                    break
                piece = Bishop(self.x + counter_3, i, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)
        counter_4 = 0
        for i in range(self.y + 1, self.get_max_y()):
            counter_4 += 1
            if self.x - counter_4 >= 0:
                if self.grid[i][self.x - counter_4] == -1:
                    break
                piece = Bishop(self.x - counter_4, i, self.get_max_x(), self.get_max_y(), self.grid)
                ls.append(piece)

        top_left = Knight(self.get_x() - 1, self.get_y() + 2, self.get_max_x(), self.get_max_y())
        ls.append(top_left)
        top_right = Knight(self.get_x() + 1, self.get_y() + 2, self.get_max_x(), self.get_max_y())
        ls.append(top_right)
        bottom_left = Knight(self.get_x() - 1, self.get_y() - 2, self.get_max_x(), self.get_max_y())
        ls.append(bottom_left)
        bottom_right = Knight(self.get_x() + 1, self.get_y() - 2, self.get_max_x(), self.get_max_y())
        ls.append(bottom_right)

        left_top = Knight(self.get_x() - 2, self.get_y() + 1, self.get_max_x(), self.get_max_y())
        ls.append(left_top)
        left_top = Knight(self.get_x() - 2, self.get_y() - 1, self.get_max_x(), self.get_max_y())
        ls.append(left_top)
        right_top = Knight(self.get_x() + 2, self.get_y() + 1, self.get_max_x(), self.get_max_y())
        ls.append(right_top)
        right_top = Knight(self.get_x() + 2, self.get_y() - 1, self.get_max_x(), self.get_max_y())
        ls.append(right_top)
        return ls


class Empress(Piece):
    def __init__(self, x, y, max_x, max_y, grid):
        super().__init__('Empress', x, y, max_x, max_y)
        self.grid = grid

    def get_actions(self):
        ls = []
        # rook like movement
        for i in range(self.get_x() - 1, -1, -1):
            if self.grid[self.get_y()][i] == -1:
                break
            piece = Rook(i, self.get_y(), self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)
        for i in range(self.get_x() + 1, self.get_max_x()):
            if self.grid[self.get_y()][i] == -1:
                break
            piece = Rook(i, self.get_y(), self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)
        for i in range(self.get_y() - 1, -1, -1):
            if self.grid[i][self.get_x()] == - 1:
                break
            piece = Rook(self.get_x(), i, self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)
        for i in range(self.get_y() + 1, self.get_max_y()):
            if self.grid[i][self.get_x()] == - 1:
                break
            piece = Rook(self.get_x(), i, self.get_max_x(), self.get_max_y(), self.grid)
            ls.append(piece)

        # Knight like movement
        top_left = Knight(self.get_x() - 1, self.get_y() + 2, self.get_max_x(), self.get_max_y())
        ls.append(top_left)
        top_right = Knight(self.get_x() + 1, self.get_y() + 2, self.get_max_x(), self.get_max_y())
        ls.append(top_right)
        bottom_left = Knight(self.get_x() - 1, self.get_y() - 2, self.get_max_x(), self.get_max_y())
        ls.append(bottom_left)
        bottom_right = Knight(self.get_x() + 1, self.get_y() - 2, self.get_max_x(), self.get_max_y())
        ls.append(bottom_right)

        left_top = Knight(self.get_x() - 2, self.get_y() + 1, self.get_max_x(), self.get_max_y())
        ls.append(left_top)
        left_top = Knight(self.get_x() - 2, self.get_y() - 1, self.get_max_x(), self.get_max_y())
        ls.append(left_top)
        right_top = Knight(self.get_x() + 2, self.get_y() + 1, self.get_max_x(), self.get_max_y())
        ls.append(right_top)
        right_top = Knight(self.get_x() + 2, self.get_y() - 1, self.get_max_x(), self.get_max_y())
        ls.append(right_top)
        return ls


#############################################################################
######## Board
#############################################################################
class Board:
    def __init__(self, board, pieces):
        self.board = board

    def get_board(self):
        return self.board


#############################################################################
######## State
#############################################################################
class State:
    def __init__(self, board, own_piece, goals, max_y, max_x, path, action_cost):
        self.board = board
        self.own_piece = own_piece
        self.goals = goals
        self.max_x = max_x
        self.max_y = max_y
        self.path = path
        self.action_cost = action_cost

    #  multiple potential goals
    def is_goal(self):
        for goal in self.goals:
            if self.own_piece.get_numeric_coord() == goal:
                return True
        return False

    #  return list of all possible Piece positions to take
    def get_actions(self):

        # all possible pieces
        ls = self.own_piece.get_actions()  # regardless of legal
        ls = list(set(ls))  # remove duplicates

        # remove those pieces outside the board
        pieces = ls.copy()
        for piece in ls:
            # assume a is start
            if piece.get_x() + 1 > self.max_x or piece.get_x() < 0 or piece.get_y() - 1 < 0 or piece.get_y() + 1 > self.max_y:
                pieces.remove(piece)

        # remove pieces in obstacles
        copy_pieces = pieces.copy()
        for piece in copy_pieces:
            obstacle = self.board[piece.get_y()][piece.get_x()]
            is_obstacle = obstacle == -1
            if is_obstacle:
                pieces.remove(piece)
        # print([piece.get_coord() for piece in pieces])
        return pieces

    #  return all transition states that are legal
    def get_transition(self):
        transitions = []
        for piece in self.get_actions():
            cost = self.board[piece.get_y()][piece.get_x()]
            new_path = self.path.copy()
            new_path.append(piece.get_coord())
            new_state = State(self.board, piece, self.goals, self.max_x, self.max_y,
                              new_path, self.action_cost + cost)
            transitions.append(new_state)
        return transitions

    def get_path(self):
        return self.path

    def get_action_cost(self):
        return self.action_cost


#############################################################################
######## Implement Search Algorithm
#############################################################################
def search(cols, rows, grid, enemy_pieces, own_pieces, goals):
    own_piece = King(own_pieces[0][1][1], own_pieces[0][1][0], cols, rows)
    enemy_pieces_list = []
    for enemy in enemy_pieces:
        piece = "error"
        if enemy[0] == "King":
            piece = King(enemy[1][1], enemy[1][0], cols, rows)
            enemy_pieces_list.append(piece)
        if enemy[0] == "Rook":
            piece = Rook(enemy[1][1], enemy[1][0], cols, rows, grid)
            enemy_pieces_list.append(piece)
        if enemy[0] == "Bishop":
            piece = Bishop(enemy[1][1], enemy[1][0], cols, rows, grid)
            enemy_pieces_list.append(piece)
        if enemy[0] == "Queen":
            piece = Queen(enemy[1][1], enemy[1][0], cols, rows, grid)
            enemy_pieces_list.append(piece)
        if enemy[0] == "Knight":
            piece = Knight(enemy[1][1], enemy[1][0], cols, rows)
            enemy_pieces_list.append(piece)
        if enemy[0] == "Ferz":
            piece = Ferz(enemy[1][1], enemy[1][0], cols, rows)
            enemy_pieces_list.append(piece)
        if enemy[0] == "Princess":
            piece = Princess(enemy[1][1], enemy[1][0], cols, rows, grid)
            enemy_pieces_list.append(piece)
        if enemy[0] == "Empress":
            piece = Empress(enemy[1][1], enemy[1][0], cols, rows, grid)
            enemy_pieces_list.append(piece)

    def enemy_positions(enemy_pieces_list):
        enemy_moves = []
        for enemy_piece in enemy_pieces_list:
            curr_enemy_moves = [i.get_numeric_coord() for i in enemy_piece.get_actions()]
            curr_enemy_moves.append(enemy_piece.get_numeric_coord())
            enemy_moves.extend(curr_enemy_moves)
        return enemy_moves

    def grid_with_enemy(grid, enemy_pieces_list):
        for position in enemy_pieces_list:
            grid[position[0]][position[1]] = -1
        return grid

    enemy_moves = enemy_positions(enemy_pieces_list)
    grid = grid_with_enemy(grid, enemy_moves)
    start_state = State(grid, own_piece, goals, cols, rows, [own_piece.get_coord()], 0)
    visited = [[False for i in range(cols)] for j in range(rows)]
    visited[start_state.own_piece.get_y()][start_state.own_piece.get_x()] = True
    queue = [start_state]
    while queue:
        curr_state = queue.pop(0)
        if curr_state.is_goal():
            print(curr_state.get_action_cost())
            return curr_state.get_path()

        trans = curr_state.get_transition()
        for state in trans:
            piece_x = state.own_piece.get_x()
            piece_y = state.own_piece.get_y()
            if not visited[piece_y][piece_x]:
                visited[piece_y][piece_x] = True
                queue.append(state)
    return []


#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline()))  # Integer
    cols = int(get_par(handle.readline()))  # Integer
    grid = [[1 for j in range(cols)] for i in range(rows)]  # Dictionary, label empty spaces as 1 (Default Step Cost)
    enemy_pieces = []  # List
    own_pieces = []  # List
    goals = []  # List

    handle.readline()  # Ignore number of obstacles
    for ch_coord in get_par(handle.readline()).split():  # Init obstacles
        r, c = from_chess_coord(ch_coord)
        grid[r][c] = -1  # Label Obstacle as -1

    handle.readline()  # Ignore Step Cost header
    line = handle.readline()
    while line.startswith("["):
        line = line[1:-2].split(",")
        r, c = from_chess_coord(line[0])
        grid[r][c] = int(line[1]) if grid[r][c] == 1 else grid[r][
            c]  # Reinitialize step cost for coordinates with different costs
        line = handle.readline()

    line = handle.readline()  # Read Enemy Position
    while line.startswith("["):
        line = line[1:-2]
        piece = add_piece(line)
        enemy_pieces.append(piece)
        line = handle.readline()

    # Read Own King Position
    line = handle.readline()[1:-2]
    piece = add_piece(line)
    own_pieces.append(piece)

    # Read Goal Positions
    for ch_coord in get_par(handle.readline()).split():
        r, c = from_chess_coord(ch_coord)
        goals.append((r, c))

    return rows, cols, grid, enemy_pieces, own_pieces, goals


def add_piece(comma_seperated) -> Piece:
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [piece, (r, c)]


def from_chess_coord(ch_coord):
    return int(ch_coord[1:]), ord(ch_coord[0]) - 97


#############################################################################
######## Main function to be called
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# To return: List of moves
# Return Format Example: [[('a', 0), ('a', 1)], [('a', 1), ('c', 3)], [('c', 3), ('d', 5)]]
def run_BFS():
    testcase = sys.argv[1]
    rows, cols, grid, enemy_pieces, own_piece, goals = parse(testcase)
    moves = search(cols, rows, grid, enemy_pieces, own_piece, goals)
    return moves


# print([king.get_coord() for king in King(5,5,10,10).get_actions()])

# print([rook.get_coord() for rook in Rook(3, 4, 10, 10, grid).get_actions()])

# print([bishop.get_coord() for bishop in Bishop(3, 3, 10, 10).get_actions()])
# print([queen.get_coord() for queen in Queen(3, 3, 10, 10).get_actions()])
# print([knight.get_coord() for knight in Knight(3, 4, 10, 10).get_actions()])
# print([ferz.get_coord() for ferz in Ferz(4, 3, 10, 10).get_actions()])
# print([princess.get_coord() for princess in Princess(4, 3, 10, 10).get_actions()])
# print([empress.get_coord() for empress in Empress(4, 3, 10, 10).get_actions()])
print(run_BFS())
