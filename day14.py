from day10 import calculateKnotHash

used_memory_squares = 0
memory_map = []

for i in range(128):
    memory_map.append([])
    for c in calculateKnotHash("jzgqcdpd-{0}".format(i)):
        used_memory_squares += sum([int(bit) for bit in '{:0b}'.format(int(c, 16))])
    
        memory_map[i].extend([bit for bit in '{:04b}'.format(int(c, 16))])

# Part 1
print(used_memory_squares)

# Part 2
def followGroup(x,y):
    memory_map[x][y] = '_'

    right = min(x+1, 127)
    left = max(x-1, 0)
    up = max(y-1, 0)
    down = min(y+1, 127)

    if memory_map[left][y] == '1':
        followGroup(left,y)
    
    if memory_map[right][y] == '1':
        followGroup(right,y)

    if memory_map[x][up] == '1':
        followGroup(x,up)

    if memory_map[x][down] == '1':
        followGroup(x,down)

    return 1

group = 0
for x in range(len(memory_map)):
    for y in range(len(memory_map[x])):
        if memory_map[x][y] == '1':
            followGroup(x,y)
            group += 1

print(group)