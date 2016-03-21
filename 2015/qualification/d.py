import time


def main():
    with open('practice.in', 'r') as src:
        with open('practice.out', 'w') as dest:
            start_time = time.time()
            solve(src, dest)
            print("%s ms" % ((time.time() - start_time) * 1000))


def solve(src, dest):
    t = int(src.readline())
    for i in xrange(1, t + 1):
        line = src.readline()
        xrc = map(int, line.split(" "))

        result = solve_case(xrc[0], xrc[1], xrc[2])

        dest.write('Case #{}: {}\n'.format(i, result))


def solve_case(x, r, c):
    s = min(r, c)
    l = max(r, c)

    if (s * l) % x != 0:
        return 'RICHARD'
    if x == 3 and s == 1:
        return 'RICHARD'
    if x == 4 and s <= 2:
        return 'RICHARD'
    if x == 5 and (s <= 2 or (s, l) == (3, 5)):
        return 'RICHARD'
    if x == 6 and s <= 3:
        return 'RICHARD'
    if x >= 7:
        return 'RICHARD'

    return 'GABRIEL'

main()
