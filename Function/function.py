
def return_day(a):
    day = {1:"Sunday", 2:"Monday",3: "Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7: "Saturday"}
    day_of_week = day.get(a)
    if day_of_week:
        return day_of_week
    return "None"
print(return_day(10))   