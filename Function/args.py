# def sum_all_nums(num1, num2, num3):
#     return num1 + num2 + num3

def sum_all_nums(*num):
    total = 0
    for i in num:
        total += i
    return total

print(sum_all_nums(3,2,4,1,2))    