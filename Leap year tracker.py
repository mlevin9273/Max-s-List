#Max Levin
#Leap year tracker
#12/1/23

def tracker():
    x =int(input("enter the year"))
    if(x % 4 == 0):
        return("it is a leap year")
    if(x % 4 == 0) and (x % 100 == 0):
        return("it is not a leap year")
    if(x % 4 == 0) and (x % 100 == 0) and (x % 400 == 0):
        return("it is a leap year")
    else:
        return("it is not a leap year")
    
#main
print(tracker())
