import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# read two input images as grayscale
img1 = cv.imread('azul.png',cv.IMREAD_GRAYSCALE) # queryImage
img2 = cv.imread('rotulo1.png',cv.IMREAD_GRAYSCALE) # trainImage
# Initiate SIFT detector
sift = cv.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.95*n.distance:
        good.append([m])
print(len(good))
# cv.drawMatchesKnn expects list of lists as matches.
# img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# plt.imshow(img3),plt.show() 

#im2, contours = cv.findContours(img2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
edged = cv.Canny(img2, 150, 300) 
cv.waitKey(0) 
  
# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
largest_contour = max(contours, key=cv.contourArea)
print(len(contours))

  
cv.imshow('Canny Edges After Contouring', edged) 
cv.waitKey(0) 

cv.drawContours(img2, [largest_contour], -1, (0, 255, 0), 2)

  
cv.imshow('Contours', img2) 
cv.waitKey(0) 

