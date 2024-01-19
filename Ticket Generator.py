#Name: Daniel Dwyer and Max Levin
#Date: 11/7/23

#Initialize
import turtle
t = turtle.Turtle()

#Functions

#Draws a text box with a label. This function uses a turtle to draw a text box with a label next to it.
#Parameters:
#(string: label) label is the word that appears next to the text box
#(integer: y_location) y_location represents the vertical loction of the text box
def draw_textbox(label, y_location):
    t.goto(-50, y_location)
    t.write(label, font=("Arial", 15, "bold"), align="right")
    t.pendown()
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(25)
        t.left(90)
    t.penup()
    t.goto(-40, y_location + 5)


#Draws a text box with a label. This function uses a turtle to draw a small text box with a label. The size of the text box is perfect for Y or N questions.
#Parameters:
#(string: label) label is the word that appears next to the text box
#(integer: y_location) y_location represents the vertical loction of the text box  
def draw_small_textbox(label, y_location):
    t.goto(60, y_location)
    t.write(label, font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(50)
        t.left(90)
        t.forward(25)
        t.left(90)
    t.penup()
    t.goto(80, y_location + 5)


#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(string: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket  

#Functions
def draw_ticket(name, price, dayofweek, y_location):
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(250)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.penup()
    t.goto(50, y_location +75)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(200, y_location +75)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(100, y_location +35)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(100, y_location +5)
    t.write(price, font=("Arial", 15), align="right")

#Main
def ticketgenerator():
    t.penup()
    t.goto(-400,400)
    t.pendown()
    t.penup()
    t.write("Field Museum", align="left", font=("Arial", 20, "normal"))

#Things that will be printed on the ticket
    name = input("What is your name?")  
    age = int(input("How old are you?"))
    dayofweek = input("What day of the week is it?")
    couponcode = input("enter any special coupon code here.")
    price = 30

#Determines the price of the ticket

    if (age <= 3):
        price = 0
    if ((age <= 18) and (couponcode == "SUNDAY10") and dayofweek == ("sunday")):
        price = 20
    elif ((age <= 18) and dayofweek != ("saturday" or "sunday")):
        price = 15
    if ((age <= 18) and (couponcode == "FREEFRIDAY") and dayofweek == ("friday")):
        price = 0
    elif ((age <= 18) and dayofweek != ("saturday" or "sunday")):
        price = 15  

#Locations for the text boxes

    t.penup()
    draw_textbox("Name", 300)
    draw_textbox("Age", 200)
    draw_textbox("Day", 100)
    draw_textbox("Couponcode", 0)

    t.penup()
    t.goto(20,300)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(0,200)
    t.write(age, font=("Arial", 15), align="right")
    t.goto(30,100)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(80,0)
    t.write(couponcode, font=("Arial", 15), align="right")

    draw_ticket(name, price, dayofweek, -200)
    turtle.done()

#Main
ticketgenerator()