#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: Hanna Schlegel
# email: hannasch@bu.edu
#


from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
        
    # Q 1
    def __init__(self, board, predecessor, move):
        """ constructs a new State object by initializing four fields below
        """
        self.board = board
        self.predecessor = predecessor
        self.move = move
        if predecessor == None:
            self.num_moves = 0
        else:
            self.num_moves = predecessor.num_moves + 1
            
    
    # Q 2
    def is_goal(self):
        """ returns True if the State object is a goal state and False otherwise
        """
        if self.board.tiles == GOAL_TILES:
            return True
        return False
    
    
    # Q 3
    def generate_successors(self):
        """ returns a list of State objects for all successor states of the called State object
        """
        successors = []
        for m in MOVES:
            b = self.board.copy()
            b2 = b.move_blank(m)
            if b2 == True:
                new_state = State(b, self, m)
                successors += [new_state]
        return successors
    
    
    # Part 3: Q 7
    def print_moves_to(self):
        """ Prints the sequence of moves that lead from the initial state to the called State object
        """
        if self.predecessor == None:    #base case
            print('initial state:')
            print(self.board)
        else:
            self.predecessor.print_moves_to()
            print('move the blank ' + self.move + ':')
            print(self.board)
        

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
