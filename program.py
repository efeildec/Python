import cv2

resim=cv2.imread('resim.jpg',1)
cv2.imshow("Orijinal Resim",resim)

r=resim[:,:,0]
g=resim[:,:,1]
b=resim[:,:,2]

cv2.imshow("Kirmizi",r)
cv2.imshow("Yesil",g)
cv2.imshow("Mavi",b)

cv2.waitKey()
cv2.destroyAllWindows()