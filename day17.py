global step

def spin( state, current_position, i ):
    gap = (current_position + step) % len(state) + 1
    return state[:gap] + [i+1] + state[gap:], gap

# Part 1
state = [0]
current_position = 0
step = 303
for i in range(2017):
    state, current_position = spin( state, current_position, i )

print(state[current_position+1])

# Part 2
size = 1
gap = 0
for i in range(50000000):
    gap = (gap + step) % size + 1
    if gap == 1:
        val = i + 1
    size += 1

print(val)