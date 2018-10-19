import collections


def bird(params):

    value_data = collections.Counter(params).items()

    k = 0
    l = 0
    t = 0
    for data, y in value_data:
        
        
        if data > k and y > l:
            t = data
            
        
        k = data
        l = y

    print(t)

    return t



if __name__ == '__main__':
    case_proble  = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3 ,4]
    case_proble1 = [1, 4, 4, 4, 5, 3]
    bird(tes_case)