import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
GRID_SIZE = 30  # Size of the blocks
COLUMNS, ROWS = 10, 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SHAPES_COLORS = [(0, 255, 255), (255, 165, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (128, 0, 128)]

# Tetris shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
]

# Shape class to handle rotation and movement
class Shape:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(SHAPES_COLORS)
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

# Main Tetris game class
class Tetris:
    def __init__(self):
        self.grid = [[BLACK] * COLUMNS for _ in range(ROWS)]
        self.current_shape = Shape()
        self.score = 0

    def check_collision(self, dx, dy, shape=None):
        shape = shape or self.current_shape
        for y, row in enumerate(shape.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = shape.x + x + dx
                    new_y = shape.y + y + dy
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS or (new_y >= 0 and self.grid[new_y][new_x] != BLACK):
                        return True
        return False

    def merge_shape(self):
        for y, row in enumerate(self.current_shape.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_shape.y + y][self.current_shape.x + x] = self.current_shape.color

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == BLACK for cell in row)]
        lines_cleared = ROWS - len(new_grid)
        self.score += lines_cleared ** 2
        self.grid = [[BLACK] * COLUMNS for _ in range(lines_cleared)] + new_grid

    def move_shape_down(self):
        if not self.check_collision(0, 1):
            self.current_shape.y += 1
        else:
            self.merge_shape()
            self.clear_lines()
            self.current_shape = Shape()
            if self.check_collision(0, 0):
                return False  # Game over
        return True

    def move_shape(self, dx):
        if not self.check_collision(dx, 0):
            self.current_shape.x += dx

    def rotate_shape(self):
        rotated_shape = Shape()
        rotated_shape.shape = [list(row) for row in zip(*self.current_shape.shape[::-1])]
        if not self.check_collision(0, 0, rotated_shape):
            self.current_shape.rotate()

    def draw_grid(self):
        for y, row in enumerate(self.grid):
            for x, color in enumerate(row):
                pygame.draw.rect(screen, color, pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
        for y, row in enumerate(self.current_shape.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.current_shape.color, pygame.Rect((self.current_shape.x + x) * GRID_SIZE, (self.current_shape.y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

# Game loop
def main():
    clock = pygame.time.Clock()
    tetris = Tetris()
    fall_time = 0

    running = True
    while running:
        screen.fill(BLACK)
        fall_speed = 500  # Speed in milliseconds
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time > fall_speed:
            fall_time = 0
            if not tetris.move_shape_down():
                running = False  # Game over

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetris.move_shape(-1)
                elif event.key == pygame.K_RIGHT:
                    tetris.move_shape(1)
                elif event.key == pygame.K_DOWN:
                    tetris.move_shape_down()
                elif event.key == pygame.K_UP:
                    tetris.rotate_shape()

        tetris.draw_grid()
        tetris.draw_score()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

