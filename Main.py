from Vision import Vision
import cv2

vision = Vision()

vision.setWebcam(0)

while True:
   vision.getImg()
   vision.getClosestFace()
   vision.highlightFace()
   vision.stream()
   cv2.waitKey(1)
   