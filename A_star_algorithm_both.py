import cv2
from MCAMartix import matrixreader
from RVCEMatrix import matrixcollegereader
import cv2 as cv
from finalapp import txt


dict1 = [
    {
        "name" : "AI001",
        "co-ords" : [744, 268]
    },

    {
        "name" : "AI002 (Door 1)",
        "co-ords" : [682,785]
    },

    {
        "name" : "AI002 (Door 2)",
        "co-ords" : [681,479]
    },

    {
        "name" : "AI003",
        "co-ords" : [467, 649]
    },

    {
        "name" : "Staff Restroom 1",
        "co-ords" : [263, 320]
    },

    {
        "name" : "Staff Restroom 2",
        "co-ords" : [791, 411]
    },

    {
        "name" : "Staff Room 1",
        "co-ords" : [789, 304]
    },

    {
        "name" : "Staff Room 2",
        "co-ords" : [562, 202]
    },

    {
        "name" : "Staff Room 3",
        "co-ords" : [361, 325]
    },

    {
        "name" : "Gents' Restroom",
        "co-ords" : [209, 377]
    },

    {
        "name" : "Ladies' Restroom",
        "co-ords" : [261, 426]
    }
]
end = ()
for i in range(len(dict1)):
    if dict1[i]['name'] == tx:
        end = dict1[i]['co-ords']
        break


import numpy as np
#from Matrix_maker import matrix

class Node():
    #Node required for A* algorithm
    #parent and position is part of self in this node

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
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(matrix) - 1) or node_position[0] < 0 or node_position[1] > (len(matrix[len(matrix)-1]) -1) or node_position[1] < 0:
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
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
#Main function using Astat algo for path using start and end point put directly into the code
#Start will be read from qr and end point will later be taken from user
def main1():

    maze=matrixreader()
    print(maze[0][5])
    pathimage=r'MCA_clean.png'
    img=cv2.imread(pathimage)
    color=(0,0,255)
    start = (751,327)

    for i in range(len(dict1)):
        if dict1[i]['name'] == txt:
            path = astar(maze, start, dict1[i]['co-ords'])
            for c in range(len(path)):
                i, j = path[c]
                img = cv2.circle(img, (i, j), 2, color, 2)
                cv2.imwrite("C:\RVDAR2.0\FinalBUILDING.jpg", img)
                cv2.waitKey()
                cv2.destroyAllWindows()
            break



def main2():

    maze=matrixcollegereader()
    print(maze[0][5])
    pathimage=r'MAINMAP_clean.jpeg'
    img=cv2.imread(pathimage)
    color=(0,0,255)
    start = (376,309)
    end = (178,516)

    path = astar(maze, start, end)
    #print(path)

    for c in range (len(path)):
        i, j = path[c]
        img=cv2.circle(img,(i,j),2,color,2)
        cv2.imwrite("C:\RVDAR2.0\Finalmap.jpg", img)




    #print(path)


    cv2.waitKey()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main2()
    main1()
