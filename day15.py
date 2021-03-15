class Generator:
    def __init__(self, val, factor, multi=None) -> None:
        self.currentValue = val
        self.factor = factor
        self.divider = 2147483647
        self.check_if_multiple = multi
    def run(self):
        while(True):
            self.currentValue *= self.factor
            self.currentValue %= self.divider
            if not self.check_if_multiple:
                break
            if not (self.currentValue % self.check_if_multiple):
                break
    def __eq__(self, o: object) -> bool:
        return (self.currentValue & int('FFFF', 16)) == (o.currentValue & int('FFFF', 16))


def runGenerators(a,b, pairs):
    count = 0
    for i in range(pairs):
        a.run()
        b.run()
        if a == b:
            count += 1
    return count


# Part 1
a = Generator(591, 16807)
b = Generator(393, 48271)
# count = runGenerators(a,b, 40000000)
# print(count)

# Part 2
pairs = 5000000
a = Generator(591, 16807, 4)
b = Generator(393, 48271, 8)
count = runGenerators(a, b, 5000000)
print(count)