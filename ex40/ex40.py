class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
        print "\n"


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])


bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])


happy_bday.sing_me_a_song()


bulls_on_parade.sing_me_a_song()

lyrics = ['Last night, she said:',
          '"Oh, baby, I feel so down.',
          'Oh it turns me off,',
          'When I feel left out"']
          
the_strokes_last_nite = Song(lyrics)

the_strokes_last_nite.sing_me_a_song()