instructor2 = "Colt"
def say_hello():
   instructor1 = "James"
   return f"Hello {instructor1}"
   
say_hello()
   
#print(instructor1) #nameError   
print(instructor2) #Colt


def outer():
   count = 0
   def inner():
      nonlocal count
      count += 1 
      return count
   return inner()


def add(a,b):
   """ this function is additional """
   return a + b

print(add.__doc__)