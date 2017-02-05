def solve():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        raw_input()  # read of d
        case_line = raw_input()
        plates = map(int, case_line.split(" "))
        result = solve_case(plates)

        print 'Case #{}: {}'.format(i, result)


def solve_case(plates):
    max_pancakes = max(plates)
    current_result = max_pancakes

    for x in xrange(1, max_pancakes):
        total_moves = 0

        for pancakes in plates:
            total_moves += (pancakes - 1) / x

        current_result = min(current_result, total_moves + x)

    return current_result

solve()
