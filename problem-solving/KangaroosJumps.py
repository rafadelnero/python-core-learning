

def kangaroo_jump_match(k_location_1, k_jump_distance_1, k_location_2, k_jump_distance_2):
    max_jumps = 100000000
    for k_1, k_2 in zip(range(k_location_1, max_jumps, k_jump_distance_1),
                        range(k_location_2, max_jumps, k_jump_distance_2)):
        print("k1", k_1, "k2", k_2)
        if k_1 == k_2:
            return "YES"

    return "NO"


def kangaroo_jump_match_user_solution(k_location_1, k_jump_distance_1, k_location_2, k_jump_distance_2):
    if k_location_1 > k_location_2:
        remainder = (k_location_1 - k_location_2) % (k_jump_distance_1 - k_jump_distance_2)

        if remainder == 0:
            return "YES"

    return "NO"


if __name__ == '__main__':
    # result = kangaroo_jump_match(14, 4, 98, 2)
    # result = kangaroo_jump_match(0, 3, 4, 2)
    result = kangaroo_jump_match(4523, 8092, 9419, 8076)
    # result = kangaroo_jump_match(0, 2, 5, 3)
    print(result)
