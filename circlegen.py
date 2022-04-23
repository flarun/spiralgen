import math
import time


def printFirstHalf():
    distanceFromCircle = radius
    for distanceFromCircle in range(distanceFromCircle, 0, -1):
        if distanceFromCircle % 4 == 0:
            sectionToRender = ""

            match response_code:
                case 200:
                    print("Everything's peachy!")
    case 300:
        print("You're going somewhere else!")
    case 400:
        print("Uh oh. Are you lost?")
    case 500:
        print("Yikes. Something went wrong!")

        print(sectionToRender)


def printSecondHalf():
    # radius = diameter / 2
    # (radius) squared = (step or section of radius) squared + (half section or half chord) squared
    # (half section or half chord) = sqrt( (radius) squared - (step or section of raddius) squared )
    distanceFromCircle = radius
    for distanceFromCircle in range(radius):
        if distanceFromCircle % 4 == 0:
            sectionToRender = ""
            solidSection = int(
                math.sqrt(pow(radius, 2) - pow(distanceFromCircle, 2)))
            emptySection = int(diameter - solidSection)
            halfEmptySection = int(emptySection / 2)
            sectionToRender = halfEmptySection * " " + \
                solidSection * "0" + halfEmptySection * " "
            print(sectionToRender)
            time.sleep(0.05)


if __name__ == '__main__':
    inputIsValid = False
    while inputIsValid == False:
        diameter = int(input("Insert width of circle (must be even): "))
        if diameter % 2 == 0:
            inputIsValid = True
    radius = int(diameter / 2)
    rendering = True
    while rendering:
        printFirstHalf()
        printSecondHalf()
