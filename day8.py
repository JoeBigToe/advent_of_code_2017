def solve():
    with open('.\day8.txt') as fp:
        input_var = fp.read().strip().splitlines()

    registers = {}
    register_values_snapshot = []

    for line in input_var:
        operation, evaluation = line.split(' if ')
        
        register1, op, op_value = operation.split()
        register2, ev, ev_value = evaluation.split()

        if not (register1 in registers.keys()):
            registers.update({register1 : 0})

        if not (register2 in registers.keys()):
            registers.update({register2 : 0})

        # print('registers[{0}] {1} {2}'.format(register2, ev, ev_value))
        if eval('registers["{0}"] {1} {2}'.format(register2, ev, ev_value)):
            if op == 'inc':
                registers[register1] += int(op_value)
            if op == 'dec':
                registers[register1] -= int(op_value)
        
        register_values_snapshot.append(max(registers.values()))

    return max(register_values_snapshot)

print(solve())

