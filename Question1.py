month=int(input("Please enter the month in numeric form"))
day=int(input("Please enter the day in numeric form"))
year=int(input("Please enter the year in two numeric digits"))





if (month>12 or month<1):
    print("Invalid month")
    
if (day>31):
    print("Invalid day")
    if(month==2 and day>28):
        print("Invalid day")
        if(year%4==0 and day!=29):
            print("Invalid day")
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 and day!=31):
        print("Invalid day")
    if(month==4 or month==6 or month==9 or month==11 and day!=30):
        print("Invalid day")

if (year>99):
    print("Invalid year")

else:
    print(month,"/",day,"/",year,"Success: Congratulations! You entered a correct date")




    


