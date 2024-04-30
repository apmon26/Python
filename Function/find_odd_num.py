def find_odd(number):
    total = 0
    for num in number:
        if num % 2 == 1:
            total += num
    return total

print(find_odd([1,2,3,4,5,23,2,2,42,112,53]))        
