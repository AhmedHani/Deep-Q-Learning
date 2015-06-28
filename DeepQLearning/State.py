__author__ = 'Ahmed Hani Ibrahim'
from Transition import Transition


class State(object):
    __name = None
    __transitions = [None]

    def GetTransitions(self):
        return self.__transitions

    def GetName(self):
        return self.__name

    def __init__(self, name):
        self.__name = name
        self.__transitions = [Transition]

    def addTransition(self, transition):
        self.__transitions.append(transition)



