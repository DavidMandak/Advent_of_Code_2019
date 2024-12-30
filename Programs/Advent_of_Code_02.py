program = list(map(int, open("../Inputs/Advent_of_Code_02.txt").read()[:-1].split(",")))
program[1], program[2] = 12, 2
save = program[:]


def run(inp):
    pos = 0
    while inp[pos] != 99:
        opcode, add1, add2, add3 = inp[pos:pos+4]
        if opcode == 1:
            inp[add3] = inp[add1]+inp[add2]
        else:
            inp[add3] = inp[add1]*inp[add2]
        pos += 4
    return inp[0]


print(run(program[:]))
for noun in range(99):
    for verb in range(99):
        program[1], program[2] = noun, verb
        if run(program[:]) == 19690720:
            print(100*noun+verb)
