'''
hacker rank

https://www.hackerrank.com/challenges/time-conversion/problem
'''


def timeConversion(s):
    #
    # Write your code here.
    #
    value_date = s
    
    if value_date[-2:] == 'AM' and value_date[:2] == "12":
        return '00'+ value_date[2:-2]
    
    elif value_date[-2:] == "AM":
        return value_date[:-2]
    
    elif value_date[-2:] == 'PM' and value_date[:2] == '12':
        return value_date[:-2]
    
    else:
        value_date = str(int(value_date[:2]) + 12) + value_date[2:-2]
        
        return value_date

if __name__ == '__main__':
    input_case = '07:05:45PM'
    timeConversion(input_case)