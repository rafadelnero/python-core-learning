import re


def urlify(url: str) -> str:
    return re.sub(r"\s+", '%20', url)


def urlify_with_array(url_array: [str]) -> [str]:
    for i in range(len(url_array)):
        if ord(url_array[i]) == 32 and url_array[i - 1] != "%20":
            url_array[i] = "%20"
        elif url_array[i - 1] == "%20":
            url_array[i] = ""

    return url_array


def replace_spaces_book_solution(url_array: [str], true_length: int) -> [str]:
    space_count = 0
    for i in range(true_length):
        if url_array[i] == " ":
            space_count = space_count + 1

    index = true_length + space_count * 2
    if true_length < len(url_array):
        url_array[true_length] = '\0'

    for i in range(true_length - 1, -1, -1):
        if url_array[i] == " ":
            url_array[index - 1] = "0"
            url_array[index - 2] = "2"
            url_array[index - 3] = "%"
            index = index - 3
        else:
            url_array[index - 1] = url_array[i]
            index = index - 1

    return url_array


# O(N)
def urlify_algo(string, str_real_length):
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    char_list = list(string)
    reverse_index = len(char_list)

    for i in reversed(range(str_real_length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[reverse_index - 3: reverse_index] = "%20"
            reverse_index -= 3
        else:
            # Move characters
            char_list[reverse_index - 1] = char_list[i]
            reverse_index -= 1
    # convert back to string
    return "".join(char_list[reverse_index:])


def urlify_pythonic(text, length):
    """solution using standard library"""
    return text[:length].replace(" ", "%20")


if __name__ == '__main__':
    # print(urlify("testing    testing    "))
    # print(urlify_with_array(list("testing   testing")))

    print(urlify_algo("much ado about nothing      ", 22))
