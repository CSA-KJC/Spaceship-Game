Name=" "
planet="earth"
newplanet="earth"
points=0
oldplanet=" "

def start():
    global Name
    print("Welcome to the Spaceship Game!  Your goal is to travel to different planets without blowing up. You will earn 100 points every time you make it to a planet.")
    Name=input("What is your name? ")
    menu()
    
def menu():
    global Name
    global planet
    global oldplanet
    global points
    print("Hi "+Name)
    print("You have "+str(points)+" points right now")
    print("1. Start Game\n2. Enter Planet Code")
    choose=input("Choice: ")
    if choose=="1":
        fly()
    elif choose=="2":
        oldplanet=input("Which planet were you on? ").lower()
        planet=oldplanet
        fly()
    else:
        print("Type in 1 or 2 to start the game")
        menu()

def fly():
    global planet
    global speed
    global newplanet

    while True:
        try:
            weight=float(input("How much does your spaceship weigh? "))
            break
        except ValueError:
            print("That is not a valid number.  Try again...")
    
    newplanet=input("Which planet are you flying to? ").lower()
    if newplanet==planet:
        print("You are already on planet "+newplanet.title()+". Try again")
        fly()
    elif newplanet=="earth" or newplanet=="venus" or newplanet=="mercury" or newplanet=="mars" or newplanet=="jupiter" or newplanet=="saturn" or newplanet=="uranus" or newplanet=="neptune":
        speed=float(input("How fast (km/s) do you want to go? "))
        escape_planet()
    else:
        print("That is not a planet. Try again")
        fly()
         
def escape_planet():
    global planet
    global speed
    global newplanet
    if planet=="earth":
        if speed>=11.186 and speed<=15:
            new_planet()
        elif speed>15:
            print("You went too fast and crashed! Try again")
            fly()
        elif speed<11.186:
            print("You went too slow and crashed! Try again")
            fly()
        else:
            print("That is not a number")
            fly()
    elif planet=="mercury":
        if speed>=4.25 and speed<=6:
            new_planet()
        elif speed>6:
            print("You went too fast and crashed! Try again")
            fly()
        elif speed<4.25:
            print("You went too slow and crashed! Try again")
            gly()
        else:
            print("That is not a number")
            fly()
    elif planet=="venus":
        if speed>=10.36 and speed<=14:
            new_planet()
        elif speed>14:
            print("You went too fast and crashed! Try again")
            fly()
        elif speed<10.36:
            print("You went too slow and crashed! Try again")
            fly()
        else:
            print("That is not a number")
            fly()
    elif planet=="mars":
        if speed>=5.02 and speed<=8:
            new_planet()
        elif speed<5.02:
            print("You went too slow and crashed! Try again")
            fly()
        elif speed>8:
            print("You went too fast and crashed! Try again")
            fly()
        else:
            print("That is not a number")
            fly()
    elif planet=="jupiter":
        if speed>=59.54 and speed<=63:
            new_planet()
        elif speed<59.54:
            print("You went too slow and crashed! Try again")
            fly()
        elif speed>63:
            print("You went too fast and crashed! Try again")
            fly()
        else:
            print("That is not a number")
    elif planet=="saturn":
        if speed>=35.49 and speed<=39:
            new_planet()
        elif speed<35.49:
            print("You went too slow and crashed! Try again")
            fly()
        elif speed>39:
            print("You went too fast and crashed! Try again")
            fly()
        else:
            print("That is not a number")
            fly()
    elif planet=="uranus":
        if speed>=21.29 and speed<=25:
            new_planet()
        elif speed<21.29:
            print("You went too slow and crashed! Try again")
            fly()
        elif speed>25:
            print("Youoldplanet went too fast and crashed! Try again")
            fly()
        else:
            print("That is not a number")
            fly()
    elif planet=="neptune":
        if speed>=23.71 and speed<=28:
            new_planet()
        elif speed<23.71:
            print("You went too slow and crashed! Try again")
            fly()
        elif speed>28:
            print("You went too fast and crashed! Try again")
            fly()
        else:
            print("That is not a number")
            fly()
    else:
        print("That is not a planet. Try again")
        menu()

def new_planet():
    global planet
    global newplanet
    global oldplanet
    global points
    planet=newplanet
    if oldplanet=="venus" or oldplanet=="mercury" or oldplanet=="mars" or oldplanet=="jupiter" or oldplanet=="saturn" or oldplanet=="uranus" or oldplanet=="neptune":
        print("You are on planet "+oldplanet.title())
        fly()
    elif newplanet=="venus" or newplanet=="mercury" or newplanet=="mars" or newplanet=="jupiter" or newplanet=="saturn" or newplanet=="uranus" or newplanet=="neptune":
        print("Congratulations! You have made it to "+newplanet.title())
        print("You have earned 100 points")
        points=points+100
        print("Your total is "+str(points))
        leave=input("Would you like to quit? ").lower()
        if leave=="yes":
            print("Trying to exit")
            exit()
        elif leave=="no":
            fly()
        else:
            print("Please put a valid answer")
            new_planet()
    elif planet==newplanet:
        print("You are already on planet "+planet.title()+". Choose a different planet")
        fly()
    else:
        print("That is not a planet.  Try again")
        fly()
    
start()



#Katie Chiu
#Computer Programming 12th
#October 12, 2017
