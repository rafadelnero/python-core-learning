
# Check if any work from s1 is contained in s2
def two_strings(s1, s2):
    for each_s1 in s1:
        if each_s1 in s2:
            return "Yes"

    return "No"


if __name__ == '__main__':
    print(two_strings("hello", "world"))
