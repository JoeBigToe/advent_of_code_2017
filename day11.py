coordinates_dictionary = {
    'n' : [1, 0],
    'ne': [0.5, 0.5],
    'se': [-0.5, 0.5],
    's' : [-1, 0],
    'sw': [-0.5, -0.5],
    'nw': [0.5, -0.5]
}

def calculate(acc, coordinate):
    acc[0] += coordinates_dictionary[coordinate][0]
    acc[1] += coordinates_dictionary[coordinate][1]
    return acc

def calculate_distance(coordinate_map):
    acc = [0,0]
    max_distance = 0

    for coordinate in coordinate_map:
        acc = calculate(acc, coordinate)
        distance = sum([abs(axis) for axis in acc])
        if distance > max_distance:
            max_distance = distance

    return max_distance

# print(calculate_distance(['ne','ne','ne']))
# print(calculate_distance(['ne','ne','sw','sw']))
# print(calculate_distance(['ne','ne','s',"s"]))
# print(calculate_distance(['se','sw','se','sw','sw']))

with open('.\day11.txt') as fp:
    coordinate_map = fp.read().strip().split(',')

print(calculate_distance(coordinate_map))