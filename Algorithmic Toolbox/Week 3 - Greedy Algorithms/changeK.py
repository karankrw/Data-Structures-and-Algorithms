# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def get_change(value):
    one, five, ten = 1, 5, 10
    count = 0
    
    while value > 0:
        if value >= ten:
            count += value // ten
            value %= ten
            
        elif value >= five:
            count += value // five
            value %= five
            
        else:
            count += value // one
            break
        
    return count



if __name__ == '__main__':
    
    money = int(input())
    print(get_change(money))