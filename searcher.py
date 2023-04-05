#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Hanna Schlegel
# email: hannasch@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
    # Q 1
    def __init__(self, depth_limit):
        """ Constructs a new Searcher object with initialization         
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit


    # Q 2
    def add_state(self, new_state):
        """ Takes a single State object and adds it to the Searcher's list of untested states
        """
        self.states += [new_state]


    # Q 3
    def should_add(self, state):
        """ Takes a State object and returns True if the called Searcher should add state to its list of untested states
            returns False otherwise
        """
        if self.depth_limit != -1 and self.depth_limit < state.num_moves:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True
            
    
    # Q 4
    def add_states(self, new_states):
        """ Takes a list State objects called new_states and processes the elements of new_states one at a time
        """
        for s in new_states:
            if self.should_add(s):
                self.add_state(s)
                
    
    # Q 5
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
        
        
    # Q 6
    def find_solution(self, init_state):
        """ Performs full state-space search that begins at the specific initial state init_state and 
            ends when the goal state is found or when the Searcher runs out of untested states
        """
        self.add_state(init_state)
        while self.states != [] :
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal() == True:
                return s
            else:
                self.add_states(s.generate_successors())
        return None


    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your BFSearcher and DFSearcher class definitions below. ###

# Q 1
class BFSearcher(Searcher):
    """ subclass of Searcher that performs breadth-first search instead of random search
    """
    def next_state(self):
        """ overrides the previous next_state tp follow first-in first-out ordering
        """
        s = self.states[0]
        self.states.remove(s)
        return s
    

# Q 2
class DFSearcher(Searcher):
    """ subclass of Searcher that performs depth-first search instead of random search
    """
    def next_state(self):
        """overrides the previous next_state tp follow last-in first-out ordering
        """
        s = self.states[-1]
        self.states.remove(s)
        return s
    
    
def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

# Q d. 
def h1(state):
    """ a heuristic function that returns number of misplaced tiles
    """
    return state.board.num_misplaced()

# Q 4
def h2(state):
    """ an alternative heuristic function to distinguish between states with the same number of misplaced tiles
    """
    return state.board.num_misplaced_2()
    

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    
    # Q b.
    def __init__(self, heuristic):
        """ constructs a new GreedySearcher object
        """
        super().__init__(-1)
        self.heuristic = heuristic
    

    # Q c.
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


    # Q e.
    def add_state(self, state):
        """ Adds a sublist that is a [priority, state] pair, where priority is the priority of state 
        """
        self.states += [[self.priority(state), state]]
        
        
    # Q f.
    def next_state(self):
        """ Chooses one of the states with the highest priority as next state
        """
        max_ch = max(self.states)
        self.states.remove(max_ch)
        return max_ch[1]

    
### Add your AStarSeacher class definition below. ###

# Q 2
class AStarSearcher(GreedySearcher):
    """ subclass of GreedySearcher that is an informed algorithm that assigns priority to a state
    """
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function given to us
        """
        return -1 * (self.heuristic(state) + state.num_moves)
