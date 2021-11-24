import matplotlib.pyplot as plt


def make_plot(home_c, coorList):
    graph_coordinates_y = [home_c[0]]
    graph_coordinates_x = [home_c[1]]

    for x, y in coorList.items():
        graph_coordinates_y.append(y[0])
        graph_coordinates_x.append(y[1])

    plt.plot(graph_coordinates_x, graph_coordinates_y, color='green', linestyle='dashed', linewidth=3,
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
