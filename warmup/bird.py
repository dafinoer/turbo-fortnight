'''
hackerrank


https://www.hackerrank.com/challenges/migratory-birds/problem

'''

import collections


def bird(params):

    value_data = collections.Counter(params).items()

    id_bird = 0
    get_total_bird = 0
    type_bird = 0
    for data, total_bird in value_data:

        if data > id_bird and total_bird > get_total_bird:
            type_bird = data
        
        id_bird = data
        get_total_bird = total_bird

    print(type_bird)

    return type_bird



if __name__ == '__main__':
    # bird_type  = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3 ,4]
    bird_type = [1, 4, 4, 4, 5, 3]
    bird(bird_type)