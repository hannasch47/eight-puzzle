#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Hanna Schlegel
# email: hannasch@bu.edu
#


# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = digitstr[3*r + c]
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c
                    
    ### Add your other method definitions below. ###

    # Q 2
    def __repr__(self):
        """ returns a string representation of a Board object
        """
        s = ''
        
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    s += '_ '
                else:
                    s = s + self.tiles[r][c] + ' '
            s += '\n'
        return s
        
        
    # Q 3
    def move_blank(self, direction):
        """ modifies the Board object based on the direction the blank should move
        """
        if direction != 'up' and direction != 'down' and direction != 'left' and direction != 'right':
            return False
        
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    new_r = r
                    new_c = c
                    if direction == 'up':
                        new_r -= 1
                    elif direction == 'down':
                        new_r += 1
                    elif direction == 'left':
                        new_c -= 1
                    elif direction == 'right':
                        new_c += 1
                
                    if new_r > 2 or new_r < 0:
                        return False
                    elif new_c > 2 or new_c < 0:
                        return False
                    else:
                        self.tiles[r][c] = self.tiles[new_r][new_c]
                        self.tiles[new_r][new_c] = '0'
                        self.blank_r = new_r
                        self.blank_c = new_c
                        return True


    # Q 4
    def digit_string(self):
        """ returns a string of digits that corresponds to the current contents of the Board's tiles attribute
        """
        s = ''
        
        for r in range(3):
            for c in range(3):
                s += self.tiles[r][c] 
        return s
        
    
    # Q 5
    def copy(self):
        """ returns a new deep copy of the Board 
        """
        return Board(self.digit_string())
    
    
    # Q 6
    def num_misplaced(self):
        """ returns the number of tiles not in the goal state on the board
        """
        count = 0
        if self.tiles[0][1] != GOAL_TILES[0][1]:
            count += 1
        if self.tiles[0][2] != GOAL_TILES[0][2]:
            count += 1
        if self.tiles[1][0] != GOAL_TILES[1][0]:
            count += 1
        if self.tiles[1][1] != GOAL_TILES[1][1]:
            count += 1
        if self.tiles[1][2] != GOAL_TILES[1][2]:
            count += 1
        if self.tiles[2][0] != GOAL_TILES[2][0]:
            count += 1
        if self.tiles[2][1] != GOAL_TILES[2][1]:
            count += 1
        if self.tiles[2][2] != GOAL_TILES[2][2]:
            count += 1
        return count

    # # Part 6 Q 4
    def num_misplaced_2(self):
        """ returns the number of tiles not in the goal state on the board 
            and accounts for number of moves left
        """
        score = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                my_tile = self.tiles[r][c]
                if my_tile != GOAL_TILES[r][c] and my_tile != '0':
                    score += abs(r - int(my_tile) // 3)
                    score += abs(c - int(my_tile) % 3)
        return score

    # Q 7
    def __eq__(self, other):
        """ returns True if self and other have the same values for each Tile attribute and False otherwise
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False
    