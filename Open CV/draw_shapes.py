import cv2 as cv
import numpy as np
from pprint import pprint


def createBlankImage():
    # (500,500,3) Represents the rows, columns and color channel of the blank image
    # uint8 is the data type used for the images
    return np.zeros((500, 500, 3), dtype='uint8')


def drawRectangleShapeOnimage(image):
    # Seting the thickness to CV.FILLED or -1 it fills the entire shape instead of borders
    cv.rectangle(image, pt1=(0, 0), pt2=(250, 250),
                 color=(0, 250, 0), thickness=3)


def drawCircleShapeOnimage(image):
    cv.circle(image, center=(
        image.shape[1]//2, image.shape[0]//2), radius=40, color=(0, 255, 255), thickness=-1)


def drawLineOnimage(image):
    cv.line(image, pt1=(0, 0), pt2=(
        image.shape[1]//2, image.shape[0]//2),
        color=(255, 255, 255), thickness=3)


def putTextOntheImage(image, textContent):
    cv.putText(image, textContent, (255, 255), cv.FONT_HERSHEY_TRIPLEX,
               1.0, (255, 255, 255), 3)


if __name__ == '__main__':
    blankImage = createBlankImage()
    # pprint(blankImage)
    blankImage[:] = 0, 0, 255
    cv.imshow('Green', blankImage)
    drawRectangleShapeOnimage(blankImage)
    drawCircleShapeOnimage(blankImage)
    drawLineOnimage(blankImage)
    putTextOntheImage(blankImage, 'Hello loki')
    cv.imshow('Rectangle Border On Image', blankImage)
    cv.waitKey(0)
    cv.destroyAllWindows()
