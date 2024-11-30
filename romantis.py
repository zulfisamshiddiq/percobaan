import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Warna
RED = (255, 0, 0)
PINK = (255, 192, 203)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Romantic Design")

# Font
font = pygame.font.Font(pygame.font.get_default_font(), 40)

# Gambar hati
def draw_heart(surface, color, x, y, size):
    top_circle = (x + size // 2, y + size // 4)
    left_circle = (x, y + size // 4)
    bottom_point = (x + size // 2, y + size)
    triangle_points = [
        (x, y + size // 2),
        bottom_point,
        (x + size, y + size // 2)
    ]

    pygame.draw.circle(surface, color, top_circle, size // 4)
    pygame.draw.circle(surface, color, left_circle, size // 4)
    pygame.draw.polygon(surface, color, triangle_points)

# Teks
def draw_text(surface, text, font, color, pos):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=pos)
    surface.blit(text_surface, text_rect)

# Loop utama
running = True
while running:
    screen.fill(PINK)  # Latar belakang warna pink

    # Gambar hati
    draw_heart(screen, RED, WIDTH // 2 - 100, HEIGHT // 2 - 100, 200)

    # Teks romantis
    draw_text(screen, "You are my everything", font, GOLD, (WIDTH // 2, HEIGHT // 2 + 50))

    pygame.display.flip()

    # Keluar program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
