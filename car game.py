import os
import random
import time

def play_car_game():
    # Game setup
    WIDTH = 7
    HEIGHT = 10
    car_pos = 3  # Start in the middle column
    obstacle_row = 0
    obstacle_col = random.randint(0, WIDTH - 1)
    score = 0
    game_speed = 0.3 # Seconds per frame (lower = faster)

    print("🚘 WELCOME TO TERMINAL RACER! 🚘")
    print("Controls: Type 'a' to go Left, 'd' to go Right, then press Enter.")
    print("Press Enter without typing to just move forward.")
    input("Press Enter to START...")

    while True:
        # 1. Clear the screen (works on Windows/Mac/Linux)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # 2. Draw the game board
        print(f"SCORE: {score}")
        print("-" * (WIDTH + 2)) # Top border
        
        for row in range(HEIGHT):
            line = "|"
            for col in range(WIDTH):
                if row == HEIGHT - 1 and col == car_pos:
                    line += "🚗"  # Your car
                elif row == obstacle_row and col == obstacle_col:
                    line += "🚧"  # Obstacle
                else:
                    line += "  "  # Empty road space
            line += "|"
            print(line)
            
        print("-" * (WIDTH + 2)) # Bottom border

        # 3. Check for Crash (Collision)
        if obstacle_row == HEIGHT - 1 and obstacle_col == car_pos:
            print("\n💥 BOOM! You crashed! 💥")
            print(f"Final Score: {score}")
            break

        # 4. Get Player Input
        move = input("Move (a/d): ").lower()
        if move == 'a' and car_pos > 0:
            car_pos -= 1
        elif move == 'd' and car_pos < WIDTH - 1:
            car_pos += 1

        # 5. Move the obstacle down
        obstacle_row += 1
        
        # If obstacle goes off screen, reset it and give a point
        if obstacle_row >= HEIGHT:
            obstacle_row = 0
            obstacle_col = random.randint(0, WIDTH - 1)
            score += 1
            # Make the game slightly faster as score increases
            game_speed = max(0.1, 0.3 - (score * 0.01))

# Run the game
play_car_game()
