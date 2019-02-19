def solve():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        case_line = raw_input()
        result = solve_case(case_line)

        print 'Case #{}: {}'.format(i, result)


def solve_case(num):
    result = []

    i = 0
    a = int(num[i])

    can_correct = True
    while i < len(num) - 1:
        b = int(num[i + 1])

        if a > b:
            b = 9
            if can_correct:
                a -= 1
                can_correct = False
                if len(result) > 0 and a < result[i - 1]:
                    result[i - 1] -= 1
                    a = 9
                    correct_result(i - 1, result)

        if a != 0:
            result.append(a)

        i += 1
        a = b

    result.append(a)

    return int(reduce(lambda x, y: str(x) + str(y), result))


def correct_result(index, result):
    if index > 0:
        if result[index] < result[index - 1]:
            result[index - 1] -= 1
            result[index] = 9
            correct_result(index - 1, result)


solve()
