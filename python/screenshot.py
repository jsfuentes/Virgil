import cv2
from time import time
vidcap = cv2.VideoCapture('step.mov')
success,image = vidcap.read()
success = True
frameRate = 30
frameNumber = 0
count = 0

while success:
  success, image = vidcap.read()
  print('Read a new frame: ', success)
  if count == 30:
      cv2.imwrite("frame%d.jpg" % frameNumber, image)     # save frame as JPEG file
      count = 0
      frameNumber += 1
  count += 1
