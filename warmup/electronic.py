'''
hacker rank 

https://www.hackerrank.com/challenges/electronics-shop/problem
'''

def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards.sort(reverse=True)
    drives.sort()
    z = -1
    for k in keyboards:
        for d in drives:
            if k+d > b:
                break
            if k+d > z:
                z= k+d
    return z 

if __name__ == '__main__':
    keyboard = [3, 1]
    driver = [5, 2, 8]
    budget = 10
    getMoneySpent(keyboard, driver, budget)
