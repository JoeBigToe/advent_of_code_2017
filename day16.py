def dance(programs, instruction):
    if ( instruction[0] == 's' ):
        size = len(programs)-int(instruction[1:])
        return ( programs[size:] + programs[:size] )

    if ( instruction[0] == 'x' ):
        pos1, pos2 = [int(a) for a in instruction[1:].split('/')]
        programs[pos2], programs[pos1] = programs[pos1], programs[pos2]
        return programs

    if ( instruction[0] == 'p' ):
        char1, char2 = instruction[1:].split('/')
        pos1, pos2 = programs.index(char1), programs.index(char2)
        programs[pos2], programs[pos1] = programs[pos1], programs[pos2]
        return programs

programs = list("abcdefghijklmnop")
instructions = open('.\day16.txt').read().split(',')

configurations = []

while (True):
    for instruction in instructions:
        programs = dance(programs, instruction)

    key = ''.join(programs)
    if ( not (key in configurations) ):
        configurations.append(key)
    else:
        break


# Part 1
print(configurations[(1-1)%len(configurations)])

# Part 2
print(configurations[(1000000000-1)%len(configurations)])