def draw_square(coordinates, side_length):
    x, y = coordinates
    square = [(x,y), (x,y+side_length), (x+side_length, y), (x+side_length, y+side_length)]
    print("square:")
    print(square)
    return square
