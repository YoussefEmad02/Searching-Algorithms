from Game_Settings import *

class Node(object):
    def __init__(self, position=None, parent=None):
        self.position = position
        self.parent = parent
        # G is the distance traveled from the start node
        self.G = 0

class Uniform:
    def __init__(self, app, start_node_x, start_node_y, end_node_x, end_node_y, wall_pos, list_of_node_types_position, list_of_weighted_nodes):
        self.app = app
        self.start_node_x = start_node_x
        self.start_node_y = start_node_y
        self.end_node_x = end_node_x
        self.end_node_y = end_node_y
        self.wall_pos = wall_pos
        self.route = []
        self.route_found = False
        self.open_list = []
        self.closed_list = []
        self.list_of_node_types_position = list_of_node_types_position
        self.list_of_weighted_nodes = list_of_weighted_nodes

    def draw_all_paths(self, current_pos):
        i, j = current_pos
        ##### Draw each node the computer is visiting as it is searching SIMULTNEOUSLY
        pygame.draw.rect(self.app.screen, TAN, (i * 24 + 240, j * 24, 24, 24), 0)

        ##### Redraw start/end nodes on top of all routes
        pygame.draw.rect(self.app.screen, WHITE, (240 + self.start_node_x * 24, self.start_node_y * 24, 24, 24), 0)
        pygame.draw.rect(self.app.screen, BLACK, (240 + self.end_node_x * 24, self.end_node_y * 24, 24, 24), 0)


        for x in range(52):
            pygame.draw.line(self.app.screen, BLACK, (GS_X + x * 24, GS_Y), (GS_X + x * 24, GE_Y))
        for y in range(30):
            pygame.draw.line(self.app.screen, BLACK, (GS_X, GS_Y + y * 24), (GE_X, GS_Y + y * 24))

        pygame.display.update()

    def generate_children(self, parent):
        parent_pos = parent.position
        for m in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            child_pos = (parent_pos[0] + m[0], parent_pos[1] + m[1])

            if self.check_valid(child_pos) and self.check_type(child_pos) == 0:
                child = Node(child_pos, parent)
                self.G_calc(child, parent, m, 0)

                if self.check_append(child) and self.check_wall_corner(parent, m):
                    self.open_list.append(child)


            elif self.check_valid(child_pos) and self.check_type(child_pos) == 1:
                child = Node(child_pos, parent)
                self.G_calc(child, parent, m, 1)

                if self.check_append(child) and self.check_wall_corner(parent, m):
                    self.open_list.append(child)

            elif self.check_valid(child_pos) and self.check_type(child_pos) == 2:
                child = Node(child_pos, parent)
                self.G_calc(child, parent, m, 2)

                if self.check_append(child) and self.check_wall_corner(parent, m):
                    self.open_list.append(child)

            elif self.check_valid(child_pos) and self.check_type(child_pos) == 3:
                child = Node(child_pos, parent)
                self.G_calc(child, parent, m, 3)

                if self.check_append(child) and self.check_wall_corner(parent, m):
                    self.open_list.append(child)

            elif self.check_valid(child_pos) and self.check_type(child_pos) == 4:
                child = Node(child_pos, parent)
                self.G_calc(child, parent, m, 4)

                if self.check_append(child) and self.check_wall_corner(parent, m):
                    self.open_list.append(child)

            elif self.check_valid(child_pos) and self.check_type(child_pos) == 5:
                child = Node(child_pos, parent)
                self.G_calc(child, parent, m, 5)

                if self.check_append(child) and self.check_wall_corner(parent, m):
                    self.open_list.append(child)

            elif self.check_valid(child_pos) and self.check_type(child_pos) == 6:
                child = Node(child_pos, parent)
                self.G_calc(child, parent, m, 6)

                if self.check_append(child) and self.check_wall_corner(parent, m):
                    self.open_list.append(child)

    def check_wall_corner(self, parent, move):
        i, j = parent.position
        if move == (-1, 1):
            x,y = 0,1
            a,b = -1,0
        elif move == (1, 1):
            x,y = 0,1
            a,b = 1,0
        elif move == (1, -1):
            x,y = 1,0
            a,b = 0,-1
        else:
            x,y = 0,-1
            a,b = -1,0

        if (i+x, j+y) not in self.wall_pos or (i+a, j+b) not in self.wall_pos and move not in self.wall_pos:
            return True
        return False

    def G_calc(self, child, parent, m, type):

        if type == 6:

            child.G = parent.G + 1                                                   ## case that we pass through default unweighted nodes the default shall be 1

        elif 0 <= type < 6:
            if m == (-1,0):
                child.G = parent.G + int(self.list_of_weighted_nodes[type].LeftWeight)
            elif m == (1, 0):
                child.G = parent.G + int(self.list_of_weighted_nodes[type].RightWeight)
            elif m == (0, 1):
                child.G = parent.G + int(self.list_of_weighted_nodes[type].UpWeight)
            elif m == (0, -1):
                child.G = parent.G + int(self.list_of_weighted_nodes[type].DownWeight)
            elif m == (-1, 1):
                child.G = parent.G + int(self.list_of_weighted_nodes[type].LowerRightWeight)
            elif m == (1, 1):
                child.G = parent.G + int(self.list_of_weighted_nodes[type].UpperRightWeight)
            elif m == (1, -1):
                child.G = parent.G + int(self.list_of_weighted_nodes[type].UpperLeftWeight)
            elif m == (-1, -1):
                child.G = parent.G + int(self.list_of_weighted_nodes[type].LowerLeftWeight)



    def check_append(self, child):
        for open_node in self.open_list:
            if child.position == open_node.position and child.G >= open_node.G:
                return False
        return True

    def check_valid(self, position):
        if position not in self.wall_pos and position not in self.closed_list:
            return True
        return False

    def check_type(self, position):

        if position in self.list_of_node_types_position[0]:
            return 0
        elif position in self.list_of_node_types_position[1]:
            return 1
        elif position in self.list_of_node_types_position[2]:
            return 2
        elif position in self.list_of_node_types_position[3]:
            return 3
        elif position in self.list_of_node_types_position[4]:
            return 4
        elif position in self.list_of_node_types_position[5]:
            return 5
        elif position not in self.list_of_node_types_position[5] and position not in self.list_of_node_types_position[4] and position not in self.list_of_node_types_position[3] and position not in self.list_of_node_types_position[2] and position not in self.list_of_node_types_position[1] and position not in self.list_of_node_types_position[0]:
            return 6

    def findEnd(self, position):
        if position == (self.end_node_x, self.end_node_y):
            return True
        return False

    def dijkstra_execute(self):
        start_node = Node((self.start_node_x, self.start_node_y), None)
        start_node.G = 0
        end_node = Node((self.end_node_x, self.end_node_y), None)

        self.open_list.append(start_node)


        print(self.list_of_weighted_nodes[0].LeftWeight)
        print(self.list_of_weighted_nodes[0].LowerRightWeight)
        print(self.list_of_weighted_nodes[0].UpperLeftWeight)
        for n in range(6):
            print(self.list_of_node_types_position[n])


        while len(self.open_list) > 0:
            # Search for the node with the lowest distance G traveled from the start node
            current_node = self.open_list[0]
            current_index = 0
            for index, node in enumerate(self.open_list):
                if node.G < current_node.G:
                    current_node = node
                    current_index = index

            # Check if the algorithm has reached the end node
            if self.findEnd(current_node.position):
                current = current_node
                while current is not None:
                    self.route.append(current.position)
                    current = current.parent
                self.route.pop(0)
                self.route_found = True
                break

            self.draw_all_paths(current_node.position)
            self.generate_children(current_node)

            self.open_list.pop(current_index)
            self.closed_list.append(current_node.position)