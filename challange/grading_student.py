'''
https://www.hackerrank.com/challenges/grading/problem
'''


def grade(params):

    lst_total = []

    for data in params:

        if data >= 38:
            grade = data / 5
            average_grade = (grade + 1) * 5
            total = average_grade - data

            if total < 3:
                lst_total.append(average_grade)
            elif total == 3:
                lst_total.append(data) 
        else:
            lst_total.append(data)

    return lst_total


if __name__ == '__main__':
    value_grade = [73, 67, 38, 33]
    print(grade(value_grade))

