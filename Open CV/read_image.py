import cv2 as cv
import os

FILE_PATH = r'photos\hd car wallpapers for mobile (5).jpg'

LARGE_IMAGE_PATH = r'photos\bruce_lee_large_image.jpg'
# using imread('path') and 0 denotes read as  grayscale image
colorImg = cv.imread(FILE_PATH, 1)
grayScaleLargeImg = cv.imread(LARGE_IMAGE_PATH, 0)

print(f"TYPE OF THE IMAGE:{type(colorImg)}")
# To View the Image
# cv.imshow(<TITLE FOR THE WINDOW>, IMG)
cv.imshow('Color Image', colorImg)
cv.imshow('Gray Scale Image', grayScaleLargeImg)

cv.waitKey(0)
cv.destroyAllWindows()
