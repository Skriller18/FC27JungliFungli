import cv2 as cv
import numpy as np
from matrix_maker import matrix
#Node required for A* algorithm
#parent and position is part of self in this node
class Node():
    

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

#A* algorithm for a shortest path in the matrix made from the map
#Each node point will be initialized using a pixel point on the image
    
def astar(matrix, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
#Main function using Astat algo for path using start and end point put directly into the code
#Start will be read from qr and end point will later be taken from user
#A* star algorithm still not complete
#path and childCell variable needs to be added
def main():

    start = (0, 0)
    end = (7, 6)


if __name__ == '__main__':
    main()
