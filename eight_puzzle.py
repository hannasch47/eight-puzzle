#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Hanna Schlegel
# email: hannasch@bu.edu
#


from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()


# Q 1
def process_file(filename, algorithm, param):
    """ Open the file for reading, loop to process the file and obtain the digit 
        string, solve the eight puzzle, and return the number of moves
    """
    file = open(filename, 'r')
    puzzle_count = 0
    moves_count = 0
    states_count = 0
    
    for line in file:
        digitstr = line[:-1]
        board = Board(digitstr)
        state = State(board, None, 'init')
        searcher = create_searcher(algorithm, param)
        
        if searcher == None:
            return
        
        soln = None
        try:
            soln = searcher.find_solution(state)
        except KeyboardInterrupt:
            print('search terminated, ', end='')
            
        if soln == None:
            print(digitstr + ': no solution')
        else:
            print(digitstr + ':', soln.num_moves, 'moves,', searcher.num_tested, 'states tested')
            puzzle_count += 1
            moves_count += soln.num_moves
            states_count += searcher.num_tested
            
    print()
    print('solved', puzzle_count, 'puzzles')
    if puzzle_count != 0:
        print('averages:', moves_count/puzzle_count, 'moves,', states_count/puzzle_count, 'states tested')
            
    file.close()
