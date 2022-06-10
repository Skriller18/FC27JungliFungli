
#importing cv2 so as to read the map image to find out the different routes
#These routes are later converted into matrix of 1,0 which will be used for getting shortest route using A* algorithm
#A nested list is used as a matrix
#Making a black pixel as 1 and other color as 0
import cv2
import numpy as np

try:
    # Reading the image using imread() function
    image = cv2.imread('black_image.jpg')

      
    # Extracting the height and width of an image
    h = image.shape[0]
    w = image.shape[1]


    # Displaying the height and width
    print("Height = {},  Width = {}".format(h, w))
    #Making nested list
    matrix = []
      
    for i in range(10):
          
        # Append an empty sublist inside the list
        #matrix.append([])
        line=[]
          
        for j in range(5):
            (B, G, R) = image[j, i]
            flag = True
            if(R<=10) and (B<=10) and (G<=10):
                #matrix[i][j] = 1
                #matrix[i].append(j)
                line.append(1)
            else:
                line.append(0)
        matrix.append(line)
              
    print(matrix)

    #np.set_printoptions(threshold=np.inf)
    #print(matrix)
    cv2.imshow("Image",image)
    cv2.waitKey()
    cv2.destroy()

except AttributeError:
    print("Image closed")

