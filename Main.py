
from Vision import Vision
from djitellopy import tello
import cv2

# drone = tello.Tello()
# drone.connect()
# drone.streamon()

vision = Vision()
vision.setWebcam(0)


prevError =0

while True:
   vision.getImg()
   vision.getClosestFace()
   vision.highlightFace()
   
   fb, fbStatus = vision.getFbVelocity()

   vision.setPid(0.4,0.4,0)
   yaw, prevError, yawStatus = vision.getYawVelocity(prevError)
   vision.addText(fbStatus+" , "+yawStatus+" , "+str(drone.get_battery()),(108, 173, 88))
   
   # drone.send_rc_control(0,fb,0,yaw)

   vision.stream()
   key = cv2.waitKey(1) & 0xff
   # if key == 27: # ESC
   #    break
   # elif key == ord('w'):
   #   drone.takeoff()
   # # elif key == ord('s'):
   # #    tello.move_back(30)
   # elif key == ord('a'):
   #    drone.move_left(30)
   # elif key == ord('d'):
   #    drone.move_right(30)
   # # elif key == ord('e'):
   # #    drone.rotate_clockwise(30)
   # # elif key == ord('q'):
   # #    drone.rotate_counter_clockwise(30)
   # elif key == ord('r'):
   #    drone.move_up(30)
   # elif key == ord('f'):
   #    drone.move_down(30)

# drone.land()