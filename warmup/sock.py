import collections

'''
hackerrank


https://www.hackerrank.com/challenges/sock-merchant/problem
'''

def sockMerchant(n, ar):
    data = [y for x, y in collections.Counter(ar).items() if y > 1]
    total = 0
    for k in data:
        total += int(k / 2)
    
    return total


if __name__ == '__main__':
    number_sock = 9
    color_number = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    sockMerchant(number_sock, color_number)