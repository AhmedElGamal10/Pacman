# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import Queue
from game import Directions

NORTH = Directions.NORTH
SOUTH = Directions.SOUTH
EAST = Directions.EAST
WEST = Directions.WEST
STOP = Directions.STOP


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def inStack(successor, s, name):
    list = []

    if name == "ucs" or name == "astar":
        list = s.heap
    else:
        list = s.list

    if name == "ucs" or name == "astar":
        list = s.heap

    for element in list:
        if element[0] == successor[0]:
            return True
    return False


def firstSearchSolution(problem, frontier, name):
    s = frontier
    start_state = problem.getStartState()

    solution = []
    visited = []
    parentStateMap = dict()
    parentActionMap = dict()
    parentCostMap = dict()

    # print start_state

    if problem.isGoalState(start_state):
        return solution
    if name == "dfs" or name == "bfs":
        s.push([start_state, STOP, 0])
    elif name == "ucs" or name == "astar":
        s.push([start_state, STOP, 0], 0)

    while not s.isEmpty():
        current = s.pop()
        current_state = current[0]
        current_action = current[1]
        current_cost = current[2]

        # print "current cost is: ", current_cost
        parentActionMap[current_state] = current_action

        if current_state not in visited:
            if problem.isGoalState(current_state):
                solution = []
                while (current_state != start_state):
                    solution.append([parentActionMap[current_state]][0])
                    current_state = parentStateMap[current_state]
                inOrderSolution = list(reversed(solution))
                return (inOrderSolution)

            visited.append(current_state)
            successors = problem.getSuccessors(current_state)
            total_cost = 0
            for successor in successors:

                if not inStack(successor, s, name) and successor[0] not in visited:
                    if name == "dfs" or name == "bfs":
                        total_cost = current_cost + 1
                        s.push([successor[0], successor[1], total_cost])
                    elif name == "ucs":
                        total_cost = current_cost + successor[2]
                        s.push([successor[0], successor[1], total_cost], total_cost)
                    elif name == "astar":
                        total_cost = current_cost + successor[2] + nullHeuristic(successor[0], problem)
                        s.push([successor[0], successor[1], total_cost], total_cost)

                    if not parentCostMap.has_key(successor[0]) or parentCostMap[
                        successor[0]] >= total_cost or name == "dfs":
                        parentStateMap[successor[0]] = current_state
                        parentCostMap[successor[0]] = total_cost
    return []


def depthFirstSearch(problem):
    return firstSearchSolution(problem, Stack(), "dfs")
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    return firstSearchSolution(problem, Queue(), "bfs")

    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue
    return firstSearchSolution(problem, PriorityQueue(), "ucs")
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    return firstSearchSolution(problem, PriorityQueue(), "astar")
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch