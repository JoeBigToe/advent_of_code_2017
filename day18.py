import re

class ProgramPart1():

    def __init__(self, instructions):
        self.pointer = 0
        self.completed = False
        self.last_played_sound = 0
        self.registers = {}
        self.instructions = instructions

    def run(self):
        instruction = self.instructions[self.pointer][:3]
        arguments = self.instructions[self.pointer][4:]

        if (instruction not in ["snd", "rcv"]):
            register, value = arguments.split()
            try:
                value = int(value)
            except:
                value = self.registers[value]

            if register not in self.registers.keys():
                self.registers.update({ register: 0 })

        if instruction == "snd":
            self.last_played_sound = self.registers[arguments]
        if instruction == "rcv":
            if not ( self.registers[arguments] == 0 ):
                print(self.last_played_sound)
                self.registers[arguments] = self.last_played_sound
                self.completed = True
        if instruction == "set":
            self.registers[register] = value
        if instruction == "add":
            self.registers[register] += value
        if instruction == "mul":
            self.registers[register] *= value
        if instruction == "mod":
            self.registers[register] %= value
        if instruction == "jgz":
            if self.registers[register] > 0:
                self.pointer += value
                return

        self.pointer += 1
        if ( self.pointer >= len(self.instructions) ):
            self.completed = True

        return

class ProgramPart2():

    def __init__(self, instructions, programId):
        self.pointer = 0
        self.registers = {"p":programId}
        self.instructions = instructions
        self.queue = []
        self.locked = False
        self.values_sent = 0

    def run(self, parallelProgram):
        self.locked = False
        instruction = self.instructions[self.pointer][:3]
        arguments = self.instructions[self.pointer][4:]
        parsed = arguments.split()
        register = parsed[0]
        value = parsed[1] if len(parsed) > 1 else None
        if value:
            try:
                value = int(value)
            except:
                value = self.registers[value]
        if (not re.match("\d", register)) and (register not in self.registers.keys()):
            self.registers.update({ register: 0 })

        if instruction == "snd":
            register = int(register) if re.match("\d", register) else self.registers[register]
            parallelProgram.queue.append(register)
            self.values_sent += 1
        if instruction == "rcv":
            if len(self.queue) == 0:
                self.locked = True
                return
            self.registers[arguments] = self.queue.pop(0)
        if instruction == "set":
            self.registers[register] = value
        if instruction == "add":
            self.registers[register] += value
        if instruction == "mul":
            self.registers[register] *= value
        if instruction == "mod":
            self.registers[register] %= value
        if instruction == "jgz":
            register = int(register) if re.match("\d", register) else self.registers[register]
            if register > 0:
                self.pointer += value
                return

        self.pointer += 1

        return

instructions = open('.\\advent_of_code_2017\\day18.txt').read().splitlines()

# Part 1
program = ProgramPart1(instructions)
while not program.completed:
    program.run()

# Part 2
p1 = ProgramPart2(instructions, 0)
p2 = ProgramPart2(instructions, 1)
while not ( p1.locked and p2.locked ):
    p1.run(p2)
    p2.run(p1)

print(p2.values_sent)