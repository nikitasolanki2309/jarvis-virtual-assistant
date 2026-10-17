import webbrowser

websites = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "facebook": "https://facebook.com",
    "linkedin": "https://linkedin.com",
    "github": "https://github.com",
    "amazon": "https://amazon.in",
    "spotify": "https://spotify.com"
}


def open_website(name):
    if name in websites:
        webbrowser.open(websites[name])
        return True

    return False

def search_google(query):
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)

def open_url(url):
    if not url.startswith("http"):
        url = "https://" + url

    webbrowser.open(url)