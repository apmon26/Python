
def return_day(a):
    day = {1:"Sunday", 2:"Monday",3: "Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7: "Saturday"}
    day_of_week = day.get(a)
    if day_of_week:
        return day_of_week
    return "None"
print(return_day(10))   


#This function takes in one parameter (a list) and returns the last value in the list. It should return None if the list is empty.
def last_element(l):
    if l:
        return l[-1]
    return None    
    
print(last_element([1,2,3,42,12]))



#This function takes in two parameters (two strings). 
#The first parameter should be a word and the second should be a letter. 
# The function returns the number of times that letter appears in the word. 
# The function should be case insensitive (does not matter if the input is lowercase or uppercase). 
# If the letter is not found in the word, the function should return 0.  
def single_letter_count(string,letter):
    return string.lower().count(letter.lower())



def multiple_letter_count(string):
    return {letter : string.count(letter) for letter in string }

