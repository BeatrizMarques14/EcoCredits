import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import glob

# read images

img2 = cv.imread('./testes/teste3.jpg',cv.IMREAD_GRAYSCALE) 

 
imgs_azul = sorted(glob.glob('./azul/rotulo*.jpg'))
imgs_verde = sorted(glob.glob('./verde/rotulo*.jpg'))
imgs_amarelo = sorted(glob.glob('./amarelo/ecoponto*.jpg'))


# Initiate SIFT detector
sift = cv.SIFT_create()
# # BFMatcher with default params
bf = cv.BFMatcher()

edged = cv.Canny(img2, 50, 300) 
# cv.waitKey(0) 
  
# Finding Contours 
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 

#sort contours by size
contours = sorted(contours, key=lambda x: cv.boundingRect(x)[2] * cv.boundingRect(x)[3], reverse=True)


#get the biggest contour's size
x_max, y_max, w_max, h_max = cv.boundingRect(contours[0])

 #cv.namedWindow('Imagem', cv.WINDOW_NORMAL)
 #cv.imshow('Imagem', img2) 
 #cv.waitKey(0) 

# draws the contours
cv.drawContours(img2, contours, -1, (0, 255, 0), 2)

good_amarelo=[]
good_azul=[]
good_verde=[]


for contour in contours:
     x, y, w, h = cv.boundingRect(contour)

     if (h> h_max-h_max/2) or (w > w_max-w_max/2):  
        box = img2[y:y+h, x:x+w]
        # cv.imshow('Box',box)
        # cv.waitKey(0)
        
        kp2, des2 = sift.detectAndCompute(box,None)
        
        #matches for blue images
        for name in imgs_azul:
            img_azul = cv.imread(name,cv.IMREAD_GRAYSCALE)
            img_azul = cv.resize(img_azul,(300,300))
            kpa1, desa1 = sift.detectAndCompute(img_azul,None)
            matches_azul = bf.knnMatch(desa1,des2,k=2)
            
            for m,n in matches_azul:
                if m.distance < 0.80*n.distance:
                    good_azul.append([m])
            
        #matches for yellow images
        for name in imgs_amarelo:
            img_amarelo = cv.imread(name,cv.IMREAD_GRAYSCALE)
            img_amarelo = cv.resize(img_amarelo,(200,200))
            kpam1, desam1 = sift.detectAndCompute(img_amarelo,None)
            matches_amarelo = bf.knnMatch(desam1,des2,k=2)
            
            for m,n in matches_amarelo:
                if m.distance < 0.80*n.distance:
                    good_amarelo.append([m]) 

                          
        #matches for green images
        for name in imgs_verde:
            img_verde = cv.imread(name,cv.IMREAD_GRAYSCALE)
            img_verde = cv.resize(img_verde,(200,200))
            kpv1, desv1 = sift.detectAndCompute(img_verde,None)
            matches_verde = bf.knnMatch(desv1,des2,k=2)
            
            for m,n in matches_verde:
                if m.distance < 0.80*n.distance:
                    good_verde.append([m])
                    
        
                    

                
        
# print('Amarelo: ' + str(len(good_amarelo)))
# print('Azul: ' + str(len(good_azul)))
# print('Verde: ' + str(len(good_verde)))


results = []
results.append(len(good_amarelo))
results.append(len(good_azul))
results.append(len(good_verde))


indice_decision = results.index(max(results))

if indice_decision == 0:
    result = "amarelo"
elif indice_decision ==1:
    result = "azul"
else:
    result = "verde"

print(result)
           
# cv.imshow('Contours', img2) 
# cv.waitKey(0) 


