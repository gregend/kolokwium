def draw_square(coordinates, side_length=1):
    """
    Returns list of tuples which are coordinates 
    of a square drawn in cartesian coordinate system

    coordinates -- anchor point around which square is drawn
    side_length -- length of the squares side (default 1) 
    """
    x, y = coordinates
    square = [(x,y), (x,y+side_length), (x+side_length, y), (x+side_length, y+side_length)]
    return square

def draw_circle(coordinates, radius=1):
    """
    Returns list of tuples which are coordinates 
    of a circle drawn in cartesian coordinate system

    coordinates -- anchor point around which circle is drawn
    radius -- radius of drawn circle (default 1) 
    """
    x, y = coordinates
    circle = [(x, y+radius), (x, y-radius), (x+radius, y), (x-radius, y)]
    return circle

def vector_move(shape_array, vector):
    """
    Returns list of tuples which are coordinates 
    of a shape drawn in cartesian coordinate system
    moved by given vector

    shape_array -- list composed of coordinates of drawn shape
    vector -- tuple describing vector the shape is to be moved  by 
    """
    moved_shape = []
    move_x, move_y = vector
    for coordinates in shape_array:
        x, y = coordinates
        new_coordinates = (x+move_x, y+move_y)
        moved_shape.append(new_coordinates)
    return moved_shape
