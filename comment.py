class Comment:
    def __init__(self,name,id,date,reply=[]):
        self.__name = name
        self.__id = id
        self.__date = date
        self.__reply = reply