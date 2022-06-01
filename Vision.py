import cv2
from Face import Face

class Vision:
   def __init__(self):
      self.capturedImage=None
      self.img= None
      self.source= ""
      self.faces = []
      self.face = Face(0,0,0,0)

   def setWebcam(self, webcam):
      self.capturedImage = cv2.VideoCapture(webcam)
      self.source = "Webcam"
   
   def setDrone(self,drone):
      # self.capturedImage = drone.get_frame_read().frame
      self.source = "Drone"

   def getImg(self):
      if self.source == "Webcam":
         _,self.img = self.capturedImage.read()
         self.img = cv2.resize(self.img,(360 ,240))

   def stream(self):
      cv2.imshow(self.source, self.img)

   def getFaces(self):
      self.faces = []
      classifier = cv2.CascadeClassifier("./resource/haarcascade_frontalface_default.xml")

      imgGray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
      faces = classifier.detectMultiScale(imgGray, 1.2, 8)
      for (x,y,w,h) in faces:
         self.faces.append(Face(x,y,w,h))
      
   
   def getClosestFace(self):
      self.getFaces()
      if(len(self.faces) != 0):
         self.face = max(self.faces, key=lambda face: face.area)
      else:
         self.face = Face(0,0,0,0)
      

   def highlightFace(self):
      cv2.rectangle(self.img,(self.face.x, self.face.y), (self.face.x + self.face.w, self.face.y + self.face.h ), (255, 0, 0), 2)