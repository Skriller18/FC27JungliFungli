import cv2 as cv
img = cv.imread('firstfloor_clean.png')
var = input("Current Location")
if var == "AI002D1":
    cv.circle(img, (682, 785), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
    cv.imwrite("D:/programming/python/RVDAR/endpoint.jpg", img)
if var == "AI002D2":
    cv.circle(img, (681, 479), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
    cv.imwrite("D:/programming/python/RVDAR/endpoint.jpg", img)
if var == "Staff Restroom 2":
    cv.circle(img, (791,  411), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
    cv.imwrite("D:/programming/python/RVDAR/endpoint.jpg", img)
if var == "Staff Room 1":
    cv.circle(img, (789, 304), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
    cv.imwrite("D:/programming/python/RVDAR/endpoint.jpg", img)
if var == "AI001":
    cv.circle(img, (744, 268), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
    cv.imwrite("D:/programming/python/RVDAR/endpoint.jpg", img)
if var == "Staff Room 2":
    cv.circle(img, (562, 202), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
    cv.imwrite("D:/programming/python/RVDAR/endpoint.jpg", img)
if var == "MCA001":
    cv.circle(img, (500, 229), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
    cv.imwrite("D:/programming/python/RVDAR/endpoint.jpg", img)
if var == "Staff Room 3":
    cv.circle(img, (361, 325), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
    cv.imwrite("D:/programming/python/RVDAR/endpoint.jpg", img)
if var == "Staff Restroom 1":
    cv.circle(img, (263, 320), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
    cv.imwrite("D:/programming/python/RVDAR/endpoint.jpg", img)
if var == "Gents Restroom":
    cv.circle(img, (209, 377), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
    cv.imwrite("D:/programming/python/RVDAR/endpoint.jpg", img)
if var == "Ladies Restroom":
    cv.circle(img, (261, 426), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
if var == "AI003":
    cv.circle(img, (467, 649), 2, (255, 0, 0), thickness=3)
    cv.imshow("Image", img)
    cv.imwrite("D:/programming/python/RVDAR/endpoint.jpg", img)
cv.waitKey()
cv.destroyAllWindows()
