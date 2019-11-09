import cv2
import math


class ShapeDetector:
    def __init__(self):
        pass

    def getLength(self, p, q):
        return (math.sqrt((q[0]-p[0])**2+(q[1]-p[1])**2))


    def getAngle(self, a, b, c):
        ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
        return ang + 360 if ang < 0 else ang  

    def detect(self, c):
        shape = 0
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        nAngles = len(approx)

        list_angles = []
        for i in range(0, nAngles):
            list_angles.append(self.getAngle(approx[(i-1)%nAngles][0] , approx[i][0], approx[(i+1)%nAngles][0]))
        

        list_length = []
        for j in range(0, nAngles):
            list_length.append(self.getLength(approx[j][0], approx[(j+1)%nAngles][0]))

        return nAngles, list_angles, list_length