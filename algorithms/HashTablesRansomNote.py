# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through
# his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them
# to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must
# use only whole words available in the magazine. He cannot use substrings or concatenation to create the
# words he needs.
#
# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate
# his ransom note exactly using whole words from the magazine; otherwise, print No.
#
# Example
#  = "attack at dawn"  = "Attack at dawn"
#
# The magazine has all the right words, but there is a case mismatch. The answer is .
#
# Function Description
#
# Complete the checkMagazine function in the editor below. It must print  if the note
# can be formed using the magazine, or .
#
# checkMagazine has the following parameters:
#
# string magazine[m]: the words in the magazine
# string note[n]: the words in the ransom note
from collections import Counter, defaultdict


# This solution works but it's not optimal
def check_magazine(magazine, notes):
    for each_note in notes:
        if each_note in magazine:
            magazine.remove(each_note)
        else:
            return "No"

    return "Yes"


def ransom_note_user_solution(magazine, ransom):
    number = (Counter(ransom) - Counter(magazine)) == {}
    print(Counter(ransom) - Counter(magazine))

    return (Counter(ransom) - Counter(magazine)) == {}


## Defaultdict explanation
# How does it works
# As is a child class of standard dictionary, it can perform all the same functions.
#
# But in case of passing an unknown key it returns the default value instead of error. For ex:
#
# >>> d_int['a']
# 10
# >>> d_int['d']
# 0
# >>> d_int
# defaultdict(<type 'int'>, {'a': 10, 'c': 13, 'b': 12, 'd': 0})
def ransom_note_dicty_solution(magazine, ransom):
    dicty = defaultdict(int)

    for word in magazine:
        dicty[word] += 1
        # print(dicty)
    for word in ransom:

        if dicty[word] == 0:
            print(dicty)
            return False
        print(word, dicty[word])
        print(dicty["two"])
        dicty[word] -= 1
    return True


if __name__ == '__main__':
    magazine_param = "two times three is not four two".split()
    ransom_param = "two times two is four".split()
    print(ransom_note_dicty_solution(magazine_param, ransom_param))
    # print(ransom_note_user_solution("give me one grand today night", "give one grand today"))
