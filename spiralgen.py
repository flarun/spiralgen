import math
import time


def printO():
    # 2 cases : there is no inner void to render, there is an inner void to render
    # distanceFromCenter >= border, else
    distanceFromCenter = radius

    # Rendering first half of a O

    sections = []
    for distanceFromCenter in range(distanceFromCenter, 0, -1):
        if distanceFromCenter % 4 == 0:
            # Deciding wether or not there is an inner void section to render
            # if distanceFromCenter >= (radius - borderWidth):
            if distanceFromCenter >= (radius - borderWidth):
                sectionToRender = ""
                solidSection = int(
                    math.sqrt(pow(radius, 2) - pow(distanceFromCenter, 2)))
                emptySection = int(diameter - solidSection)
                halfEmptySection = int(emptySection / 2)
                sectionToRender = halfEmptySection * " " + \
                    solidSection * "0" + halfEmptySection * " "
                sections.append(sectionToRender)
            else:
                sectionToRender = ""
                # build the sections that make up the rendered sections
                emptySection = int(diameter - solidSection)
                halfEmptySection = int(emptySection / 2)
                solidSection = int(
                    math.sqrt(pow(radius, 2) - pow(distanceFromCenter, 2)))
                innerEmptySection = int(
                    math.sqrt(pow(radius - borderWidth, 2) - pow(distanceFromCenter, 2)))
                halfSolidSection = int((solidSection - innerEmptySection) / 2)
                sectionToRender = halfEmptySection * " " + halfSolidSection * "0" + \
                    innerEmptySection * " " + halfSolidSection * "0" + halfEmptySection * " "
                sections.append(sectionToRender)

    # Rendering second half of an O

    sections2 = []
    distanceFromCenter = radius

    for distanceFromCenter in range(0, distanceFromCenter, +1):
        if distanceFromCenter % 4 == 0:
            # Deciding wether or not there is an inner void section to render
            # if distanceFromCenter >= (radius - borderWidth):
            if distanceFromCenter < int(radius/3):
                # working where there are void parts in the
                if distanceFromCenter < int(radius*2/3):
                    sectionToRender = ""
                    # build the sections that make up the rendered sections
                    emptySection = int(diameter - solidSection)
                    halfEmptySection = int(emptySection / 2)
                    solidSection = int(
                        math.sqrt(pow(radius, 2) - pow(distanceFromCenter, 2)))
                    innerEmptySection = int(
                        math.sqrt(pow(radius - borderWidth, 2) - pow(distanceFromCenter, 2)))
                    halfSolidSection = int(
                        (solidSection - innerEmptySection) / 2)
                    sectionToRender = halfEmptySection * " " + halfSolidSection * "0" + \
                        innerEmptySection * " " + halfSolidSection * "0" + halfEmptySection * " "
                    sections2.append(sectionToRender)
                # working on the border
                if distanceFromCenter >= int(radius*2/3):
                    sectionToRender = ""
                    solidSection = int(
                        math.sqrt(pow(radius, 2) - pow(distanceFromCenter, 2)))
                    emptySection = int(diameter - solidSection)
                    halfEmptySection = int(emptySection / 2)
                    sectionToRender = halfEmptySection * " " + \
                        solidSection * "0" + halfEmptySection * " "
                    sections2.append(sectionToRender)
                    # to do: define the behaviour when the distance becomes greater than 1/3 radius

    # Shortening down the start of the first section and the end of the second one
    # so that the O's meet when printed

    # slash 8 because you are already printing just one line
    lengthToPop = int(borderWidth/8)
    # evry 4 lines, so to divide by 2 you have to do slash 8

    for i in range(lengthToPop):
        sections.pop(0)
        sections2.pop()

    # print sections iteratively
    for i in range(len(sections)):
        print(sections[i])
        time.sleep(0.05)

    for i in range(len(sections2)):
        print(sections2[i])
        time.sleep(0.05)


if __name__ == '__main__':
    inputIsValid = False
    while inputIsValid == False:
        diameter = int(input("Insert width of spiral (must be even): "))
        if diameter % 2 == 0:
            inputIsValid = True
    radius = int(diameter / 2)
    borderWidth = int(radius / 3)
    overlappingRadius = int(radius*4/3)
    overlappingDiameter = int(overlappingRadius*2)
    rendering = True
    while rendering:
        printO()
