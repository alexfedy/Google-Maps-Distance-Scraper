def _url_dissection(urls):
    All_Coordinates = {}
    for url in urls:
        url = url.split("/")[5:]
        Addy = url[0].replace("+", " ")
        url = url[1].replace("@", "")
        url = url.split(',')
        url.pop()
        lat = float(url[0])
        long = float(url[1])
        coordinates = []
        coordinates.append(lat)
        coordinates.append(long)
        All_Coordinates[Addy] = coordinates
    return All_Coordinates
