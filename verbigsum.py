

'''
hacker rank solve

https://www.hackerrank.com/challenges/a-very-big-sum/problem
'''

def aVeryBigSum(ar):
    
    get_you = 0
    for data in ar:
        get_you += data
        
    return get_you


if __name__ == '__main__':
    list_data = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    aVeryBigSum(list_data)