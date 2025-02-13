import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLUE = (50, 153, 213)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 102)

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout Game")

# Set up the paddle
paddle_width = 100
paddle_height = 15
paddle_speed = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 40

# Set up the ball
ball_radius = 10
ball_x = screen_width // 2
ball_y = paddle_y - ball_radius
ball_dx = random.choice([-4, 4])  # Horizontal speed
ball_dy = -4  # Vertical speed

# Set up the bricks
brick_width = 75
brick_height = 25
bricks = []

for i in range(7):
    for j in range(5):
        brick_x = i * (brick_width + 10) + 35
        brick_y = j * (brick_height + 10) + 35
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# Game variables
score = 0
font = pygame.font.SysFont("comicsansms", 20)
clock = pygame.time.Clock()

# Function to display the score
def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])

# Function to draw everything
def draw_screen():
    screen.fill(BLUE)
    pygame.draw.rect(screen, GREEN, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, YELLOW, (ball_x, ball_y), ball_radius)
    
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    show_score()
    pygame.display.update()

# Main game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with the walls
    if ball_x <= 0 or ball_x >= screen_width:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1
    if ball_y >= screen_height:
        running = False  # Game over if the ball falls below the screen

    # Ball collision with the paddle
    if paddle_y < ball_y + ball_radius < paddle_y + paddle_height and paddle_x < ball_x < paddle_x + paddle_width:
        ball_dy *= -1

    # Ball collision with bricks
    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y):
            ball_dy *= -1
            bricks.remove(brick)  # Remove the brick
            score += 10  # Increase score
            break

    # If no more bricks are left, the player wins
    if len(bricks) == 0:
        running = False
        print("You win!")

    # Draw everything on the screen
    draw_screen()

pygame.quit()
quit()
