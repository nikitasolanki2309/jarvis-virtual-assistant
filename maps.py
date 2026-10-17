import webbrowser


def search_maps(query):
    url = "https://www.google.com/maps/search/" + query.replace(" ", "+")
    webbrowser.open(url)