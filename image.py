import cv2
import numpy as np
img=cv2.imread('C:\\Users\\hp\\geeksforgeeks.png')
img1=cv2.imwrite('C:\\Users\\hp\\geeksforgeeks2.png',img)
imp=cv2.imshow('geeksforgeeks2',img)
print('Height Of Image:',int(img.shape[0]),'pixels')
print('Height Of Image:',int(img.shape[1]),'pixels')  
print(img.shape) 
cropped_image = img[80:280, 150:330]
cv2.imshow("cropped", cropped_image)
cv2.imwrite("Cropped Image.jpg", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
