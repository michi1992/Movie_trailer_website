class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, poster_url, youtube_trailer_link):
        # assign the provided arguments to the needed instance variables
        self.title = movie_title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_trailer_link