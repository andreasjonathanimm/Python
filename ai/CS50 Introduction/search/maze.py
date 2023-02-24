import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class GreedyFrontier():
    def __init__(self, goal):
        self.frontier = []
        self.goal = goal

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            min = 0
            for i in range(len(self.frontier)):
                if self.distance(self.frontier[i]) < self.distance(self.frontier[min]):
                    min = i
            node = self.frontier[min]
            self.frontier = self.frontier[:min] + self.frontier[min+1:]
            return node

    def distance(self, node):
        x1, y1 = node.state
        x2, y2 = self.goal
        return abs(x1 - x2) + abs(y1 - y2)

class AStarFrontier():
    def __init__(self, goal):
        self.frontier = []
        self.goal = goal
        self.start = None

    def add(self, node):
        self.frontier.append(node)

        if self.start is None:
            self.start = node

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            min = 0
            for i in range(len(self.frontier)):
                if self.distance(self.frontier[i]) < self.distance(self.frontier[min]):
                    min = i
            node = self.frontier[min]
            self.frontier = self.frontier[:min] + self.frontier[min+1:]
            return node

    def distance(self, node):
        x1, y1 = node.state
        x2, y2 = self.goal
        return abs(x1 - x2) + abs(y1 - y2) + self.cost(node)
    
    def cost(self, node):
        cost = 0
        while node.parent is not self.start and node.parent is not None:
            cost += 1
            node = node.parent
        return cost

class Maze():
    def __init__(self, filename):
        # Read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("Maze must have exactly one start point.")
        if contents.count("B") != 1:
            raise Exception("Maze must have exactly one goal.")

        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state

        # All possible actions
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        # Ensure actions are valid
        result = []
        for action, (r, c) in candidates:
            try:
                if not self.walls[r][c]:
                    result.append((action, (r, c)))
            except IndexError:
                continue
        return result

    def solve(self, algorithm):
        """Finds a solution to maze, if one exists."""

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)

        if algorithm == "dfs":
            frontier = StackFrontier()
        elif algorithm == "bfs":
            frontier = QueueFrontier()
        elif algorithm == "greedy":
            frontier = GreedyFrontier(self.goal)
        elif algorithm == "astar":
            frontier = AStarFrontier(self.goal)
        
        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until solution found
        while True:
            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("No solution")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []

                # Follow parent nodes to find solution
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def output_image(self, filename, show_solution=True, show_explored=False):
        """Outputs an image of the maze, coloring start, goal, solution, and explored cells."""
        from PIL import Image, ImageDraw

        # Colors
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        green = (0, 255, 0)
        lightred = (255, 100, 100)
        yellow = (255, 255, 0)

        # Create a new image with a black background
        img = Image.new("RGB", (self.width * 50, self.height * 50), black)
        draw = ImageDraw.Draw(img)

        # Draw grid
        for i in range(self.width):
            for j in range(self.height):
                if self.walls[j][i]:
                    draw.rectangle(((i * 50, j * 50), ((i + 1) * 50, (j + 1) * 50)), fill=white)

        # Draw explored cells
        if show_explored:
            for cell in self.explored:
                draw.rectangle(((cell[1] * 50 + 15, cell[0] * 50 + 15), (cell[1] * 50 + 35, cell[0] * 50 + 35)), fill=lightred)

        # Draw solution path
        if show_solution and self.solution is not None:
            for cell in self.solution[1]:
                draw.rectangle(((cell[1] * 50 + 15, cell[0] * 50 + 15), (cell[1] * 50 + 35, cell[0] * 50 + 35)), fill=yellow)

        # Draw start and goal
        draw.rectangle(((self.start[1] * 50 + 15, self.start[0] * 50 + 15), (self.start[1] * 50 + 35, self.start[0] * 50 + 35)), fill=red)
        draw.rectangle(((self.goal[1] * 50 + 15, self.goal[0] * 50 + 15), (self.goal[1] * 50 + 35, self.goal[0] * 50 + 35)), fill=green)

        # Save the image at folder where the code is
        img.save(filename)

if __name__ == "__main__":
    # Ensure proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt; Make sure you are in the same folder as the code")

    # Get maze
    maze = Maze(sys.argv[1])

    # Maze preview
    maze.print()

    # Solve maze
    print("Solving maze...")
    maze.solve("astar")
    print(f"States Explored: {maze.num_explored}")

    # Output maze
    maze.print()
    maze.output_image("maze.png", show_explored=True)