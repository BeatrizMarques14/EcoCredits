import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# read two input images as grayscale
img_azul = cv.imread('azul.png',cv.IMREAD_GRAYSCALE) # queryImage
img_verde = cv.imread('verde.png',cv.IMREAD_GRAYSCALE)
img_amarelo = cv.imread('amarelo.png',cv.IMREAD_GRAYSCALE)
img2 = cv.imread('rotulo1.png',cv.IMREAD_GRAYSCALE) # trainImage
# Initiate SIFT detector
sift = cv.SIFT_create()
# # BFMatcher with default params
bf = cv.BFMatcher()


#im2, contours = cv.findContours(img2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
edged = cv.Canny(img2, 50, 400) 
# cv.waitKey(0) 
  
# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
#contours = sorted(contours, key=cv.contourArea, reverse=True)
contours = sorted(contours, key=lambda x: cv.boundingRect(x)[2] * cv.boundingRect(x)[3], reverse=True)


x_max, y_max, w_max, h_max = cv.boundingRect(contours[0])

  
# cv.imshow('Canny Edges After Contouring', edged) 
# cv.waitKey(0) 

cv.drawContours(img2, [contours[0]], -1, (0, 255, 0), 2)

good_amarelo=[]
good_azul=[]
good_verde=[]
for contour in contours:
     x, y, w, h = cv.boundingRect(contour)

     if (h> h_max-h_max/2) or (w > w_max-w_max/2):  
        box = img2[y:y+h, x:x+w]
        kpa1, desa1 = sift.detectAndCompute(img_azul,None)
        kpv1, desv1 = sift.detectAndCompute(img_verde,None)
        kpam1, desam1 = sift.detectAndCompute(img_amarelo,None)
        kp2, des2 = sift.detectAndCompute(img2,None)
        
        matches_azul = bf.knnMatch(desa1,des2,k=2)
        # Apply ratio test
        for m,n in matches_azul:
            if m.distance < 0.95*n.distance:
                good_azul.append([m])
        
        matches_verde = bf.knnMatch(desv1,des2,k=2)
        # Apply ratio test
        for m,n in matches_verde:
            if m.distance < 0.95*n.distance:
                good_verde.append([m])
        
        matches_amarelo = bf.knnMatch(desam1,des2,k=2)
        # Apply ratio test
        for m,n in matches_amarelo:
            if m.distance < 0.95*n.distance:
                good_amarelo.append([m])
            

# print('Amarelo: ' + str(len(good_amarelo)))
# print('Azul: ' + str(len(good_azul)))
# print('Verde: ' + str(len(good_verde)))    

results = []
results.append(len(good_amarelo))
results.append(len(good_azul))
results.append(len(good_verde))

decision = max(results)

print(str(decision))
           
# cv.imshow('Contours', img2) 
# cv.waitKey(0) 

