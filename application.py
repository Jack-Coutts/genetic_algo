import streamlit as st
from PIL import Image, ImageDraw
import time

# Define the sizes and positions of the squares and circles
square_size = 700
target_square_size = 25
circle_size = 10
circle_positions_1 = [(100, 100), (200, 200), (300, 300), (400, 400), (500, 500)]
circle_positions_2 = [(150, 200), (250, 300), (350, 400), (450, 500), (550, 600)]

# Define the colors for the squares and circles
big_square_color = (254, 220, 194)
target_square_color = (255, 87, 51)
circle_color = (51, 153, 255)


# Define the function to draw the squares and circles
def draw_squares_and_circles(circle_positions):
    # Create a new image with the big square color
    image = Image.new("RGB", (square_size, square_size), big_square_color)
    # Draw the target square with the target square color
    draw = ImageDraw.Draw(image)
    draw.rectangle((square_size / 2 - target_square_size / 2, square_size / 2 - target_square_size / 2,
                    square_size / 2 + target_square_size / 2, square_size / 2 + target_square_size / 2),
                   fill=target_square_color)
    # Draw the circles with the circle color
    for pos in circle_positions:
        draw.ellipse((square_size / 2 - target_square_size / 2 + pos[0] - circle_size / 2,
                      square_size / 2 - target_square_size / 2 + pos[1] - circle_size / 2,
                      square_size / 2 - target_square_size / 2 + pos[0] + circle_size / 2,
                      square_size / 2 - target_square_size / 2 + pos[1] + circle_size / 2),
                     fill=circle_color)
    return image


# Define the main function
def main():
    st.title("Genetic Algorithms")


    # Iterate over the different images (positions of circles)
    image = st.empty()
    for item in range(10):
        if item % 2:
            a = circle_positions_1
        else:
            a = circle_positions_2
        image.image(draw_squares_and_circles(a), use_column_width=True)
        time.sleep(0.3)


# Call the main function
if __name__ == "__main__":
    main()
