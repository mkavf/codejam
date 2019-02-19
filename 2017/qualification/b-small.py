def solve():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        case_line = raw_input()
        result = solve_case(case_line)

        print 'Case #{}: {}'.format(i, result)


def solve_case(line):
    num = long(line)

    while True:
        if is_tidy(num):
            return num
        else:
            num = num - 1


def is_tidy(num):
    if num < 10:
        return True
    else:
        prev = None
        while num:
            num, d = divmod(num, 10)

            if prev is None:
                prev = d
            if prev < d:
                return False

            prev = d

        return True


solve()
