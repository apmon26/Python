def find_odd(number):
    total = 0
    for num in number:
        if num % 2 == 1:
            total += num
    return total

print(find_odd([1,2,3,4,5,23,2,2,42,112,53]))        



#default parameters
def add(a,b):
    return a + b

def math(a,b, fn = add):
    return fn(a,b)

def subtract(a,b):
    return a - b

print(math(1,4))
print(math(2,1, subtract))

def speak(animal = "dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

print(speak("dog"))