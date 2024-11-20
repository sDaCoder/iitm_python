def index_of_first_occurance(row:list,elem):
    for i in range(len(row)):
        if row[i] == 1:
            return i

def index_of_last_occurance(row:list,elem):
    for i in range(len(row)-1,-1,-1):
        if row[i] == 1:
            return i

def is_valid_coordinate(x:int,y:int, M):
    return 0 <= x < len(M) and 0 <= y < len(M[0])

def valid_adjacent_coordinates(x:int,y:int, M):
    '''
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
    '''
    return {
      (x1,y1)
      for x1,y1 in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]  # all the possible adjacent coordinates
      if is_valid_coordinate(x1,y1, M)
    }

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None
    '''
    # Get the current row and column
    row, col = curr_coords
    m, n = len(M), len(M[0])

    # Possible directions to move (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Iterate through each direction to find the next 1
    for dr, dc in directions:
        # Calculate the new row and column
        new_row, new_col = row + dr, col + dc
        
        # Check if the new position is within bounds and is a 1
        if 0 <= new_row < m and 0 <= new_col < n:
            if M[new_row][new_col] == 1 and (new_row, new_col) != prev_coords:
                return (new_row, new_col)
    
    # Return None if no valid neighbor is found
    return None

def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    '''
    x_start, x_end = len(M)-1,0
    y_start, y_end = index_of_last_occurance(M[-1],1), index_of_first_occurance(M[0],1)

    path = []

def print_path(M):
    path = get_path_coordinates(M)
    ...

def alternate_path(M):
    path = get_path_coordinates(M)
    ...

def count_path(M):
    path = get_path_coordinates(M)
    ...

def mirror_horizontally(M):
    path = get_path_coordinates(M)
    ...

def mirror_vertically(M):
    path = get_path_coordinates(M)
    ...
