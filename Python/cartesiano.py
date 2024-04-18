def point_location(rectangle, point):
    x_min, y_min = rectangle
    x_max, y_max = x_min + (x_max - x_min), y_min + (y_max - y_min)
    if (x_min <= point[0] <= x_max and y_min <= point[1] <= y_max):
        print("O ponto está dentro do retângulo.")
    elif (point[0] == x_min or point[0] == x_max or point[1] == y_min or point[1] == y_max):
        print("O ponto está na borda do retângulo.")
    else:
        print("O ponto está fora do retângulo.")