__author__ = 'Ahmed Hani Ibrahim'


class Transition(object):

    def GetAction(self):
        return self.__action

    def SetAction(self, action):
        self.__action = action

    def GetReinforcementCost(self):
        return self.__reinforcementCost

    def SetReinforcementCost(self, reinforcementCost):
        self.__reinforcementCost = reinforcementCost

    def GetDestinationState(self):
        return self.__destinationState
    def SetDestinationState(self, state):
        self.__destinationState = state

    def GetQValue(self):
        return self.__qValue

    def SetQValue(self, value):
        self.__qValue = value

    def __init__(self, action, reinforcementCost, destinationState, qValue):
        self.__action = action
        self.__reinforcementCost = reinforcementCost
        self.__destinationState = destinationState
        self.__qValue = qValue

