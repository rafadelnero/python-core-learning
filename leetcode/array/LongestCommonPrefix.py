from typing import List


def longest_common_prefix(words: List[str]) -> str:
    results = {}
    letters = set()
    min_str_len = len(min(words, key=len))

    for index in range(min_str_len):
        str_to_compare = words[0][index]
        for word in words:
            if str_to_compare == word[index]:
                letters.add(word[index])
            else:
                return get_result_as_string(results)
        results[index] = letters.copy()
        letters.clear()

    return get_result_as_string(results)


def get_result_as_string(results: dict) -> str:
    str_result = ""
    for key in results:
        str_result += "".join(results[key])

    return str_result


if __name__ == '__main__':
    print(longest_common_prefix(["flower", "flow", "flight"]))
