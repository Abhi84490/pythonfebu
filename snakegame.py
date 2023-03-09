import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption of the game window
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the font for the score text
font = pygame.font.SysFont(None, 25)

# Define the size of each block in the game grid
block_size = 10

# Define the function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, [0, 0])

# Define the function to display the snake
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, black, [block[0], block[1], block_size, block_size])

# Define the main function for the game
def game_loop():
    # Set the starting position and length of the snake
    snake_length = 1
    snake_list = []
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake_list.append([snake_x, snake_y])

    # Set the initial position of the apple
    apple_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    apple_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    # Set the initial score to zero
    score = 0

    # Set the initial direction of the snake
    direction = "right"

    # Set the initial speed of the snake
    speed = 10

    # Set the game loop flag
    game_exit = False

    # Start the game loop
    while not game_exit:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                elif event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"

        # Move the snake
        if direction == "right":
            snake_x += speed
        elif direction == "left":
            snake_x -= speed
        elif direction == "up":
            snake_y -= speed
        elif direction == "down":
            snake_y += speed

        # Check if the snake has hit the edge of the screen
        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_exit = True

        # Check if the snake has collided with itself
        for block in snake_list[1:]:
            if block[0] == snake_x and block[1] == snake_y:
                game_exit = True
