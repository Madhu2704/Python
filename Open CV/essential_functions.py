import cv2 as cv


def convertImageToGrayScale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)


def blurImage(image):
    return cv.GaussianBlur(image, (7, 7), cv.BORDER_DEFAULT)


def getEdgesOfImage(image):
    return cv.Canny(image, 125, 175)


if __name__ == '__main__':
    IMAGE_PATH = r'photos/dhoni.jfif'
    image = cv.imread(IMAGE_PATH)
    grayImage = convertImageToGrayScale(image)
    blurimage = blurImage(image)
    cannyImage = getEdgesOfImage(image)
    cv.imshow('Gray Scale Image', cannyImage)
    cv.waitKey(0)
    cv.destroyAllWindows()
