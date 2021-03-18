# Count the valleys from the hiker

# Sample Input
# 8
# UDDDUDUU
# Sample Output
# 1

# Explanation
# If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:
#
# _/\      _
#    \    /
#     \/\/

def counting_valleys(steps, path):
    up_down_step = count_valleys = 0

    for each_step in path:
        print(each_step)

        if each_step == "U":
            up_down_step += 1
        else:
            up_down_step -= 1

        if each_step == 'U' and up_down_step == 0:
            count_valleys += 1

    print(count_valleys)


if __name__ == '__main__':
    counting_valleys(8, "DDUUDDUDUUUD")
