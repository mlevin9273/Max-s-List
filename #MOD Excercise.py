#Max Levin
#Leap year tracker
#12/1/23

def tracker():
    input("enter the year")
    if(input % 4 == 0):
        return("it is a leap year")
    if(input % 4 == 0) and (input % 100 == 0):
        return("it is not leap year")
    if(input % 4 == 0) and (input % 100 == 0) and (input % 400 == 0):
        return("it is a leap year")
    else:
        return("it is not a leap year")



