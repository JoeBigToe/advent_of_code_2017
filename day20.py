import re

def getDistance( p, v, a, i ):
    return sum([abs(p[el] + i*(v[el] + a[el]) + a[el]*((i-1)*i)/2) for el in range(3)])

def getLocationHashed( p, v, a, i):
    return '/'.join([str(int(p[el] + i*(v[el] + a[el]) + a[el]*((i-1)*i)/2)) for el in range(3)])

def parseLine(str):
    return [[int(i) for i in coord] for coord in [ re.sub(r'^.=<(.*)>',r'\1',param).split(',') for param in str.split(', ') ]]

vals = [ parseLine(line) for line in open('.\\advent_of_code_2017\\day20.txt').read().splitlines() ]

# Part 1
distances = [ getDistance(particle[0], particle[1], particle[2], 10000000) for particle in vals ]
print(distances.index(min(distances)))

# Part 2
for i in range(100):
    seen = {}
    remove = set()
    for p in range(len(vals)):
        point = getLocationHashed(vals[p][0], vals[p][1], vals[p][2], i)
        if point not in seen:
            seen.update({point: [vals[p]]})
        else:
            seen[point].append(vals[p])
            if point not in remove:
                remove.add(point)
    
    for key in remove:
        [vals.remove(value) for value in seen[key]]

print(len(vals))


