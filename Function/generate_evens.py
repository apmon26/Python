def generate_evens():
    return [ x for x in range(1,50) if x%2 == 0]

#Define a function called generate_evens
def generate_evens():
    result = []
    for i in range(1,50):
        if i % 2 == 0:
            result.append(i)
    return result    
            
#It should return a list of even numbers between 1 and 50(not including 50)
print(generate_evens())


def find_odd():
    return[x for x in range(1,20) if x%2 == 1]
print(find_odd())