def draw_square(coordinates, side_length):
    x, y = coordinates
    square = [(x,y), (x,y+side_length), (x+side_length, y), (x+side_length, y+side_length)]
    print("square:")
    print(square)
    return square

def draw_circle(coordinates, radius):
    x, y = coordinates
    circle = [(x, y+radius), (x, y-radius), (x+radius, y), (x-radius, y)]
    return circle

def vector_move(shape_array, vector):
    moved_shape = []
    move_x, move_y = vector
    for coordinates in shape_array:
        x, y = coordinates
        new_coordinates = (x+move_x, y+move_y)
        moved_shape.append(new_coordinates)
    return moved_shape
