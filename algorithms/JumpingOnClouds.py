def jumping_on_clouds(clouds: []):
    jump_count = 0
    i = 0
    clouds_quantity = len(clouds)

    while i < clouds_quantity - 1:
        if (i + 2) < clouds_quantity and clouds[i + 2] == 0:
            jump_count += 1
            i += 2
        elif (i + 1) < clouds_quantity and clouds[i + 1] == 0:
            jump_count += 1
            i += 1

    print(jump_count)


def jumping_on_clouds_recursive(c):
    if len(c) == 1: return 0
    if len(c) == 2: return 0 if c[1] == 1 else 1
    if c[2] == 1:
        return 1 + jumping_on_clouds_recursive(c[1:])
    if c[2] == 0:
        return 1 + jumping_on_clouds_recursive(c[2:])


if __name__ == '__main__':
    jumping_on_clouds([0, 1, 0, 0, 0, 1, 0])
