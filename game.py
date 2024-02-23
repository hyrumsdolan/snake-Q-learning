import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Snake Game')
game_over = False
points = 0

# Screen setup
screen_size = 800
screen = pygame.display.set_mode((screen_size, screen_size))
grid_size = screen_size / 10

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)

# Boundary Setup
boundary = {
  "top": 0,
  "bottom": screen_size/grid_size-1,
  "left": 0,
  "right": screen_size/grid_size-1
}

# Snake Setup
snake_head_pos = (5, 5)
snake_tail = []
snake_direction = "UP"
snake_tail_length = 0
def snake_pos(index):
  return (snake_head_pos[index] * grid_size)
  
# Food Setup
food_pos = (random.randint(0, 9), random.randint(0, 9))
def randomize_food():
  global food_pos
  food_pos = (random.randint(0, 9), random.randint(0, 9))


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
              snake_direction = "UP"
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
              snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
              snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
              snake_direction = "RIGHT"

    


    if snake_direction == "UP":
      snake_head_pos = (snake_head_pos[0], snake_head_pos[1] - 1)
    elif snake_direction == "DOWN":
      snake_head_pos = (snake_head_pos[0], snake_head_pos[1] + 1)
    elif snake_direction == "LEFT":
      snake_head_pos = (snake_head_pos[0] - 1, snake_head_pos[1])
    elif snake_direction == "RIGHT":
      snake_head_pos = (snake_head_pos[0] + 1, snake_head_pos[1])

    if snake_head_pos[0] < boundary["left"] or snake_head_pos[0] > boundary["right"] or snake_head_pos[1] < boundary["top"] or snake_head_pos[1] > boundary["bottom"]:
      game_over = True

    
    

    if snake_head_pos == food_pos:
      randomize_food()
      points += 1
      snake_tail_length += 1

  


    

    #DISPLAY
    # Fill the screen with black
    screen.fill(black)
    
    pygame.draw.rect(screen, green, (snake_pos(0), snake_pos(1), grid_size, grid_size))
    pygame.draw.rect(screen, white, (food_pos[0] * grid_size, food_pos[1] * grid_size, grid_size, grid_size))
    print(snake_tail)
    for segment in snake_tail:
      pygame.draw.rect(screen, white, (segment[0] * grid_size, segment[1] * grid_size, grid_size, grid_size))
      if snake_head_pos == segment:
        game_over = True
    

    if game_over:
      font = pygame.font.Font(None, 60)
      text = font.render('GAME OVER', True, white, black)
      text_rect = text.get_rect()
      text_rect.center = (screen_size // 2, screen_size // 2)
      screen.blit(text, text_rect)
      pygame.display.flip()

     
      while game_over:
          for event in pygame.event.get():  # Process events to keep the game responsive
              if event.type == pygame.QUIT:  # Allows the window to be closed
                  game_over = False

          if pygame.key.get_pressed()[pygame.K_SPACE]:
              snake_head_pos = (5, 5)
              game_over = False
          elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()



    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(5)

pygame.quit()
sys.exit()