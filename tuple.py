#x = (1,2,3)
#x[0] = 2 #TypeError: 'tuple' object does not support item assignment

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

i = len(months) - 1
while (i >= 0):
    print(months[i])
    i -= 1