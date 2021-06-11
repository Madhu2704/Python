import cv2 as cv


LARGE_IMAGE_PATH = r'photos\bruce_lee_large_image.jpg'

VIDEO_PATH = r'video/loki.mp4'


def resizeResolution(videoframe, width, height):
    # ONLY WORKS FOR LIVE RECORDING VIDEOS
    # DOESNOT WORKS FOR EXISTING VIDEOS
    videoframe.set(3, width)
    videoframe.set(4, height)


def rescaleFrame(frame, scale=0.75):
    width, height = int(frame.shape[1]*scale), int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def viewImage(imagePath):
    # using imread('path') and 0 denotes read as  grayscale image
    colorImg = cv.imread(imagePath, 1)
    print(f"TYPE OF THE IMAGE:{type(colorImg)}")
    # To View the Image
    # cv.imshow(<TITLE FOR THE WINDOW>, IMG)
    cv.imshow('Color Image', rescaleFrame(colorImg, .25))
    cv.waitKey(0)
    cv.destroyAllWindows()


def viewVideo(videoPath):
    capture = cv.VideoCapture(videoPath)
    # TO CAPTURE THE VIDEO FROM WEB CAM
    # capture = cv.VideoCapture(0)
    while True:
        isTrue, frame = capture.read()
        cv.imshow('Video', rescaleFrame(frame, .75))
        if cv.waitKey(20) and 0xFF == ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    viewVideo(VIDEO_PATH)
