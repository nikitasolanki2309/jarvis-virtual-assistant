import webbrowser

music = {
    "levitating": "https://www.youtube.com/watch?v=TUVcZfQe-Kw&list=RDTUVcZfQe-Kw&start_radio=1",
    "dracula": "https://youtu.be/UvhkjVBBKiU?list=RDUvhkjVBBKiU",
    "criminal": "https://youtu.be/GmsmUswOBzQ?list=RDGmsmUswOBzQ"
}


def play_song(song):
    if song in music:
        webbrowser.open(music[song])
        return True

    return False