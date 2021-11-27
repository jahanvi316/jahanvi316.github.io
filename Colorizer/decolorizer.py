# https://techtutorialsx.com/2019/04/13/python-opencv-converting-image-to-black-and-white/
import cv2

def decolorize(imagePath):
    originalImage = cv2.imread(imagePath)
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    
    return originalImage, grayImage, blackAndWhiteImage

def mainMethod(image_path):
    originalImage, grayImage, blackAndWhiteImage = decolorize(image_path)

    # cv2.imshow('Black white image', blackAndWhiteImage)
    # cv2.imshow('Original image',originalImage)
    # cv2.imshow('Gray image', grayImage)
    cv2.imwrite("Images/new.png", grayImage)

    
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


mainMethod('Images/old.png')  # to test specific images