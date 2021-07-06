

def count_and_say(n: int) -> str:
    numbers_mapping = {1: "1", 2: "11", 3: "21", 4: "1211", 5: "111221"}
    result = "1"
    while n > 1:
        current_str = ""
        i = 0
        while i < len(result):
            i += 1
            count = 1
            while i + 1 < len(result) and result[i] == result[i + 1]:
                count += 1
                i += 1
            current_str += str(count) + str(result[i])

        result = current_str
        n -= 1
    return result


if __name__ == '__main__':
    print(count_and_say(4))
