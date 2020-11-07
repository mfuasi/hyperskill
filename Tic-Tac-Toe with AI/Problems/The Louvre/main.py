class Painting:
    def __init__(self, title, painter, creation_year):
        self.title = title
        self.painter = painter
        self.creation_year = creation_year


tit = input()
artist = input()
year = int(input())

painting = Painting(tit, artist, year)

print(f'"{painting.title}" by {painting.painter} ({painting.creation_year}) hangs in the Louvre.')
