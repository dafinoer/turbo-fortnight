'''
hackerrank solve

https://www.hackerrank.com/challenges/diagonal-difference/problem
'''

def diagonalDifference(arr):
    
    value_list =0
    
    phone = 0
    for data in arr:
        
        phone += data[value_list]
        
        value_list +=1
    
    dec = len(arr) - 1
    
    phtwo = 0
    
    for datak in arr:
        
        phtwo += datak[dec]
        
        dec -= 1
    
    tot = phtwo - phone
    
    return abs(tot)


if __name__ == '__main__':
    case_value =  [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    diagonalDifference(case_value)