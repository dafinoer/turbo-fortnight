'''
hacker rank 

https://www.hackerrank.com/challenges/electronics-shop/problem
'''

def get_Money_Spent(keyboards, drives, budget):
    #get
    # Write your code here.
    #
    list_data = []
    for data in drives:
        for k in keyboards:
            total = data + k
            if total <= b:
                list_data.append(total)
            else:
                list_data.append(-1)
                
    
    max_data = max(list_data)
    
    return max_data

if __name__ == '__main__':
    keyboard = [3, 1]
    driver = [5, 2, 8]
    budget = 10
  print(get_Money_Spent(keyboard, driver, budget))
