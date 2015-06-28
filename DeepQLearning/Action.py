__author__ = 'Ahmed Hani Ibrahim'


class Action(object):

    def GetActionName(self):
        return self.__name

    def SetActionName(self, name):
        self.__name = name

    def __init__(self, name):
        self.__name = name
