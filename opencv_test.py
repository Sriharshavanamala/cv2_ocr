import cv2
img=cv2.imread('C:\\Users\\Armed Bunker\\Downloads\\Ugadi_FEATURE.jpg',1) # which 0-is 2dim array,1-3dim array
print(type(img))
print(img.shape)#eg 200*250*3 is rgb,200*300 is a black white img
print(img) #converts into numpy
resized=cv2.resize(img,(500,300))#resizeing an image by pixel
#resized=cv2.resize(img,(img.shape[1]*2,img.shape[0]*2))


show=cv2.imshow('digit',resized)
cv2.waitKey(0)#zero is black and white, 1 is colour 
cv2.destroyAllWindows()

# so we need to use cascade classifier to detect face here
