import re 

global letters, matrix

def getDirection(location, direction):
    if direction in ["down", "up"]:
        if matrix[location[0]][location[1]-1] != " ":
            return "left"
        if matrix[location[0]][location[1]+1] != " ":
            return "right"
    if direction in ["left", "right"]:
        if matrix[location[0]-1][location[1]] != " ":
            return "up"
        if matrix[location[0]+1][location[1]] != " ":
            return "down"
    
    return None

def getIncs(direction):
    if direction == "down":
        return [1,0]
    if direction == "up":
        return [-1,0]
    if direction == "left":
        return [0,-1]
    if direction == "right":
        return [0,1]

def isMatrixEdge(location):
    if location[0] * location[1] < 0:
        return True
    if location[1] >= len(matrix[location[0]]):
        return True
    if location[0] >= len(matrix):
        return True

letters = []
matrix = [list(line) for line in open('.\\advent_of_code_2017\\day19.txt').read().splitlines()]
location = (0, matrix[0].index('|'))
direction = "down"
incs = [1,0]
steps = 1

while True:
    
    location = [location[a] + incs[a] for a in range(2)]
    
    if isMatrixEdge(location):
        break
    char = matrix[location[0]][location[1]]

    if char == ' ':
        break
    letters.append(''.join(re.findall("\w", char)))
    
    steps += 1
    if char == "+":
        direction = getDirection(location, direction)
        if direction == None:
            break
        incs = getIncs(direction)
    
        
# Part 1
print(''.join(letters))    

# Part 2
print(steps)
