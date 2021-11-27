import numpy as np
import cv2

# https://www.youtube.com/watch?v=oNjQpq8QuAo
# Models: https://github.com/richzhang/colorization/tree/caffe/colorization/models
# https://code.naturkundemuseum.berlin/mediaspherefornature/colorize_iiif/blob/master/experimental/model/colorization_release_v2.caffemodel

# Points: https://github.com/richzhang/colorization/blob/caffe/colorization/resources/pts_in_hull.npy

def colorize(image_path):
    prototxt_path = 'models/colorization_deploy_v2.prototxt'
    model_path = 'models/colorization_release_v2.caffemodel'
    kernel_path = 'models/pts_in_hull.npy'

    # neural network
    net =  cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
    # kernels
    points = np.load(kernel_path)

    # LAB Color Scheme --> L = lightness a*b ; NOT RGB
    points = points.transpose().reshape(2, 313, 1, 1)
    net.getLayer(net.getLayerId("class8_ab")).blobs = [points.astype(np.float32)]
    net.getLayer(net.getLayerId("conv8_313_rh")).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    bw_image = cv2.imread(image_path)
    normalized = bw_image.astype("float32") / 255.0
    lab = cv2.cvtColor(normalized, cv2.COLOR_BGR2LAB)

    # 224 x 224
    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0] #lightness
    L -= 50 # can adjust this value

    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1,2,0))

    # resize back to original size
    ab = cv2.resize(ab, (bw_image.shape[1], bw_image.shape[0]))
    L = cv2.split(lab)[0]

    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = (255.0 * colorized).astype("uint8")

    return bw_image, colorized

    
def mainMethod(image_path):
    bw_image, colorized = colorize(image_path)


    # cv2.imshow("BW Image", bw_image)
    # cv2.imshow("Colorized Image", colorized)
    cv2.imwrite("Images/new.png", colorized)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

mainMethod('Images/old.png') # to test specific images