class music:
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return f'Performer: {self.artist}\n Title: {self.title}\n Album: {self.album}\n Year: {self.year}'

my_music = music('Ed Sheeran',"Hearts Don't Break Around Here",'Divide', 2017)

print(my_music)