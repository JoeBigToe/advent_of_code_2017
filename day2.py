with open('.\day2.txt') as fp:
    input_var = fp.read().strip().splitlines()
    
def solve( spreadsheet ):
    rows = [ [ int(number) for number in line.split() ] for line in spreadsheet ]
    return sum( [ b-a for a, *_, b in map(sorted, rows) ] )


print(solve(input_var))