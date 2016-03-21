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
        lx_line = src.readline()
        lx = map(int, lx_line.split(" "))

        seq = src.readline().strip()
        result = solve_case(lx[0], lx[1], seq)

        dest.write('Case #{}: {}\n'.format(i, result))

TABLE = {
    '1': {'1': '1', 'i': 'i',  'j': 'j',  'k': 'k'},
    'i': {'1': 'i', 'i': '-1', 'j': 'k',  'k': '-j'},
    'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
    'k': {'1': 'k', 'i': 'j',  'j': '-i', 'k': '-1'}
}


def solve_case(l, x, seq):
    if multiply_all(x, seq) == '-1':
        if shortest_ij(l, x, seq):
            return 'Yes'

    return 'No'


def shortest_ij(l, x, seq):
    i, found = reduce_to(0, 'i', l, x, seq)

    if found:
        j, found = reduce_to(i, 'j', l, x, seq)

    return found


def reduce_to(start, char, l, x, seq):
    idx = start
    a = seq[start % l]
    length = l * x

    while idx < length:
        idx += 1
        if a == char:
            return idx, True
        a = multiply(a, seq[idx % l])

    return idx, False


def multiply_all(x, seq):
    a = reduce(multiply, seq[1:], seq[0])

    x %= 4

    if x == 0:
        return '1'
    if x == 1:
        return a
    if x == 2:
        return multiply(a, a)
    if x == 3:
        return multiply(multiply(a, a), a)


def multiply(x, y):
    negative = False

    if '-' in x:
        negative ^= True
        x = x[1]

    if '-' in y:
        negative ^= True
        y = y[1]

    z = TABLE[x][y]

    if negative:
        if '-' in z:
            return z[1]
        else:
            return '-' + z

    return z


main()
