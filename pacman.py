import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Dimensi layar
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
GRID_SIZE = 20
ROWS, COLS = SCREEN_HEIGHT // GRID_SIZE, SCREEN_WIDTH // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Kecepatan Pac-Man
PACMAN_SPEED = 20

# Posisi awal Pac-Man
pacman_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
pacman_direction = [0, 0]

# Inisialisasi titik-titik makanan
food_positions = []
for _ in range(30):  # jumlah makanan
    food_x = random.randint(0, COLS - 1) * GRID_SIZE
    food_y = random.randint(0, ROWS - 1) * GRID_SIZE
    food_positions.append((food_x, food_y))

# Fungsi untuk menggambar Pac-Man dan makanan
def draw_pacman():
    pygame.draw.circle(screen, YELLOW, pacman_pos, GRID_SIZE // 2)

def draw_food():
    for pos in food_positions:
        pygame.draw.circle(screen, WHITE, pos, GRID_SIZE // 4)

# Fungsi untuk menggerakkan Pac-Man
def move_pacman():
    pacman_pos[0] += pacman_direction[0] * PACMAN_SPEED
    pacman_pos[1] += pacman_direction[1] * PACMAN_SPEED

    # Batasi agar tidak keluar dari layar
    pacman_pos[0] = pacman_pos[0] % SCREEN_WIDTH
    pacman_pos[1] = pacman_pos[1] % SCREEN_HEIGHT

# Fungsi untuk mendeteksi makanan yang dimakan
def check_food_collision():
    global food_positions
    pacman_rect = pygame.Rect(pacman_pos[0] - GRID_SIZE // 2, pacman_pos[1] - GRID_SIZE // 2, GRID_SIZE, GRID_SIZE)
    food_positions = [food for food in food_positions if not pacman_rect.collidepoint(food)]

# Fungsi utama game loop
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman_direction[0] = -1
                    pacman_direction[1] = 0
                elif event.key == pygame.K_RIGHT:
                    pacman_direction[0] = 1
                    pacman_direction[1] = 0
                elif event.key == pygame.K_UP:
                    pacman_direction[0] = 0
                    pacman_direction[1] = -1
                elif event.key == pygame.K_DOWN:
                    pacman_direction[0] = 0
                    pacman_direction[1] = 1

        # Pergerakan Pac-Man dan cek makanan
        move_pacman()
        check_food_collision()

        # Menggambar objek
        draw_pacman()
        draw_food()

        # Update layar
        pygame.display.flip()
        clock.tick(10)  # FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
