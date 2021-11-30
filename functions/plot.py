import math
from math import sqrt
import matplotlib.pyplot as plt


def make_plot(home_c, coorList):
    graph_coordinates_y = [home_c[0]]
    graph_coordinates_x = [home_c[1]]

    for x, y in coorList.items():
        graph_coordinates_y.append(y[0])
        graph_coordinates_x.append(y[1])

    list_x = graph_coordinates_x
    list_y = graph_coordinates_y

    SortedDist = []

    for x in range(len(list_x)):
        dist = math.sqrt(((home_c[1]-list_x[x])**2) +
                         ((home_c[0]-list_y[x])**2))
        SortedDist.append([list_x[x], list_y[x], dist])

    sortedList = sorted(SortedDist, key=lambda x: x[2], reverse=False)

    newX = []
    newY = []
    for x in sortedList:
        newX.append(x[0])
        newY.append(x[1])
    print(coorList)
    print(newX)
    plt.plot(newX, newY,
             color='gray', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)
    for x, y in coorList.items():
        street = x.split(",", 1)
        street = street[0]
        plt.annotate(street, (y[1], y[0]))
    plt.annotate("Start", (home_c[1], home_c[0]))
    plt.xlabel('longitude')
    # naming the y axis
    plt.ylabel('latitude')

    # giving a title to graph
    plt.title('Route Graph')

    # function to show the plot
    plt.show()
