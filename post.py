from workshop import Workshop
class Post(Workshop):
    def __init__(self,id,media_link,poster): 
        self.__id = id
        self.__media_link = media_link
        self.__poster = poster 