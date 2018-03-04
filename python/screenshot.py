import cv2

#framerate is assumed 30 per second
def movToScreenshots(movFile, framesPer25 = 25, saveToFile=False):
    vidcap = cv2.VideoCapture(movFile)
    success, image = vidcap.read()
    success = True
    frameNumber = 0
    count = 0
    images = []

    while success:
        success, image = vidcap.read()
        # print('Read a new frame: ', success)
        if count == framesPer25 and success:
          images.append(image)
          if saveToFile:
              cv2.imwrite("frame%d.jpg" % frameNumber, image)     # save frame as JPEG file
          count = 0
          frameNumber += 1

        count += 1

    return images

if __name__ == "__main__":
    movToScreenshots('step.mov', 25 , True)
