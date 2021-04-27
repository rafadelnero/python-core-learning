

def minimum_bribes(queue):
    bribes = 0

    for i in range(len(queue) - 1, -1, -1):
        if queue[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, queue[i] - 2), i):
            print(queue[i])
            if queue[j] > queue[i]:

                bribes += 1
                if queue[i] == 4:
                    print(bribes)

    print(bribes)


if __name__ == '__main__':
    minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4])

