class Gallery:

    def __init__(self):
        self.exhibitions = []

    def add_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)

    def __str__(self):
        output = "=" * 40 + "\n"
        output += f"The gallery has {len(self.exhibitions)} exhibitions.\n"
        output += "=" * 40 + "\n"
        for exhibition in self.exhibitions:
            output += f"Exhibition {self.exhibitions.index(exhibition)+1}\n{exhibition}\n"
        output += "=" * 40 + "\n"
        return output


class Exhibition:
    
    def __init__(self, start_date, end_date):
        self.art_pieces = []
        self.start_date = start_date
        self.end_date = end_date

    def add_art(self, art_piece):
        self.art_pieces.append(art_piece)

    def remove_art(self, art_piece):
        if len(self.art_pieces) > 0:
            self.art_pieces.remove(art_piece)

    def get_total_value(self):
        self.total_value = 0
        for art_piece in self.art_pieces:
            self.total_value += art_piece.initial_price
        return self.total_value

    def __str__(self):
        output = f"Dates: {self.start_date} to {self.end_date}\n"
        output += f"Total Value: £{self.get_total_value()}\n"
        output += "Exhibition Art Pieces:\n"
        for art_piece in self.art_pieces:
            output += f"{art_piece}\n"
        output += "=" * 40 + "\n"
        return output


class ArtPiece:
    
    def __init__(self, title, artist, initial_price):
        self.title = title
        self.artist = artist
        self.initial_price = initial_price

    def price_increase(self):
        self.initial_price = self.initial_price * 1.1

    def __str__(self):
        output = f"The {self.title} by {self.artist} has an initial price of £{self.initial_price}"
        return output


def test():
    art = ArtPiece('Mona Lisa', 'Leonardo DaVinci', 1000000)
    art2 = ArtPiece('Starry Night', 'Vincent Van Gogh', 50000)
    art3 = ArtPiece('Sunflow', 'Vincent Van Gogh', 50000)
    art4 = ArtPiece('The Scream', 'Edvar Munch', 750000)
    print(art)
    art.price_increase()
    print(art)

    exhibition = Exhibition('12/04/26','15/04/26')
    print(exhibition)
    exhibition.add_art(art)
    exhibition.add_art(art2)
    print(exhibition)
    exhibition2 = Exhibition('12/06/26','15/06/26')
    print(exhibition2)
    exhibition2.add_art(art3)
    exhibition2.add_art(art4)
    print(exhibition2)

    gallery = Gallery()
    print(gallery)
    gallery.add_exhibition(exhibition)
    gallery.add_exhibition(exhibition2)
    print(gallery)


test()