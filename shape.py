import cv2


class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):
        shape = 0
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        if len(approx) == 3:
            shape = "Triangle"

        elif len(approx) == 4:
            shape = "Rectangle"

        elif len(approx) == 5:
            shape = "Pentagon"

        elif len(approx) == 6:
            shape = "Hexagon"

        else:
            shape = "Circle"

        
        return shape