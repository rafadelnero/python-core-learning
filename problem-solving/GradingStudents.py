from math import ceil


# if the number is greater or equal to 40
# Check if the number is less than 3 of a difference to the the next multiple value of 5
def grading_students(grades):
    for i in range(len(grades)):
        next_multiple_5 = (5 * ceil(grades[i] / 5))
        if next_multiple_5 >= 40 and next_multiple_5 - grades[i] < 3:
            grades[i] = next_multiple_5

    return grades


if __name__ == '__main__':
    result = grading_students([4, 73, 67, 38, 33])
    print(result)
