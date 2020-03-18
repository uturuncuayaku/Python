import cv2

image = cv2.imread('H:/DownloadsFirefox/test.jpg')
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('original image', image)
cv2.imshow('hsv Image', hsvImage)
cv2.imwrite('H:/Code/Python/ImageManipulation/test1.jpg', hsvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
