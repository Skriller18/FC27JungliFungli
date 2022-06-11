import cv2
from MCAMartix import matrixreader
from RVCEMatrix import matrixcollegereader
from FrontEnd import tx
from endNode import jsonFile
import cv2 as cv
import numpy as np


# from Matrix_maker import matrix

class Node():
    # Node required for A* algorithm
    # parent and position is part of self in this node

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


# A* algorithm for a shortest path in the matrix made from the map
# Each node point will be initialized using a pixel point on the image

def astar(matrix, start, end):
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

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(matrix) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(matrix[len(matrix) - 1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if matrix[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


# Main function using Astat algo for path using start and end point put directly into the code
# Start will be read from qr and end point will later be taken from user
def main():
    start = (429,376)
    end = tx
    '''endDep = tagger(end)
    endDepCoords = getEndNode(endDep)'''

    maze = matrixcollegereader()
    pathimage = r'MAINMAP_clean.jpeg'
    img = cv2.imread(pathimage)
    color = (0, 0, 255)
    end=(186, 621)
    print(end)
    path = astar(maze, start, end)

    for c in range(len(path)):
        i, j = path[c]
        img = cv2.circle(img, (i, j), 2, color, 2)
    # print(path)

    '''if endDep != end:
        maze = matrixreader()
        pathimage = r'MCA_clean.png'
        img1 = cv2.imread(pathimage)
        color = (0, 0, 255)
        path = astar(maze, (579, 859), getRoomCoords(end))

        for c in range(len(path)):
            i, j = path[c]
            img1 = cv2.circle(img1, (i, j), 2, color, 2)'''

    # print(path)
    cv2.imshow("IMAGE", img)
    cv2.imshow("IMAGE", img1)
    cv2.imwrite("C:\RVDAR2.0\FINAL_DRAW.jpg", img)
    cv2.imwrite("C:\RVDAR2.0\FINAL_DRAW_INSIDE.jpg", img1)

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
