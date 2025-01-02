import Intcode
program = list(map(int, open("../Inputs/Advent_of_Code_05.txt").read()[:-1].split(",")))
save = program[:]

Intcode.run(program, 1)
Intcode.run(save, 5)
