def solve():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        case_line = raw_input()
        result = solve_case(case_line)

        print 'Case #{}: {}'.format(i, result)


def solve_case(line):
    ab = line.split(" ")
    a = ab[0]
    b = ab[1]

    s_max = int(a)
    stand = int(b[0])

    friends = 0

    for i in range(1, s_max + 1):
        if i > stand:
            friends += (i - stand)
            stand += (i - stand)
        stand += int(b[i])

    return friends


solve()
