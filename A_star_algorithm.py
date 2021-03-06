import cv2
from endNode import getEndNodeDep
from endNode import getEndNodeFloor
from matices import mazecollege
from matrices2 import biotechmaze
from matrices3 import mcamaze
#from frontendgui import txt

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

def astar(maze, start, end):
    

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
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable path
            if maze[node_position[0]][node_position[1]] != 0:
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
def main():

    pathimg=r'RVCE_map_black_route_croppedformatrix.jpg'
    img=cv2.imread(pathimg)

    color=(0,0,255)
    start = (51, 393)
    end = (0, 0)
    endDep = getEndNodeDep()

    campusPath = astar(mazecollege, start, endDep)

    for c in range(len(campusPath)):
        i, j = campusPath[c]
        img = cv2.circle(img, (i,j), 2, color, 2)

    #print(campusPath)

    if end != endDep:
        floorPath = astar(mcamaze, (579, 859), getEndNodeFloor())
        for c in range(len(floorPath)):
            i, j = floorPath[c]
            img = cv2.circle(img, (i, j), 2, color, 2)

    #for c in range (50,150):
        #for j in range(300,400):
            #if maze[c][j]==0:

                #img=cv2.circle(img,(c,j),2,color,thickness=2)

    cv2.imshow("IMAGE", img)
    cv2.imwrite('C:/RVDAR/final.jpg', img)
    cv2.waitKey()
    cv2.destroy()


if __name__ == '__main__':
    main()
