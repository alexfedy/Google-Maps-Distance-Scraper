def _home_url(home_url):
    url = home_url.split("/")[5:]
    url = url[1].replace("@", "")
    url = url.split(",")
    url.pop()
    lat = float(url[0])
    long = float(url[1])
    home = []
    home.append(lat)
    home.append(long)
    return home
