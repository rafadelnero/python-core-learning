

def get_total_of_factors_for_a_b(a, b):
    multiples_a = []

    total_matched_factors = 0

    lcm = a[0]

    # for i in a:
    #     lcm =

    for each_a in a:
        for i in range(1, 100):
            if i % each_a == 0:
                multiples_a.append(i)

    multiples_a = set(multiples_a)

    for each_b in b:
        for each_a in multiples_a:
            if each_b % each_a == 0:
                total_matched_factors += 1

    return total_matched_factors


def get_lcm(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    else:
      gcd = get_gcd(n1, n2)
    return abs(n1 * n2) / gcd


def get_gcd(n1, n2):
    if n2 == 0:
        return n1

    return get_gcd(n2, n1 % n2)


if __name__ == '__main__':
    result = get_total_of_factors_for_a_b([2, 4], [16, 32, 96])
    print(result)
