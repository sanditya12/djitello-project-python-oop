class Face:
   def __init__(self,x,y,w,h):
      self.x = x
      self.y = y
      self.w = w
      self.h = h
      self.area = w*h
      self.cx = (x+w)//2
      self.cy = (y+h)//2