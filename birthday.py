'''
hacker rank

https://www.hackerrank.com/challenges/birthday-cake-candles/problem
'''


def birthdayCakeCandles(ar):
    
    max_data = max(ar)
    
    x = 0
    for i in ar:
        
        if i == max_data:
            x+= 1
    
    return x


if __name__ == '__main__':
    candle = [3, 2, 1, 3]
    birthdayCakeCandles(candle)
