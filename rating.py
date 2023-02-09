class Rating:
    def __init__(self,rating,thumbs_up=None,thumbs_down=None):
        self.__thumbs_up = thumbs_up
        self.__thumbs_down = thumbs_down
        self.__rating = rating
