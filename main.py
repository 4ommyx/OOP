class Post(Workshop):
    def __init__(self,id,media_link,poster): 
        self.__id = id
        self.__media_link = media_link
        self.__poster = poster 
class Workshop:
    def __init__(self,name,from_game,sub_date="",last_update="",is_recomment=None,is_favorite=None,is_subscrice=None):
        self.__name = name
        self.__from_game = from_game
        self.__sub_date = sub_date
        self.__last_update = last_update
        self.__is_recomment = is_recomment
        self.__is_favorite = is_favorite
        self.__is_subscrice = is_subscrice
class Comment:
    def __init__(self,name,id,date,reply=[]):
        self.__name = name
        self.__id = id
        self.__date = date
        self.__reply = reply
class Rating:
    def __init__(self,rating,thumbs_up=None,thumbs_down=None):
        self.__thumbs_up = thumbs_up
        self.__thumbs_down = thumbs_down
        self.__rating = rating
