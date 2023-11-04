#Showing how to create, instantiate and use a class.


#Writing class representing a song
class Song(object):

    def __init__(self, lyrics):  #__init__ is the constructor method of the class. self represents the object in creation, the others are arbitrary parameters. In this case we chose to add lyrics.
        self.lyrics = lyrics  # Defining lyrics field of the object in creation ad assigning it lyrics passed to the constructor.
    
    def sing(self):  #Method that prints the lyrics of the song.
        for line in self.lyrics:
            print(line)


#Using the Song class

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there!"])  # Creation of a new song object

hotel_california = Song(["Welcome to the hotel california", "Such a lovely place", "..."])  # Creation of a new song object

happy_bday.sing()

hotel_california.sing()


