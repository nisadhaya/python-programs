import tkinter as tk
import random

# Game Settings
WIDTH = 400
HEIGHT = 600
SPEED = 20
OBSTACLE_SPEED = 8
LANE_WIDTH = WIDTH // 3  # Divides the screen into 3 lanes

class SubwaySurfers:
    def __init__(self, window):
        self.window = window
        self.window.title("Subway Surfers 2D")

        # Game Variables
        self.score = 0
        self.player_lane = 1  # 0 = Left, 1 = Center, 2 = Right
        self.is_jumping = False
        self.jump_count = 0

        # Score Display
        self.label = tk.Label(window, text=f"Score: {self.score}", font=("Arial", 20))
        self.label.pack()

        # Canvas (Game Screen)
        self.canvas = tk.Canvas(window, bg="gray", height=HEIGHT, width=WIDTH)
        self.canvas.pack()

        # Draw Lane Separators (Tracks)
        self.canvas.create_line(LANE_WIDTH, 0, LANE_WIDTH, HEIGHT, fill="white", dash=(5, 5))
        self.canvas.create_line(LANE_WIDTH * 2, 0, LANE_WIDTH * 2, HEIGHT, fill="white", dash=(5, 5))

        # Create Player (Blue Square)
        self.player = self.canvas.create_rectangle(
            0, 0, 40, 40, fill="blue", outline="white"
        )
        self.update_player_position()

        # List to store active obstacles
        self.obstacles = []
        
        # Controls Bindings
        self.window.bind('<Left>', lambda event: self.move_lane(-1))
        self.window.bind('<Right>', lambda event: self.move_lane(1))
        self.window.bind('<Up>', lambda event: self.jump())

        # Start Game Elements
        self.spawn_obstacle()
        self.game_loop()

    def update_player_position(self):
        # Calculate X coordinate based on current lane
        x_start = (self.player_lane * LANE_WIDTH) + (LANE_WIDTH // 2) - 20
        y_start = HEIGHT - 100
        
        # If jumping, shift the player higher up on the screen
        if self.is_jumping:
            y_start -= 60  

        self.canvas.coords(self.player, x_start, y_start, x_start + 40, y_start + 40)

    def move_lane(self, direction):
        # Change lanes (Keep within bounds 0 and 2)
        new_lane = self.player_lane + direction
        if 0 <= new_lane <= 2:
            self.player_lane = new_lane
            self.update_player_position()

    def jump(self):
        # Trigger jump mechanism
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_count = 15  # Duration of the jump
            self.update_player_position()

    def spawn_obstacle(self):
        # Choose a random lane for the obstacle
        lane = random.randint(0, 2)
        x_start = (lane * LANE_WIDTH) + (LANE_WIDTH // 2) - 20
        
        # Create Obstacle (Red Rectangle)
        obstacle = self.canvas.create_rectangle(
            x_start, 0, x_start + 40, 30, fill="red"
        )
        self.obstacles.append((obstacle, lane))
        
        # Spawn next obstacle after 1.5 seconds (1500ms)
        self.window.after(1500, self.spawn_obstacle)

    def game_loop(self):
        # Handle Jump timing
        if self.is_jumping:
            self.jump_count -= 1
            if self.jump_count <= 0:
                self.is_jumping = False
                self.update_player_position()

        # Move obstacles down and check for collisions
        for obstacle, lane in self.obstacles[:]:
            self.canvas.move(obstacle, 0, OBSTACLE_SPEED)
            pos = self.canvas.coords(obstacle)

            # If obstacle goes off-screen, delete it and increase score
            if pos[1] >= HEIGHT:
                self.canvas.delete(obstacle)
                self.obstacles.remove((obstacle, lane))
                self.score += 1
                self.label.config(text=f"Score: {self.score}")

            # Collision Detection
            player_pos = self.canvas.coords(self.player)
            
            # Check if obstacle is in the same lane and player is NOT jumping over it
            if lane == self.player_lane and not self.is_jumping:
                if player_pos[1] < pos[3] and player_pos[3] > pos[1]:
                    self.game_over()
                    return

        # Repeat the game loop
        self.window.after(SPEED, self.game_loop)

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(
            WIDTH / 2, HEIGHT / 2,
            font=("Arial", 30, "bold"),
            text="GAME OVER", fill="red"
        )

# Main Window Initialization
root = tk.Tk()
game = SubwaySurfers(root)
root.mainloop()
