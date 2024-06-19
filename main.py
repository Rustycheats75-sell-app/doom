from microbit import *
import random

# Initial player position
player_x = 2
player_y = 2

# Function to update the display with the player's position and obstacles
def display_grid(player_x, player_y, obstacle_x, obstacle_y):
    display.clear()
    if (player_x, player_y) == (obstacle_x, obstacle_y):
        display.show(Image.SAD)
        return False
    display.set_pixel(player_x, player_y, 9)
    display.set_pixel(obstacle_x, obstacle_y, 5)
    return True

# Generate a random obstacle position
obstacle_x = random.randint(0, 4)
obstacle_y = random.randint(0, 4)

# Ensure the obstacle is not placed at the initial player position
while (obstacle_x, obstacle_y) == (player_x, player_y):
    obstacle_x = random.randint(0, 4)
    obstacle_y = random.randint(0, 4)

# Display the initial grid
game_running = display_grid(player_x, player_y, obstacle_x, obstacle_y)

while game_running:
    if button_a.was_pressed():
        # Move left
        player_x = max(0, player_x - 1)
    elif button_b.was_pressed():
        # Move right
        player_x = min(4, player_x + 1)
    
    if accelerometer.was_gesture('up'):
        # Move up
        player_y = max(0, player_y - 1)
    elif accelerometer.was_gesture('down'):
        # Move down
        player_y = min(4, player_y + 1)
    
    # Update the display with the new position
    game_running = display_grid(player_x, player_y, obstacle_x, obstacle_y)
    
    # Add a short delay to avoid overwhelming the micro:bit
    sleep(100)
