import cv2
from Face import Face

class Vision:
   def __init__(self):
      self.capturedImage=None
      self.img= None
      self.source= ""
      self.faces = []
      self.face = Face(0,0,0,0)
      self.wFrame= 360
      self.hFrame= 240
      self.faceAreaThreshold= [6000,8000]
      self.fb = 20
      self.pid=[]
      self.drone=None

   def setWebcam(self, webcam):
      self.capturedImage = cv2.VideoCapture(webcam)
      self.source = "Webcam"
   
   def setDrone(self,drone):
      self.drone = drone
      self.source = "Drone"

   def getImg(self):
      if self.source == "Webcam":
         _,self.img = self.capturedImage.read()
         self.img = cv2.resize(self.img,(360 ,240))
      if self.source =="Drone":
         self.img = self.drone.get_frame_read().frame
         self.img = cv2.resize(self.img, (360,240))

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

   def addText(self, text, color):
      cv2.putText(self.img, text, (5,25), cv2.FONT_HERSHEY_TRIPLEX, 1,color,2)

   def setPid(self, kp, kd, ki):
      self.pid = (kp,kd,ki)

   def getFbVelocity(self):
      area = self.face.area
      if (area>self.faceAreaThreshold[0] and area<self.faceAreaThreshold[1]):
         return 0, "STAY"
      elif (area>self.faceAreaThreshold[1]):
         return -self.fb, "BACKWARD"
      elif (area<self.faceAreaThreshold[0] and area!=0):
         return self.fb,"FORWARD"
      return 0, "STAY"
 
   def getYawVelocity(self, prevError):
      cx = self.face.cx
      error = cx - (112)
      yaw = self.pid[0]*error+self.pid[1]*(error-prevError)

      if cx == 0:
         error=0
         yaw =0

      if yaw > 0:
         yawStatus = "RIGHT"
      elif yaw < 0:  
         yawStatus = "LEFT"
      else:
         yawStatus = "STAY"
      return yaw, error, yawStatus




      
