def solve():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        result = solve_case()

        print 'Case #{}: {}'.format(i, result)


def solve_case():
    engines = set({})
    queries = set({})

    s = int(raw_input())
    for i in range(s):
        engines.add(raw_input())

    count = 0

    q = int(raw_input())
    for j in range(q):
        query = raw_input()
        queries.add(query)

        if len(engines) == len(queries):
            count += 1
            queries.clear()
            queries.add(query)

    return count


solve()
