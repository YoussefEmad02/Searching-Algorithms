from Game_Settings import *

class Node:
    def __init__(self, position = None, parent = None):
        self.position = position
        self.parent = parent
        self.G = 0        # distance traveled cost
        self.H = 0        # Distance from end point cost (Hurestic function)
        self.F = 0        # H + G

class AStar():
    def __init__(self, app, start_node_x, start_node_y, end_node_x, end_node_y, wall_pos,list_of_node_types_position, list_of_weighted_nodes):
        self.app = app
        self.start_node_x = start_node_x
        self.start_node_y = start_node_y
        self.end_node_x = end_node_x
        self.end_node_y = end_node_y
        self.open_list = []
        self.closed_list = []
        self.wall_pos = wall_pos
        self.route = []
        self.route_found = False
        self.list_of_node_types_position = list_of_node_types_position
        self.list_of_weighted_nodes = list_of_weighted_nodes

    def draw_all_paths(self, current):
        i, j = current

        ##### Draw each node the computer is visiting as it is searching SIMULTNEOUSLY
        pygame.draw.rect(self.app.screen, TAN, (i * 24 + 240, j * 24, 24, 24), 0)

        ##### Redraw start/end nodes on top of all routes
        pygame.draw.rect(self.app.screen, WHITE, (240 + self.start_node_x * 24, self.start_node_y * 24, 24, 24), 0)
        pygame.draw.rect(self.app.screen, BLACK, (240 + self.end_node_x * 24, self.end_node_y * 24, 24, 24), 0)

        # Redraw grid (for aesthetic purposes lol)
        for x in range(52):
            pygame.draw.line(self.app.screen, BLACK, (GS_X + x * 24, GS_Y), (GS_X + x * 24, GE_Y))
        for y in range(30):
            pygame.draw.line(self.app.screen, BLACK, (GS_X, GS_Y + y * 24), (GE_X, GS_Y + y * 24))

        pygame.display.update()

    def generate_children(self, parent, end_node):
        print('generating children')
        parent_pos = parent.position
        for m in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            child_pos = (parent_pos[0] + m[0], parent_pos[1] + m[1])
            if self.check_valid(child_pos):
                child = Node(child_pos, parent)
                self.G_calc(child, parent, m)
                self.H_calc(child, end_node)
                self.F_calc(child)

                # If node not already added to the open list AND node isn't cutting corners around wall, then append
                if self.append_to_open(child) and self.check_wall_corner(m, parent_pos):
                    self.open_list.append(child)

            elif self.check_valid(child_pos):
                child = Node(child_pos, parent)
                self.G_calc(child, parent, m)
                self.H_calc(child, end_node)
                self.F_calc(child)

                # If node not already added to the open list AND node isn't cutting corners around wall, then append
                if self.append_to_open(child) and self.check_wall_corner(m, parent_pos):
                    self.open_list.append(child)

    def append_to_open(self, child):
        for open_node in self.open_list:

            # If node is already in open list and the new node has a higher F-score than node about to be replaced,
            # return False
            # IMPORTANT NOTE: Even if another node with same position with different F value gets added, the node with
            # higher F-score will never be checked, so it's fine to have two nodes with same position.
            if child.position == open_node.position and child.F >= open_node.F:
                return False
        return True

    def check_wall_corner(self, move, parent_pos):
        if move == (-1, 1) or move == (1, 1) or move == (1, -1) or move == (-1, -1):
            i,j = parent_pos
            (m,n) = move
            # (x, y) = Orthogonal
            if move == (1,1):
                (x,y) = (0,1)
                (a,b) = (1,0)
            elif move == (1,-1):
                (x,y) = (1,0)
                (a, b) = (0,-1)
            elif move == (-1,-1):
                (x,y) = (0,-1)
                (a, b) = (-1,0)
            else:
                (x,y) = (-1,0)
                (a, b) = (0,1)

            # If cutting corner case, return False
            if (i+x, j+y) in self.wall_pos or (i+a, i+b) in self. wall_pos and (i+m, j+n) not in self.wall_pos:
                return False
            return True
        else:
            return True

    def G_calc(self, child, parent, m):

            if m == (-1, 0):
                child.G = parent.G + int(self.list_of_weighted_nodes[0].LeftWeight)
            elif m == (1, 0):
                child.G = parent.G + int(self.list_of_weighted_nodes[0].RightWeight)
            elif m == (0, 1):
                child.G = parent.G + int(self.list_of_weighted_nodes[0].UpWeight)
            elif m == (0, -1):
                child.G = parent.G + int(self.list_of_weighted_nodes[0].DownWeight)
            elif m == (-1, 1):
                child.G = parent.G + int(self.list_of_weighted_nodes[0].LowerRightWeight)
            elif m == (1, 1):
                child.G = parent.G + int(self.list_of_weighted_nodes[0].UpperRightWeight)
            elif m == (1, -1):
                child.G = parent.G + int(self.list_of_weighted_nodes[0].UpperLeftWeight)
            elif m == (-1, -1):
                child.G = parent.G + int(self.list_of_weighted_nodes[0].LowerLeftWeight)


    def H_calc(self, child, m):
        #child.H = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)

            if m == (-1, 0):
                child.H =  int(self.list_of_weighted_nodes[1].LeftWeight)
            elif m == (1, 0):
                child.H =  int(self.list_of_weighted_nodes[1].RightWeight)
            elif m == (0, 1):
                child.H = int(self.list_of_weighted_nodes[1].UpWeight)
            elif m == (0, -1):
                child.H =  int(self.list_of_weighted_nodes[1].DownWeight)
            elif m == (-1, 1):
                child.H =  int(self.list_of_weighted_nodes[1].LowerRightWeight)
            elif m == (1, 1):
                child.H =  int(self.list_of_weighted_nodes[1].UpperRightWeight)
            elif m == (1, -1):
                child.H =  int(self.list_of_weighted_nodes[1].UpperLeftWeight)
            elif m == (-1, -1):
                child.H =  int(self.list_of_weighted_nodes[1].LowerLeftWeight)

    def F_calc(self, child):
        child.F = child.G + child.H

    def check_valid(self, move):
        if move not in self.wall_pos and move not in self.closed_list:
            return True
        return False


    def findEnd(self, current):
        if current == (self.end_node_x, self.end_node_y):
            return True
        return False

    def astar_execute(self):
        # Initialize Start & End Nodes
        start_node = Node((self.start_node_x, self.start_node_y), None)
        start_node.G = start_node.H = start_node.F = 0
        end_node = Node((self.end_node_x, self.end_node_y), None)
        end_node.G = end_node.H = end_node.F = 0

        self.open_list.append(start_node)

        print(start_node.position)
        print(end_node.position)

        while len(self.open_list) > 0:
            current_node = self.open_list[0]
            current_index = 0

            # Get the node with lowest F-Cost
            for index, node in enumerate(self.open_list):
                if node.F < current_node.F:
                    current_node = node
                    current_index = index

            # Check if route has been found
            if self.findEnd(current_node.position):
                current = current_node
                # Append path until the current node becomes none (start node has a parent of None)
                while current is not None:
                    self.route.append(current.position)
                    current = current.parent
                self.route.pop(0)
                self.route_found = True
                break

            self.generate_children(current_node, end_node)
            self.draw_all_paths(current_node.position)

            self.open_list.pop(current_index)
            self.closed_list.append(current_node.position)