def main():
    with open('practice.in', 'r') as src:
        with open('practice.out', 'w') as dest:
            solve(src, dest)


def solve(src, dest):
    t = int(src.readline())
    for i in xrange(1, t + 1):
        src.readline()  # read of d
        case_line = src.readline()
        plates = map(int, case_line.split(" "))
        result = solve_case(plates)

        dest.write('Case #{}: {}\n'.format(i, result))


def solve_case(plates):
    max_pancakes = max(plates)
    current_result = max_pancakes

    for x in xrange(1, max_pancakes):
        total_moves = 0

        for pancakes in plates:
            total_moves += (pancakes - 1) / x

        current_result = min(current_result, total_moves + x)

    return current_result

main()
