'''
hacker rank

https://www.hackerrank.com/challenges/staircase/problem
'''

def staircase(n):
    value = 0
    for data in range(n, -1, -1):
        value += 1
        for k in range(data):
            print(' ', end='')
        
        if value <= n:
            for j in range(0, value):
                print('#', end='')
        else:
            break

        print('')           
        # print(value)

    return params


if __name__ == '__main__':
    input_case = 6
    staircase(input_case)