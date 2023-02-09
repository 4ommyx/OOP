class Workshop:
    def __init__(self,name,from_game,sub_date="",last_update="",is_recomment=None,is_favorite=None,is_subscrice=None):
        self.__name = name
        self.__from_game = from_game
        self.__sub_date = sub_date
        self.__last_update = last_update
        self.__is_recomment = is_recomment
        self.__is_favorite = is_favorite
        self.__is_subscrice = is_subscrice