from shape import ShapeDetector
import imutils
import cv2


file_image = "trap_rata_kiri.jpeg"
nAngleCheck = 4

image = cv2.imread(file_image)
# resized = imutils.resize(image, width=100)
# ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

thresh1,thresh2 = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY_INV)

# # Tambahan
mean_c = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 12)

gaus = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 12)

# cnts = cv2.findContours(mean_c.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# # -----


cnts = cv2.findContours(mean_c.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

# cv2.imshow("Image", gaus)
# cv2.waitKey(0)

# c = cnts[0]
for c in cnts:
    M = cv2.moments(c)
    

    # nAngle = banyak sudut
    # list_angles = list besar sudut
    # list_length = list panjang sisi
    nAngle, list_angles, list_length = sd.detect(c)
    # print(nAngle, list_angles, list_length)

    threshold_area = 1000
    area = cv2.contourArea(c)

    # cv2.imshow("Image", image)
    # cv2.waitKey(0)
    # print(area)

    c = c.astype("float")
    # c *= ratio
    c = c.astype("int")
    if (nAngleCheck == nAngle and area > threshold_area) :
        try :
            cX = int((M["m10"] / M["m00"]) )
            cY = int((M["m01"] / M["m00"]) )
        except :
            print("shape terlalu kecil")

        print(nAngle, list_angles, list_length)
        # cv2.imshow("Imagegaus", mean_c)
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.putText(image, "detect", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.imshow("Image", image)
        cv2.waitKey(0)

cv2.destroyAllWindows()