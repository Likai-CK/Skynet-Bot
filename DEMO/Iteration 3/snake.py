import curses
from random import randint

class SnakeGame:
    def __init__(self, board_width = 20, board_height = 20, gui = False):
        self.score = 0
        self.done = False
        self.board = {'width': board_width, 'height': board_height}
        self.gui = gui
        self.obstacles = []
        
    def start(self):
        self.snake_init()
        self.generate_food()
        self.generate_obstacles()
        if self.gui: self.render_init()
        return self.generate_observations()
        
    def generate_obstacles(self):
        self.obstacles.append([2,3])
        self.obstacles.append([4,3])
        self.obstacles.append([14,6])
        self.obstacles.append([15,3])
        self.obstacles.append([10,15])
        
        self.obstacles.append([11,16])
        self.obstacles.append([9,4])
        self.obstacles.append([18,7])
        self.obstacles.append([7,3])
        
    def snake_init(self):
        x = randint(5, self.board["width"] - 5)
        y = randint(5, self.board["height"] - 5)
        self.snake = []
        vertical = randint(0,1) == 0
        for i in range(3):
            point = [x + i, y] if vertical else [x, y + i]
            self.snake.insert(0, point)

    def generate_food(self):
        food = []
        while food == []:
            food = [randint(1, self.board["width"]), randint(1, self.board["height"])]
            if food in self.snake: food = []
            if food in self.obstacles: food = []
        self.food = food

    def render_init(self):
        curses.initscr()
        win = curses.newwin(self.board["width"] + 2, self.board["height"] + 2, 0, 0)
        curses.curs_set(0)
        win.nodelay(1)
        win.timeout(200)
        self.win = win
        self.render()

    def render(self):
        self.win.clear()
        self.win.border(0)
        self.win.addstr(0, 2, 'Score : ' + str(self.score) + ' ')
        for i in self.obstacles:
            self.win.addch(i[0], i[1], '#')
                
        self.win.addch(self.food[0], self.food[1], 'o')
        for i, point in enumerate(self.snake):
            if i == 0:
                self.win.addch(point[0], point[1], 'X')
            else:
                self.win.addch(point[0], point[1], 'x')
        self.win.getch()

    def step(self, key):
        # 0 - UP
        # 1 - RIGHT
        # 2 - DOWN
        # 3 - LEFT
        if self.done == True: self.end_game()
        self.create_new_point(key)
        if self.food_eaten():
            self.score += 1
            self.generate_food()
        else:
            self.remove_last_point()
        self.check_collisions()
        if self.gui: self.render()
        return self.generate_observations()

    def create_new_point(self, key):
        new_point = [self.snake[0][0], self.snake[0][1]]
        if key == 0:
            new_point[0] -= 1
        elif key == 1:
            new_point[1] += 1
        elif key == 2:
            new_point[0] += 1
        elif key == 3:
            new_point[1] -= 1
        self.snake.insert(0, new_point)

    def remove_last_point(self):
        self.snake.pop()

    def food_eaten(self):
        return self.snake[0] == self.food

    def check_collisions(self):
        if (self.snake[0][0] == 0 or
            self.snake[0][0] == self.board["width"] + 1 or
            self.snake[0][1] == 0 or
            self.snake[0][1] == self.board["height"] + 1 or
            self.snake[0] in self.snake[1:-1] or
            self.snake[0] in self.obstacles):
            self.done = True

    def generate_observations(self):
        return self.done, self.score, self.snake, self.food, self.obstacles

    def generate_observations_as_list(self):
        return [self.done, self.score, self.snake, self.food, self.obstacles]
    
    def render_destroy(self):
        curses.endwin()

    def end_game(self):
        if self.gui:
            render_destroy()
            exit()

if __name__ == "__main__":
    game = SnakeGame(gui = True)
    game.start()
    for _ in range(20):
        game.step(randint(0,3))
