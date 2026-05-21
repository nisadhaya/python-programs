import tkinter as tk
import random

# Game settings
WIDTH = 500
HEIGHT = 500
SPEED = 100
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Initial snake body
        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x,
                y,
                x + SPACE_SIZE,
                y + SPACE_SIZE,
                fill=SNAKE_COLOR,
                outline="white"
            )

            self.squares.append(square)


class Food:

    def __init__(self):

        x = random.randint(
            0,
            (WIDTH // SPACE_SIZE) - 1
        ) * SPACE_SIZE

        y = random.randint(
            0,
            (HEIGHT // SPACE_SIZE) - 1
        ) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(
            x,
            y,
            x + SPACE_SIZE,
            y + SPACE_SIZE,
            fill=FOOD_COLOR,
            tag="food"
        )


def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    # Add new head
    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x,
        y,
        x + SPACE_SIZE,
        y + SPACE_SIZE,
        fill=SNAKE_COLOR,
        outline="white"
    )

    snake.squares.insert(0, square)

    # Check if food eaten
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text=f"Score: {score}")

        canvas.delete("food")

        food = Food()

    else:

        # Remove tail
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(
            SPEED,
            next_turn,
            snake,
            food
        )


def change_direction(new_direction):

    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction

    elif new_direction == "right":
        if direction != "left":
            direction = new_direction

    elif new_direction == "up":
        if direction != "down":
            direction = new_direction

    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collisions(snake):

    x, y = snake.coordinates[0]

    # Wall collision
    if x < 0 or x >= WIDTH:
        return True

    if y < 0 or y >= HEIGHT:
        return True

    # Self collision
    for body_part in snake.coordinates[1:]:

        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():

    canvas.delete(tk.ALL)

    canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2,
        font=("Arial", 40, "bold"),
        text="GAME OVER",
        fill="red"
    )


# Main window
window = tk.Tk()

window.title("Snake Game")

score = 0
direction = "down"

label = tk.Label(
    window,
    text=f"Score: {score}",
    font=("Arial", 20)
)

label.pack()

canvas = tk.Canvas(
    window,
    bg=BACKGROUND_COLOR,
    height=HEIGHT,
    width=WIDTH
)

canvas.pack()

window.update()

# Center window
window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Controls
window.bind('<Left>', lambda event: change_direction("left"))
window.bind('<Right>', lambda event: change_direction("right"))
window.bind('<Up>', lambda event: change_direction("up"))
window.bind('<Down>', lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
