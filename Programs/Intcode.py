def run(program, inp=None):
    pos = 0
    while pos < len(program):
        modes, opcode = setup(program[pos])
        match opcode:
            case 1:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                c = program[pos+3]
                program[c] = a+b
                pos += 4
            case 2:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                c = program[pos+3]
                program[c] = a*b
                pos += 4
            case 3:
                c = program[pos+1]
                program[c] = inp
                pos += 2
            case 4:
                a = get(program, pos+1, modes[0])
                print(a)
                pos += 2
            case 5:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                if a:
                    pos = b
                else:
                    pos += 3
            case 6:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                if not a:
                    pos = b
                else:
                    pos += 3
            case 7:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                c = program[pos+3]
                program[c] = 1 if a < b else 0
                pos += 4
            case 8:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                c = program[pos+3]
                program[c] = 1 if a == b else 0
                pos += 4
            case 99:
                return program


def setup(instr):
    op = instr % 100
    mod = []
    instr = str(instr)
    length = len(instr)
    for i in range(-3, -5, -1):
        if -i > length:
            mod.append(0)
        else:
            mod.append(int(instr[i]))
    return mod, op


def get(program, pos, mode):
    parameter = program[pos]
    match mode:
        case 0:
            return program[parameter]
        case 1:
            return parameter
    exit("Invalid mode")
