# Randomness Perpetua
"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

PI = 3.14159

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)

pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Randomness Perpetua")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Rectangle starting point for x
rect_x = 0

# Rectangle increment
rect_change_x = 5

# Yellow circle starting point for y
cir_y = 50

# Yellow circle increment
cir_change_y = 5

# Orange circle starting point for x
cir_x = 150

# Orange circle increment
cir_change_x = 5

# Starting points for stick figure
# Starting points for left leg
leg1_x = 200
leg1_y = 500

leg1_2x = 250
leg1_2y = 400

# Increments for left leg
leg1_change_x = 2
leg1_change_y = 0

leg1_change_2x = 2
leg1_change_2y = 0

# Starting points for right leg
leg2_x = 300
leg2_y = 500

leg2_2x = 250
leg2_2y = 400

# Increments for right leg
leg2_change_x = 2
leg2_change_y = 0

leg2_change_2x = 2
leg2_change_2y = 0

# Starting points for body
body_x = 250
body_y = 400

body_2x = 250
body_2y = 300

# Increments for body
body_change_x = 2
body_change_y = 0

body_change_2x = 2
body_change_2y = 0

# Starting points for left arm
arm1_x = 200
arm1_y = 350

arm1_2x = 250
arm1_2y = 350

# Increments for left arm
arm1_change_x = 2
arm1_change_y = 0

arm1_change_2x = 2
arm1_change_2y = 0

# Starting points for right arm
arm2_x = 250
arm2_y = 350

arm2_2x = 300
arm2_2y = 350

# Increments for right arm
arm2_change_x = 2
arm2_change_y = 0

arm2_change_2x = 2
arm2_change_2y = 0

# Starting points for head
head_x = 220
head_y = 240

# Increments for head
head_change_x = 2
head_change_y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    if cir_y > 659 or cir_y < 42:
        cir_change_y *= -1

    if cir_x > 659 or cir_x < 150:
        cir_change_x *= -1

    if arm2_2x > 500:
        leg1_change_x = 0
        leg1_change_y = 5

        leg1_change_2x = 0
        leg1_change_2y = 5

        leg2_change_x = 0
        leg2_change_y = 5

        leg2_change_2x = 0
        leg2_change_2y = 5

        body_change_x = 0
        body_change_y = 5

        body_change_2x = 0
        body_change_2y = 5

        arm1_change_x = 0
        arm1_change_y = 5

        arm1_change_2x = 0
        arm1_change_2y = 5

        arm2_change_x = 0
        arm2_change_y = 5

        arm2_change_2x = 0
        arm2_change_2y = 5

        head_change_x = 0
        head_change_y = 5

    if head_y > 699:
        done = True

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE)

    # --- Drawing code should go here

    # Prints more silly text when arm reaches certain point
    if arm2_2x > 500:
        font = pygame.font.SysFont("Calibri", 25, True, False)
        text = font.render("Oh no! Mr. Bill!", True, WHITE)
        screen.blit(text, [150, 180])	


    # Printing silly text to screen
    font = pygame.font.SysFont("Calibri", 25, True, False)
    text = font.render("Two suns?! I must be on Tatooine.", True, WHITE)
    screen.blit(text, [150, 150])

    # Draw green rectangle for ground
    pygame.draw.rect(screen, GREEN, [rect_x, 500, 700, 200])
    rect_x += rect_change_x

    # Draw yellow circle for sun
    pygame.draw.circle(screen, YELLOW, [50, cir_y], 40)
    cir_y += cir_change_y

    # Draw orange circle for other sun
    pygame.draw.circle(screen, ORANGE, [cir_x, 50], 40)
    cir_x += cir_change_x

    # Draw two legs for body of guy
    pygame.draw.line(screen, BLACK, [leg1_x, leg1_y], [leg1_2x, leg1_2y], 3)

    # Only need to horizontally move leg
    leg1_x += leg1_change_x
    leg1_y += leg1_change_y

    leg1_2x += leg1_change_2x
    leg1_2y += leg1_change_2y    

    # Only need to horizontally move leg
    pygame.draw.line(screen, BLACK, [leg2_x, leg2_y], [leg2_2x, leg2_2y], 3)

    leg2_x += leg2_change_x
    leg2_y += leg2_change_y    	

    leg2_2x += leg2_change_2x
    leg2_2y += leg2_change_2y

    # Draw line for body and another for arms
    pygame.draw.line(screen, BLACK, [body_x, body_y], [body_2x, body_2y], 3)
    body_x += body_change_x
    body_y += body_change_y

    body_2x += body_change_2x
    body_2y += body_change_2y

    # Draw line for left arm
    pygame.draw.line(screen, BLACK, [arm1_x, arm1_y], [arm1_2x, arm1_2y], 3)

    arm1_x += arm1_change_x
    arm1_y += arm1_change_y

    arm1_2x += arm1_change_2x
    arm1_2y += arm1_change_2y	

    # Draw line for right arm
    pygame.draw.line(screen, BLACK, [arm2_x, arm2_y], [arm2_2x, arm2_2y], 3)

    arm2_x += arm2_change_x
    arm2_y += arm2_change_y

    arm2_2x += arm2_change_2x
    arm2_2y += arm2_change_2y  	

    # Draw full circle arc for head
    pygame.draw.arc(screen, BLACK, [head_x, head_y, 60, 60], 0, 2*PI, 3)

    head_x += head_change_x
    head_y += head_change_y

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(20)

# Close the window and quit.
pygame.quit()
