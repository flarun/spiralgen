import math
import time


def printO():
    # 2 cases : there is no inner void to render, there is an inner void to render
    # distanceFromCenter >= border, else
    distanceFromCenter = radius
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
    # print sections iteratively
    for i in range(len(sections)):
        print(sections[i])
        time.sleep(0.05)

    sections2 = []
    distanceFromCenter = radius

    for distanceFromCenter in range(0, distanceFromCenter, +1):
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
                sections2.append(sectionToRender)
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
                sections2.append(sectionToRender)
    # print sections iteratively
    for i in range(len(sections2)):
        print(sections2[i])
        time.sleep(0.05)


if __name__ == '__main__':
    inputIsValid = False
    while inputIsValid == False:
        diameter = int(input("Insert width of = (must be even): "))
        if diameter % 2 == 0:
            inputIsValid = True
    radius = int(diameter / 2)
    borderWidth = int(radius / 3)
    rendering = True
    while rendering:
        printO()
