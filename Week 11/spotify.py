class Song:

    def __init__(self, title, artist, length):
        self.title = title
        self.artist = artist
        self.length = length

    def __str__(self):
        mins = self.length // 60
        secs = self.length % 60
        output = f"Song Title: {self.title} by {self.artist}, Duration: {mins}:{secs}"
        return output


class Playlist:

    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, title):
        for song in self.playlist:
            if song.title == title:
                self.playlist.remove(song)

    def total_duration(self):
        duration = 0
        for song in self.playlist:
            duration += song.length
        return duration

    def __str__(self):
        playlist_duration = self.total_duration()
        mins = playlist_duration // 60
        secs = playlist_duration % 60
        output = "=" * 50 + "\n"
        output += "Playlist:\n"
        for song in self.playlist:
            output += f"{song}\n"
        output += "=" * 50 + "\n"
        output += f"Playlist Duration: {mins}:{secs:02d}"
        return output


def test_song():
    song = Song('Vitamin C', 'CAN', 212)
    song2 = Song('Train in Vain', 'The Clash', 194)
    song3 = Song('Cosmic Dance', 'T. Rex', 266)
    #print(song)
    playlist = Playlist()
    playlist.add_song(song)
    playlist.add_song(song2)
    playlist.add_song(song3)
    print(playlist)

test_song()