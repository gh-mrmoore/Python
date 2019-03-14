rect1 = ((2,1), (5,5))
rect2 = ((3,2), (5,7))

point1 = rect1[0]
point2 = rect1[1]
point3 = rect2[0]
point4 = rect2[1]

#x_coords = 
sorted_x_coords = sorted([point1[0], point2[0], point3[0], point4[0]])
#y_coords = 
sorted_y_coords = sorted([point1[1], point2[1], point3[1], point4[1]])

def horizontal_overlay(x_coords):
    x_length = sorted_x_coords[1] - sorted_x_coords[2]
    
    return x_length

def vertical_overlay(y_coords):
    y_length = sorted_y_coords[1] - sorted_y_coords[2]

    return y_length

def overlap_area(x_coords, y_coords):
    area = horizontal_overlay(x_coords) * vertical_overlay(y_coords)

    return area

print(overlap_area(sorted_x_coords, sorted_y_coords))