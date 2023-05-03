import sys
from Game_Settings import *
from GUI_Buttons import *
from Breadth_First_Search_Algorithm import *
from Depth_First_Search_Algorithm import *
from A_Star_Algorithm import *
from Uniform_Cost_Algorithm import *
from Path_Visualizer import *
from Greedy_Algorithm import*
from Iterative_Deepening_Algorithm import *

pygame.init()

class number_object(object):
    def __init__(self, number):
        self.number = number




#object_list = [object_0, object_1, object_2]

#for obj in object_list:
 #    print(obj.number)

#print(object_list[0].number)


class Nodes(object):


    def __init__(self, LeftWeight, RightWeight, UpWeight, DownWeight, UpperLeftWeight , LowerLeftWeight,UpperRightWeight, LowerRightWeight ):
        self.LeftWeight = LeftWeight
        self.RightWeight = RightWeight
        self.UpWeight = UpWeight
        self.DownWeight = DownWeight
        self.UpperLeftWeight = UpperLeftWeight
        self.LowerLeftWeight = LowerLeftWeight
        self.UpperRightWeight = UpperRightWeight
        self.LowerRightWeight = LowerRightWeight







class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((1720, 1080))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'main menu'
        self.algorithm_state = ''
        self.grid_square_length = 24 # The dimensions of each grid square is 24 x 24
        self.load()
        self.start_checker = 0
        self.end_checker = 0
        self.mouse_drag = 0





        self.weighted_nodes_checker = 0
        self.added_weight_nodes_counter = 0
        self.list_of_weighted_nodes = []

        self.list_of_weighted_nodes.append(Nodes(0, 0, 0, 0 , 0 , 0, 0, 0))
        self.list_of_weighted_nodes.append(Nodes(0, 0, 0, 0 , 0 , 0, 0, 0))
        self.list_of_weighted_nodes.append(Nodes(0, 0, 0, 0 , 0 , 0, 0, 0))
        self.list_of_weighted_nodes.append(Nodes(0, 0, 0, 0 , 0 , 0, 0, 0))
        self.list_of_weighted_nodes.append(Nodes(0, 0, 0, 0 , 0 , 0, 0, 0))
        self.list_of_weighted_nodes.append(Nodes(0, 0, 0, 0 , 0 , 0, 0, 0))
        self.list_of_weighted_nodes.append(Nodes(0, 0, 0, 0 , 0 , 0, 0, 0))

        #self.weigted_nodes_pos_list = []     # A



        # Creates a list containing 6 lists, each of 1000 items, all set to (-1,-1)
        w, h = 1000, 6
        self.weigted_nodes_pos_list = [[(-1,-1) for x in range(w)] for y in range(h)]

        #self.weigted_nodes_pos_list = wall_nodes_coords_list.copy()

        #self.weigted_nodes_pos_list.append(wall_nodes_coords_list.copy())
        #self.weigted_nodes_pos_list.append(wall_nodes_coords_list.copy())
        #self.weigted_nodes_pos_list.append(wall_nodes_coords_list.copy())
        #self.weigted_nodes_pos_list.append(wall_nodes_coords_list.copy())
        #self.weigted_nodes_pos_list.append(wall_nodes_coords_list.copy())
        #self.weigted_nodes_pos_list.append(wall_nodes_coords_list.copy())

        #self.weigted_nodes_pos_list[0]




        #self.weigted_nodes_pos_list.append(wall_nodes_coords_list.copy(), self.list_of_nodes[self.added_weight_nodes_counter + 0])
        #self.weigted_nodes_pos_list.append(wall_nodes_coords_list.copy(), self.list_of_nodes[self.added_weight_nodes_counter + 1])
        #self.weigted_nodes_pos_list.append(wall_nodes_coords_list.copy(), self.list_of_nodes[self.added_weight_nodes_counter + 2])
        #self.weigted_nodes_pos_list.append(wall_nodes_coords_list.copy(), self.list_of_nodes[self.added_weight_nodes_counter + 3])
        #self.weigted_nodes_pos_list.append(wall_nodes_coords_list.copy(), self.list_of_nodes[self.added_weight_nodes_counter + 4])






        # Start and End Nodes Coordinates
        self.start_node_x = None
        self.start_node_y = None
        self.end_node_x = None
        self.end_node_y = None

        # Wall Nodes List (list already includes the coordinates of the borders)
        self.wall_pos = wall_nodes_coords_list.copy()



        # Define Main-Menu buttons
        self.bfs_button = Buttons(self, TURQUOISE, 200, 550, 400, MAIN_BUTTON_HEIGHT, 'Breadth-First Search')
        self.dfs_button = Buttons(self, TURQUOISE, 650, 550, 400, MAIN_BUTTON_HEIGHT, 'Depth-First Search')
        self.astar_button = Buttons(self, TURQUOISE, 1100, 550, 400, MAIN_BUTTON_HEIGHT, 'A-Star Search')
        self.uniform_cost_button = Buttons(self, TURQUOISE, 200, 650, 400, MAIN_BUTTON_HEIGHT, 'Uniform Cost Search')
        self.Greedy_button = Buttons(self, TURQUOISE, 650, 650, 400, MAIN_BUTTON_HEIGHT, 'Greedy Search')
        self.IterativeDepeening_button = Buttons(self, TURQUOISE, 1100, 650, 400, MAIN_BUTTON_HEIGHT, 'Iterative_D Search')


        # Define Grid-Menu buttons
        self.start_position_button = Buttons(self, TURQUOISE, 315,800 ,300, GRID_BUTTON_HEIGHT, 'Start Position')
        self.weighted_node_button = Buttons(self, TURQUOISE, 740, 800, 300, GRID_BUTTON_HEIGHT, 'Weighted Nodes')
        self.add_weight_and_direction_button = Buttons(self, TURQUOISE, 1160, 800, 300, GRID_BUTTON_HEIGHT, 'Weight & Direct')
        self.start_button = Buttons(self, TURQUOISE,  315 ,900, 300, GRID_BUTTON_HEIGHT, 'Solve Maze')
        self.main_menu_button = Buttons(self, TURQUOISE , 740, 900, 300, GRID_BUTTON_HEIGHT, 'Main Menu')
        self.End_position_button = Buttons(self, TURQUOISE , 1160, 900, 300, GRID_BUTTON_HEIGHT, 'End Position')
    def run(self):
        while self.running:
            if self.state == 'main menu':
                self.main_menu_events()
            if self.state == 'grid window':
                self.grid_events()
            if self.state == 'draw S' or self.state == 'draw walls':
                self.draw_nodes()
            if self.state == 'draw E' or self.state == 'draw walls':
                self.draw_nodes()
            if self.state == 'Weight Nodes':
                self.draw_nodes()
            if self.state == 'taking input':
                self.receive_input()
            if self.state == 'start visualizing':
                self.execute_search_algorithm()
            if self.state == 'aftermath':
                self.reset_or_main_menu()

        pygame.quit()
        sys.exit()

#################################### SETUP FUNCTIONS #########################################

##### Loading Images



    def load(self):
        self.main_menu_background = pygame.image.load('main_background.png')
        self.grid_background = pygame.image.load('Maze_Logo.png')

##### Draw Text
    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

##### Setup for Main Menu
    def sketch_main_menu(self):
        self.screen.blit(self.main_menu_background, (0, 0))

        # Draw Buttons
        self.bfs_button.draw_button(TURQUOISE)
        self.dfs_button.draw_button(TURQUOISE)
        self.astar_button.draw_button(TURQUOISE)
        self.uniform_cost_button.draw_button(TURQUOISE)
        self.Greedy_button.draw_button(TURQUOISE)
        self.IterativeDepeening_button.draw_button(TURQUOISE)


##### Setup for Grid
    def sketch_hotbar(self):
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, BLACK, (0, 0, 240, 768), 0)
        self.screen.blit(self.grid_background, (25, 768))
        self.screen.blit(self.grid_background, (1480, 768))

    def sketch_grid(self):
        # Add borders for a cleaner look
        pygame.draw.rect(self.screen, ROYALBLUE, (0, 0, 1720, HEIGHT), 0)
        pygame.draw.rect(self.screen, SPRINGGREEN, (264, 24, GRID_WIDTH, GRID_HEIGHT), 0)

        # Draw grid
        # There are 52 square pixels across on grid [ WITHOUT BORDERS! ]
        # There are 30 square pixels vertically on grid [ WITHOUT BORDERS! ]
        for x in range(52):
            pygame.draw.line(self.screen, BLACK, (GS_X + x * self.grid_square_length, GS_Y),
                             (GS_X + x * self.grid_square_length, GE_Y))
        for y in range(30):
            pygame.draw.line(self.screen, BLACK, (GS_X, GS_Y + y * self.grid_square_length),
                             (GE_X, GS_Y + y * self.grid_square_length))

    def sketch_grid_buttons(self):
        # Draw buttons
        self.start_position_button.draw_button(TURQUOISE)
        self.weighted_node_button.draw_button(TURQUOISE)
        self.add_weight_and_direction_button.draw_button(TURQUOISE)
        self.start_button.draw_button(TURQUOISE)
        self.main_menu_button.draw_button(TURQUOISE)
        self.End_position_button.draw_button(TURQUOISE)


    # Checks for state when button is clicked and changes button colour when hovered over.
    def grid_window_buttons(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_position_button.isOver(pos):
                self.state = 'draw S'
            elif self.End_position_button.isOver(pos):
                 self.state = 'draw E'
            elif self.weighted_node_button.isOver(pos):
                self.weighted_nodes_checker += 1
                self.added_weight_nodes_counter += 1
                self.state = 'Weight Nodes'

                #for m in self.weigted_nodes_and_pos_list:
                  #  for n in m[0]:

                #print (self.weigted_nodes_pos_list[0])




            elif self.add_weight_and_direction_button.isOver(pos):
                self.state = 'taking input'
            elif self.start_button.isOver(pos):
                self.state = 'start visualizing'
            elif self.main_menu_button.isOver(pos):
                self.back_to_menu()


        # Get mouse position and check if it is hovering over button
        if event.type == pygame.MOUSEMOTION:
            if self.start_position_button.isOver(pos):
                self.start_position_button.colour = TURQUOISE
            elif self.weighted_node_button.isOver(pos):
                self.weighted_node_button.colour = TURQUOISE
            elif self.add_weight_and_direction_button.isOver(pos):
                self.add_weight_and_direction_button.colour = TURQUOISE
            elif self.start_button.isOver(pos):
                self.start_button.colour = TURQUOISE
            elif self.main_menu_button.isOver(pos):
                self.main_menu_button.colour = TURQUOISE
            elif self.End_position_button.isOver(pos):
                self.End_position_button.colour = TURQUOISE
            else:
                self.start_position_button.colour, self.weighted_node_button.colour, self.add_weight_and_direction_button.colour, \
                self.start_button.colour, self.main_menu_button.colour, self.End_position_button.colour = \
                    STEELBLUE, STEELBLUE, STEELBLUE, STEELBLUE, STEELBLUE, STEELBLUE

    def grid_button_keep_colour(self):
        if self.state == 'draw S':
            self.start_position_button.colour = STEELBLUE
        elif self.state == 'draw E':
            self.End_position_button.colour = STEELBLUE
        elif self.state == 'draw walls':
            self.weighted_node_button.colour = STEELBLUE
        elif self.state == 'taking input':
            self.add_weight_and_direction_button.colour = STEELBLUE



    def execute_reset(self):
        self.start_checker = 0
        self.end_checker = 0

        # Start and End Nodes Coordinates
        self.start_node_x = None
        self.start_node_y = None
        self.end_node_x = None
        self.end_node_y = None


        # Wall Nodes List (list already includes the coordinates of the borders)
        self.wall_pos = wall_nodes_coords_list.copy()

        # Switch States
        self.state = 'grid window'

    def back_to_menu(self):
        self.start_checker = 0
        self.end_checker = 0

        # Start and End Nodes Coordinates
        self.start_node_x = None
        self.start_node_y = None
        self.end_node_x = None
        self.end_node_y = None

        # Wall Nodes List (list already includes the coordinates of the borders)
        self.wall_pos = wall_nodes_coords_list.copy()

        # Switch States
        self.state = 'main menu'


#################################### EXECUTION FUNCTIONS #########################################

##### MAIN MENU FUNCTIONS

    def main_menu_events(self):
        # Draw Background
        pygame.display.update()
        self.sketch_main_menu()


        # Check if game is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            pos = pygame.mouse.get_pos()
            # Get mouse position and check if it is clicking button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.bfs_button.isOver(pos):
                    self.algorithm_state = 'bfs'
                    self.state = 'grid window'
                if self.dfs_button.isOver(pos):
                    self.algorithm_state = 'dfs'
                    self.state = 'grid window'
                if self.astar_button.isOver(pos):
                    self.algorithm_state = 'astar'
                    self.state = 'grid window'
                if self.uniform_cost_button.isOver(pos):
                    self.algorithm_state = 'Uniform Cost'
                    self.state = 'grid window'
                if self.Greedy_button.isOver(pos):
                    self.algorithm_state = 'greedy'
                    self.state = 'grid window'
                if self.IterativeDepeening_button.isOver(pos):
                    self.algorithm_state = 'iterative_D'
                    self.state = 'grid window'


            # Get mouse position and check if it is hovering over button
            if event.type == pygame.MOUSEMOTION:
                if self.bfs_button.isOver(pos):
                    self.bfs_button.colour = TURQUOISE
                elif self.dfs_button.isOver(pos):
                    self.dfs_button.colour = TURQUOISE
                elif self.astar_button.isOver(pos):
                    self.astar_button.colour = TURQUOISE
                elif self.uniform_cost_button.isOver(pos):
                    self.uniform_cost_button.colour = TURQUOISE
                elif self.Greedy_button.isOver(pos):
                    self.Greedy_button.colour = TURQUOISE
                elif self.IterativeDepeening_button.isOver(pos):
                    self.IterativeDepeening_button.colour = TURQUOISE

                else:
                    self.bfs_button.colour, self.dfs_button.colour, self.astar_button.colour, self.uniform_cost_button.colour, \
                     self.Greedy_button.colour, self.IterativeDepeening_button.colour = WHITE, WHITE, WHITE, WHITE, WHITE, WHITE

##### PLAYING STATE FUNCTIONS #####

    def grid_events(self):
        #print(len(wall_nodes_coords_list))
        self.sketch_hotbar()
        self.sketch_grid()
        self.sketch_grid_buttons()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            pos = pygame.mouse.get_pos()

            # Grid button function from Helper Functions
            self.grid_window_buttons(pos, event)

##### DRAWING STATE FUNCTIONS #####
    # Check where the mouse is clicking on grid
    # Add in feature to Draw nodes on grid
    # Add in feature so that the drawn nodes on grid translate onto text file
    def draw_nodes(self):
        # Function made in Helper Functions to check which button is pressed and to make it keep colour
        self.grid_button_keep_colour()
        self.sketch_grid_buttons()
        pygame.display.update()
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Grid button function from Helper Functions
            self.grid_window_buttons(pos, event)

            # Set boundaries for where mouse position is valid
            if pos[0] > 264 and pos[0] < 1512 and pos[1] > 24 and pos[1] < 744:
                x_grid_pos = (pos[0] - 264) // 24
                y_grid_pos = (pos[1] - 24) // 24

                # Get mouse position and check if it is clicking button. Then, draw if clicking. CHECK DRAG STATE
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_drag = 1

                    # The chunk of code for start/end pos is placed here, because I do not want the drag feature to be available for start/end nodes
                    if self.state == 'draw S' and self.start_checker < 2:
                        # Choose point colour for grid and record the coordinate of start pos
                        if self.start_checker == 0 and (x_grid_pos+1, y_grid_pos+1) not in self.wall_pos:
                            node_colour = WHITE
                            self.start_node_x = x_grid_pos + 1
                            self.start_node_y = y_grid_pos + 1
                            # print(self.start_node_x, self.start_node_y)
                            self.start_checker += 1
                        else:
                            continue


                        # Choose point colour for grid and record the coordinate of end pos
                        # Also, check that the end node is not the same point as start node
                    elif self.state == 'draw E' and self.end_checker < 2 and (x_grid_pos+1, y_grid_pos+1) != (self.start_node_x, self.start_node_y) and (x_grid_pos+1, y_grid_pos+1) not in self.wall_pos:
                            node_colour = BLACK
                            self.end_node_x = x_grid_pos + 1
                            self.end_node_y = y_grid_pos + 1
                            # print(self.end_node_x, self.end_node_y)
                            self.end_checker += 1
                    else:
                        continue

                        # Draw point on Grid
                    pygame.draw.rect(self.screen, node_colour, (264 + x_grid_pos * 24, 24 + y_grid_pos * 24, 24, 24), 0)

                # Checks if mouse button is no longer held down
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_drag = 0





                    # Checks if mouse button is being held down; drag feature
                if self.mouse_drag == 1:







                        if self.state == 'Weight Nodes' and self.weighted_nodes_checker <= self.added_weight_nodes_counter:

                            if (x_grid_pos + 1, y_grid_pos + 1) not in self.wall_pos \
                                    and (x_grid_pos + 1, y_grid_pos + 1) != (self.start_node_x, self.start_node_y) \
                                    and (x_grid_pos + 1, y_grid_pos + 1) != (self.end_node_x, self.end_node_y):
                                pygame.draw.rect(self.screen, (0,0, self.weighted_nodes_checker * 50),
                                                 (264 + x_grid_pos * 24, 24 + y_grid_pos * 24, 24, 24), 0)
                                self.weigted_nodes_pos_list[self.added_weight_nodes_counter - 1].append((x_grid_pos + 1, y_grid_pos + 1))   #
                                #self.wall_pos.append((x_grid_pos + 1, y_grid_pos + 1))
                                print (" the following supposed to have some appending to it")
                                print("counter equals ")
                                print(self.added_weight_nodes_counter)
                                print(self.weigted_nodes_pos_list[self.added_weight_nodes_counter - 1])
                                print(" end of list number")
                                print(self.added_weight_nodes_counter)
                                print(" space deliniation")




                            # print(len(self.wall_pos))

                for x in range(52):
                    pygame.draw.line(self.screen, BLACK, (GS_X + x * self.grid_square_length, GS_Y),
                                        (GS_X + x * self.grid_square_length, GE_Y))
                for y in range(30):
                    pygame.draw.line(self.screen, BLACK, (GS_X, GS_Y + y * self.grid_square_length),
                                        (GE_X, GS_Y + y * self.grid_square_length))

    def receive_input(self):

        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False



        if self.state == 'taking input':



            P = True
            while P:

                clock = pygame.time.Clock()
                base_font = pygame.font.Font(None, 32)
                user_text = ''

                # create rectangle
                input_rect = pygame.Rect(50, 0, 50, 50)

                # color_active stores color(lightskyblue3) which
                # gets active when input box is clicked by user
                color_active = pygame.Color('lightskyblue3')

                # color_passive store color(chartreuse4) which is
                # color of input box.
                color_passive = pygame.Color('chartreuse4')
                color = color_passive

                user_input = ''

                active = False
                done = False
                x = True
                while x and not done:
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            done = True
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:

                                user_input = user_text[:-1]


                            elif event.mod & pygame.KMOD_LSHIFT:

                                self.list = user_input.split()







                                #for added_weight_nodes_counter in self.list_of_nodes:

                                node1 = Nodes(self.list[0], self.list[1], self.list[2], self.list[3], self.list[4], self.list[5], self.list[6], self.list[7])




                                #list_of_nodes = [node1, node2, node3]


                                self.list_of_weighted_nodes[self.added_weight_nodes_counter] = node1

                                #self.weighted_nodes_checker += 1

                                print (" checker value at ")
                                print(self.weighted_nodes_checker)
                                print(" checker value at ")



                                print(self.list_of_weighted_nodes[self.added_weight_nodes_counter].LeftWeight)
                                print(self.list_of_weighted_nodes[self.added_weight_nodes_counter].UpWeight)
                                print(self.list_of_weighted_nodes[self.added_weight_nodes_counter].RightWeight)
                                print(self.list_of_weighted_nodes[self.added_weight_nodes_counter].DownWeight)
                                print(self.list_of_weighted_nodes[self.added_weight_nodes_counter].UpperLeftWeight)
                                print(self.list_of_weighted_nodes[self.added_weight_nodes_counter].LowerLeftWeight)
                                print(self.list_of_weighted_nodes[self.added_weight_nodes_counter].UpperRightWeight)
                                print(self.list_of_weighted_nodes[self.added_weight_nodes_counter].LowerRightWeight)

                                #+ " " + self.list_of_nodes[self.added_weight_nodes_counter].RightWeight + " " + self.list_of_nodes[self.added_weight_nodes_counter].UpWeight + " " + self.list_of_nodes[self.added_weight_nodes_counter].DownWeight)





                                P = False
                                done = True
                                # x = False

                            # self.state = 'Weight Nodes'
                            # self.draw_nodes()

                            else:
                                user_input += event.unicode

                    if active:
                        color = color_active
                    else:
                        color = color_passive

                    # draw rectangle and argument passed which should
                    # be on screen
                    pygame.draw.rect(self.screen, color, input_rect)

                    text_surface = base_font.render(user_input, True, (255, 255, 255))

                    # render at position stated in arguments
                    self.screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

                    # set width of textfield so that text cannot get
                    # outside of user's text input
                    input_rect.w = max(100, text_surface.get_width() + 10)

                    # display.flip() will update only a portion of the
                    # screen to updated, not full area
                    pygame.display.flip()

                    clock.tick(60)

            print("it seems we get out of here")

        pygame.display.update()
        self.state = 'Weight Nodes'
#################################### VISUALIZATION FUNCTIONS #########################################

    def execute_search_algorithm(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        #print(self.start_node_x, self.start_node_y)
        #print(self.end_node_x, self.end_node_y)

        ### BFS ###

        if self.algorithm_state == 'bfs':
            self.bfs = BreadthFirst(self, self.start_node_x, self.start_node_y, self.end_node_x, self.end_node_y, self.wall_pos)

            if self.start_node_x or self.end_node_x is not None:
                self.bfs.bfs_execute()

            # Make Object for new path
            if self.bfs.route_found:
                self.draw_path = VisualizePath(self.screen, self.start_node_x, self.start_node_y, self.bfs.route, [])
                self.draw_path.get_path_coords()
                self.draw_path.draw_path()

            else:
                self.draw_text('NO ROUTE WAS FOUND FROM THE STARTING POINT TO THE END POINT SPECIFIED', self.screen, [768,384], 50, RED, FONT, centered = True)

        ### DFS ###

        elif self.algorithm_state == 'dfs':
            self.dfs = DepthFirst(self, self.start_node_x, self.start_node_y, self.end_node_x, self.end_node_y, self.wall_pos)

            if self.start_node_x or self.end_node_x is not None:
                self.dfs.dfs_execute()

            # Make Object for new path
            if self.dfs.route_found:
                self.draw_path = VisualizePath(self.screen, self.start_node_x, self.start_node_y, self.dfs.route, [])
                self.draw_path.get_path_coords()
                self.draw_path.draw_path()

            else:
                self.draw_text('NO ROUTE WAS FOUND FROM THE STARTING POINT TO THE END POINT SPECIFIED', self.screen, [768,384], 50, RED, FONT, centered = True)

        ### A-STAR ###

        elif self.algorithm_state == 'astar':
            self.astar = AStar(self, self.start_node_x, self.start_node_y, self.end_node_x, self.end_node_y, self.wall_pos,self.weigted_nodes_pos_list, self.list_of_weighted_nodes)

            if self.start_node_x or self.end_node_x is not None:
                self.astar.astar_execute()

            if self.astar.route_found:
                self.draw_path = VisualizePath(self.screen, self.start_node_x, self.start_node_y, None, self.astar.route)
                self.draw_path.draw_path()

            else:
                self.draw_text('NO ROUTE WAS FOUND FROM THE STARTING POINT TO THE END POINT SPECIFIED', self.screen, [768, 384], 50, RED, FONT, centered=True)

        ### DIJKSTRA ###

        elif self.algorithm_state == 'Uniform Cost':
            self.Uniform_Cost = Uniform(self, self.start_node_x, self.start_node_y, self.end_node_x, self.end_node_y, self.wall_pos, self.weigted_nodes_pos_list, self.list_of_weighted_nodes)

            if self.start_node_x or self.end_node_x is not None:
                self.Uniform_Cost.dijkstra_execute()

            if self.Uniform_Cost.route_found:
                self.draw_path = VisualizePath(self.screen, self.start_node_x, self.start_node_y, None, self.Uniform_Cost.route)
                self.draw_path.draw_path()

            else:
                self.draw_text('NO ROUTE WAS FOUND FROM THE STARTING POINT TO THE END POINT SPECIFIED', self.screen, [768, 384], 50, RED, FONT, centered=True)

        ### Greedy ###

        elif self.algorithm_state == 'greedy':
            self.greedy = Greedy(self, self.start_node_x, self.start_node_y, self.end_node_x, self.end_node_y,
                                        self.wall_pos, self.weigted_nodes_pos_list, self.list_of_weighted_nodes)

            if self.start_node_x or self.end_node_x is not None:
                self.greedy.greedy_execute()

            # Make Object for new path
            if self.greedy.route_found:
                self.draw_path = VisualizePath(self.screen, self.start_node_x, self.start_node_y, None, self.greedy.route)

                self.draw_path.draw_path()

            else:
                self.draw_text('NO ROUTE WAS FOUND FROM THE STARTING POINT TO THE END POINT SPECIFIED', self.screen, [768, 384], 50, RED, FONT, centered=True)

        ### Iterative Deepening ###

        elif self.algorithm_state == 'iterative_D':
            self.iterative_D = Iterative_D(self, self.start_node_x, self.start_node_y, self.end_node_x, self.end_node_y,
                                    self.wall_pos)

            if self.start_node_x or self.end_node_x is not None:
                self.iterative_D.iterative_D_execute()

            # Make Object for new path
            if self.iterative_D.route_found:
                self.draw_path = VisualizePath(self.screen, self.start_node_x, self.start_node_y, self.iterative_D.route, [])
                self.draw_path.get_path_coords()
                self.draw_path.draw_path()

            else:
                self.draw_text('NO ROUTE WAS FOUND FROM THE STARTING POINT TO THE END POINT SPECIFIED', self.screen, [768, 384], 50, RED, FONT, centered=True)




        pygame.display.update()
        self.state = 'aftermath'

#################################### AFTERMATH FUNCTIONS #########################################

    def reset_or_main_menu(self):
        self.sketch_grid_buttons()
        pygame.display.update()

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEMOTION:
                if self.start_position_button.isOver(pos):
                    self.start_position_button.colour = MINT
                elif self.weighted_node_button.isOver(pos):
                    self.weighted_node_button.colour = MINT
                elif self.add_weight_and_direction_button.isOver(pos):
                    self.add_weight_and_direction_button.colour = MINT
                elif self.start_button.isOver(pos):
                    self.start_button.colour = MINT
                elif self.main_menu_button.isOver(pos):
                    self.main_menu_button.colour = MINT
                else:
                    self.start_position_button.colour, self.weighted_node_button.colour, self.add_weight_and_direction_button.colour, self.start_button.colour, self.main_menu_button.colour = STEELBLUE, STEELBLUE, STEELBLUE, STEELBLUE, STEELBLUE

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.add_weight_and_direction_button.isOver(pos):
                    self.execute_reset()
                elif self.main_menu_button.isOver(pos):
                    self.back_to_menu()