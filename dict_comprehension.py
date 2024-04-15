# numbers = dict(first = 1, second = 2, third = 3)

# square_numbers = {key:value ** 2 for key, value in numbers.items()}

# print (square_numbers)


# str1 = "ABC"
# str2 = "123"
# combine = {str1[i] : str2[i] for i in range(0, len(str1))}

# print (combine)

#conditional logic with dictionary

number = range(10)
check = {num: ("even" if num % 2  == 0 else "odd") for num in number}
print(check)