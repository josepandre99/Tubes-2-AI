import cv2
import math


class ShapeDetector:
    def __init__(self):
        pass

    # Fungsi mencari panjang sisi   
    def getLength(self, p, q):
        return (math.sqrt((q[0]-p[0])**2+(q[1]-p[1])**2))

    # Fungsi mencari besar sudut
    def getAngle(self, a, b, c):
        ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
        return ang + 360 if ang < 0 else ang  


    def detect(self, c):
        shape = 0
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        # Banyaknya sudut
        nAngles = len(approx)

        # Membuat list besar sudut
        list_angles = []
        for i in range(0, nAngles):
            list_angles.append(self.getAngle(approx[(i+1)%nAngles][0] , approx[i][0], approx[(i-1)%nAngles][0]))

        # handle error angles
        sum_angle = 0
        for k in range(0, nAngles):
            sum_angle += list_angles[k]
        # Segitiga
        if (nAngles == 3):
            if(sum_angle > 189):
                list_angles = []
                for i in range(0, nAngles):
                    list_angles.append(self.getAngle(approx[(i-1)%nAngles][0] , approx[i][0], approx[(i+1)%nAngles][0]))    
        # Segiempat
        if (nAngles == 4):
            if(sum_angle > 378):
                list_angles = []
                for i in range(0, nAngles):
                    list_angles.append(self.getAngle(approx[(i-1)%nAngles][0] , approx[i][0], approx[(i+1)%nAngles][0]))
        # Segilima
        if (nAngles == 5):
            if(sum_angle > 567):
                list_angles = []
                for i in range(0, nAngles):
                    list_angles.append(self.getAngle(approx[(i-1)%nAngles][0] , approx[i][0], approx[(i+1)%nAngles][0]))
        # Segienam
        if (nAngles == 6):
            if(sum_angle > 756):
                list_angles = []
                for i in range(0, nAngles):
                    list_angles.append(self.getAngle(approx[(i-1)%nAngles][0] , approx[i][0], approx[(i+1)%nAngles][0]))

        # Membuat list panjang sisi
        list_length = []
        for j in range(0, nAngles):
            list_length.append(self.getLength(approx[j][0], approx[(j+1)%nAngles][0]))

        # Return semua data
        return nAngles, list_angles, list_length