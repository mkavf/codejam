def solve():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        case_line = raw_input()
        result = solve_case(case_line)

        print 'Case #{}: {}'.format(i, result)


def solve_case(line):
    pancakes, size = line.split(' ')
    size = int(size)
    pancakes = list(pancakes)

    result = 0
    while True:
        index = first_index(pancakes)

        if index == -1:
            return result

        if index + size > len(pancakes):
            return "IMPOSSIBLE"

        for i in xrange(index, index + size):
            if pancakes[i] == '+':
                pancakes[i] = '-'
            else:
                pancakes[i] = '+'

        result += 1


def first_index(collection):
    for i in xrange(0, len(collection)):
        if collection[i] == '-':
            return i

    return -1


solve()
