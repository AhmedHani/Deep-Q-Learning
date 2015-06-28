__author__ = 'Ahmed Hani Ibrahim'
from State import State
from Transition import Transition


class QLearning(object):

    def train(self, initState, actions):
        currentState = initState
        foundState = False

        #iterator = iter(actions)

        for action in actions:
            for transition in currentState.GetTransitions:
                if foundState:
                    break

                if transition.GetAction().name == action.GetActionName():
                    transition.SetQValue(transition.GetReinforcementCost() + self.__learningRate *
                                         self.__maxValue(transition.GetDestinationState()))
                    currentState = transition.GetDestinationState()
                    foundState = True

            foundState = False

    def agentPlay(self, initState):
        currentState = initState
        temp = Transition
        print(currentState.GetName + " -> ")

        while True:
            temp = self.__bestMove(currentState.GetTransitions())
            print(temp.GetDestinationState().GetName() + " -> ")
            currentState = temp.GetDestinationState()

    def __maxValue(self, state):
        maxVal = 0.0

        for transition in state.GetTransitions():
            if transition.GetQValue() > maxVal:
                maxVal = transition.GetQValue()

        return maxVal

    def addState(self, state):
        self.__states.append(state)

    def __bestMove(self, transitions):
        bestTransition = transitions.get(0)
        temp = Transition

        for transition in transitions:
            temp = transition

            if temp.GetQValue() > bestTransition.GetQValue():
                bestTransition = temp

        return bestTransition

    def logs(self):
        for state in self.__states:
            for transition in state.GetTransitions():
                print(state.GetName() + " " + transition.GetAction().GetName + " " + transition.GetQValue())



    def __init__(self, learningRate):
        self.__states = [State]
        self.__learningRate = learningRate

