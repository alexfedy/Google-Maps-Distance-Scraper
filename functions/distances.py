from math import sin, cos, sqrt, atan2, radians


def _distances_(home, coordinates):
    for x, y in coordinates.items():
        vals = []
        vals.append(y[0])
        vals.append(y[1])
        # print(vals)

        # approximate radius of earth in miles using the Haversine distance.
        R = 6373.0

        lat1 = radians(home[0])
        lon1 = radians(home[1])
        lat2 = radians(vals[0])
        lon2 = radians(vals[1])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        distance = distance/1.609

        # print("Result:", distance)
        coordinates[x] = distance

    sort_distance_ascending = sorted(
        coordinates.items(), key=lambda x: x[1])
    sort_distance_descending = sorted(
        coordinates.items(), key=lambda x: x[1], reverse=True)

    # print("Sorted Ascending: ", sort_distance_ascending)
    # print("Sorted Descending: ", sort_distance_descending)

    order = []

    for item in sort_distance_descending:
        order = order + [item[0], " ----- Distance: ",
                         str(round(item[1], 3)), " miles", "\n"]
    file = open("finalOutput.txt", "w")
    file.close()
    with open('finalOutput.txt', 'w') as filehandle:
        for listitem in order:
            filehandle.write('%s' % listitem)
