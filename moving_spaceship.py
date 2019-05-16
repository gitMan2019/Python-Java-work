# Spaceship that responds to keyboard input,
# Or to a Logitech controller, if you have one.
# The asteroid can be moved with the mouse
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (172, 177, 181)
YELLOW = (255, 255, 0)
 
pygame.init()

# Function that draws spaceship based on drawing code below
def draw_ship(screen, x, y):
    pygame.draw.polygon(screen, RED, [ [50-50+x, 100-100+y], [50-50+x, 300-100+y], [200-50+x, 200-100+y] ])
    pygame.draw.rect(screen, GREEN, [60-50+x, 175-100+y, 50, 50])	

# Function the draws asteroid based on drawing code below
def draw_asteroid(screen, x, y):
    pygame.draw.rect(screen, GREY, [300-300+x, 300-300+y, 80, 80])
    pygame.draw.rect(screen, BLACK, [320-300+x, 350-300+y, 20, 20])
    pygame.draw.rect(screen, BLACK, [345-300+x, 335-300+y, 20, 20])


def draw_stars(screen, x, y):
    pygame.draw.line(screen, YELLOW, [300, 500], [300, 700], 2)

# Set the width and height of the screen [width, height]
size = (700, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Moving Spaceship")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Sets ship speed for later use
x_speed = 0
y_speed = 0

# Starting position of spaceship
x_coord = 30
y_coord = 30

# Starting points of star lines
# Vertical line
star_x = 300
star_y = 400

star_2x = 300
star_2y = 500

# Horizontal line
star2_x = 250
star2_y = 450

star2_2x = 350
star2_2y = 450

# Diagonal line
star3_x = 250
star3_y = 400

star3_2x = 350
star3_2y = 500

# Increments for star
# Vertical line increments
star_change_x = 3
star_change_y = 3

star_change_2x = 3
star_change_2y = 3

# Horizontal line increments
star2_change_x = 3
star2_change_y = 3

star2_change_2x = 3
star2_change_2y = 3

# Diagonal line increments
star3_change_x = 3
star3_change_y = 3

star3_change_2x = 3
star3_change_2y = 3

# Makes mouse cursor invisible on screen
pygame.mouse.set_visible(False)

# Count the joysticks the computer has
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0

        # This goes in the main program loop!
        # As long as there is a joystick
        if joystick_count != 0:
 
            # This gets the position of the axis on the game controller
            # It returns a number between -1.0 and +1.0
            horiz_axis_pos = my_joystick.get_axis(0)
            vert_axis_pos = my_joystick.get_axis(1)
 
            # Move x according to the axis. We multiply by 10 to speed up the movement.
            # Convert to an integer because we can't draw at pixel 3.5, just 3 or 4.
            x_coord = x_coord + int(horiz_axis_pos * 10)
            y_coord = y_coord + int(vert_axis_pos * 10)

    # --- Game logic should go here

    # Sets variable for cursor position (x, y)
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    # Changes starting position of ship according to user input
    x_coord += x_speed
    y_coord += y_speed

    if x_coord > 549:
        x_coord = 548

    if x_coord < 1:
        x_coord = 2

    if y_coord > 499:
        y_coord = 498

    if y_coord < 1:
        y_coord = 2

    if x_coord == x and y_coord == y:
        done = True
        print("Oh no! The spaceship collided with the asteroid!")

    # Keeps star bouncing off edges

    # Bounces star off bottom
    if star_2y > 699:
        star_change_x *= -1
        star_change_y *= -1
        star_change_2x *= -1
        star_change_2y *= -1

        star2_change_x *= -1
        star2_change_y *= -1
        star2_change_2x *= -1
        star2_change_2y *= -1

        star3_change_x *= -1
        star3_change_y *= -1
        star3_change_2x *= -1
        star3_change_2y *= -1	

    # Bounces star off left edge
    if star2_x < 1:
        star_change_x *= -1
        star_change_y *= 1
        star_change_2x *= -1
        star_change_2y *= 1

        star2_change_x *= -1
        star2_change_y *= 1
        star2_change_2x *= -1
        star2_change_2y *= 1

        star3_change_x *= -1
        star3_change_y *= 1
        star3_change_2x *= -1
        star3_change_2y *= 1

    # Bounces star off top edge
    if star_y < 1:
        star_change_x *= 1
        star_change_y *= -1
        star_change_2x *= 1
        star_change_2y *= -1

        star2_change_x *= 1
        star2_change_y *= -1
        star2_change_2x *= 1
        star2_change_2y *= -1

        star3_change_x *= 1
        star3_change_y *= -1
        star3_change_2x *= 1
        star3_change_2y *= -1

    # Bounces star off right edge
    if star2_2x > 699:
        star_change_x *= -1
        star_change_y *= 1
        star_change_2x *= -1
        star_change_2y *= 1

        star2_change_x *= -1
        star2_change_y *= 1
        star2_change_2x *= -1
        star2_change_2y *= 1

        star3_change_x *= -1
        star3_change_y *= 1
        star3_change_2x *= -1
        star3_change_2y *= 1

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here

    # Draws star that bounces

    # Vertical line
    pygame.draw.line(screen, YELLOW, [star_x, star_y], [star_2x, star_2y], 2)
    star_x += star_change_x
    star_y += star_change_y

    star_2x += star_change_2x
    star_2y += star_change_2y

    # Horizontal line
    pygame.draw.line(screen, YELLOW, [star2_x, star2_y], [star2_2x, star2_2y], 2)
    star2_x += star2_change_x
    star2_y += star2_change_y

    star2_2x += star2_change_2x
    star2_2y += star2_change_2y

    # Diagonal line
    pygame.draw.line(screen, YELLOW, [star3_x, star3_y], [star3_2x, star3_2y], 2)
    star3_x += star3_change_x
    star3_y += star3_change_y

    star3_2x += star3_change_2x
    star3_2y += star3_change_2y

    # Draws asteroid at position of the cursor
    draw_asteroid(screen, x, y)

    # Draws ship at using function above
    # and event processing loop
    draw_ship(screen, x_coord, y_coord)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(40)
 
# Close the window and quit.
pygame.quit()
