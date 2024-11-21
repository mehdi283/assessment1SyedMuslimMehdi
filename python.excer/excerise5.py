daysinmonth = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

month = int(input("enter the number of month (1-12): "))

if month in daysinmonth : 
    print(f"the number of days in {month} is {daysinmonth[month]}") 


else:
    print("number is invalid please enter a valid number")

    