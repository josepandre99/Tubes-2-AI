from clips import Environment,Symbol
from shape import ShapeDetector
import imutils
import cv2


def callRule (rule) :
    global listRuleActivated

    listRuleActivated.append(rule)

def callFact (fact) :
    global listFactsUsed

    listFactsUsed.append(fact)

#Deteksi Gambar
def detectImage(img, nAngleCheck, list_angles, list_length):
    image = cv2.imread(img)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh1,thresh2 = cv2.threshold(blurred, 210, 255, cv2.THRESH_BINARY_INV)

    mean_c = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 12)
    gaus = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 12)
    cnts = cv2.findContours(thresh2.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()

    result = []
    for c in cnts:
        M = cv2.moments(c)

        # nAngle = banyak sudut
        # list_angles = list besar sudut
        # list_length = list panjang sisi
        nAngle, list_angles, list_length = sd.detect(c)
        #print(nAngle, list_angles, list_length)

        threshold_area = 1000
        area = cv2.contourArea(c)

        c = c.astype("float")
        c = c.astype("int")

        if (nAngleCheck == nAngle and area > threshold_area) :
            try :
                cX = int((M["m10"] / M["m00"]) )
                cY = int((M["m01"] / M["m00"]) )
            except :
                print("shape terlalu kecil")

            #print(nAngle, list_angles, list_length)
            # cv2.imshow("Imagegaus", mean_c)
            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            cv2.putText(image, "detect", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            status = cv2.imwrite("hasil.png", image)
            result.append((nAngle, list_angles, list_length))
        
    return result


def deter(list_facts, nAngle, list_angles, list_length):  
    if nAngle == 3 :
        list_facts.append("(total-point 3)")
        n = 3
        for angle in list_angles :
            if angle > 93 :
                list_facts.append("(sudut utama atas 90)")
                list_angles.remove(angle)
                if (list_angles[0] / list_angles[1]) >= 0.5 and (list_angles[0] / list_angles[1] <= 1.5) :
                    list_facts.append("(ada dua sudut sama)")
                else :
                    list_facts.append("(tidak ada dua sudut sama)")
                break

            elif angle >= 87 and angle <= 93 :
                list_facts.append("(sudut utama sama 90)")
                list_angles.remove(angle)
                if (list_angles[0] / list_angles[1]) >= 0.5 and (list_angles[0] / list_angles[1] <= 1.5) :
                    list_facts.append("(ada dua sudut sama)")
                else :
                    list_facts.append("(tidak ada dua sudut sama)")
                break

            else :
                n-=1

        if (n == 0) :
            m = 3
            list_facts.append("(sudut utama bawah 90)")
            for angle in list_angles :
                if angle >= 57 and angle <= 63 :
                    m-=1
            if m == 0 :
                list_facts.append("(semua sudut sama)")
            else :
                if (list_angles[0] / list_angles[1]) >= 0.5 and (list_angles[0] / list_angles[1] <= 1.5) :
                    list_facts.append("(ada dua sudut sama)")
                elif (list_angles[1] / list_angles[2]) >= 0.5 and (list_angles[1] / list_angles[2] <= 1.5) :
                    list_facts.append("(ada dua sudut sama)")
                elif (list_angles[0] / list_angles[2]) >= 0.5 and (list_angles[0] / list_angles[2] <= 1.5) :
                    list_facts.append("(ada dua sudut sama)")
                else :
                    list_facts.append("(tidak ada dua sudut sama)")

    elif nAngle == 4 :
        list_facts.append("(total-point 4)")
        n = 4
        for angle in list_angles :
            if angle >= 85.5 and angle <= 94.5 :
                n-=1
        if n == 0 :
            list_facts.append("(semua sudut sama)")
        else :
            if (list_angles[0] / list_angles[2] >= 0.5) and (list_angles[0] / list_angles[2] <= 1.5) :
                if (list_angles[1] / list_angles[3] >= 0.5) and (list_angles[1] / list_angles[3] <= 1.5) :
                    list_facts.append("(dua pasang sudut berhadapan sama)")
                else :
                    list_facts.append("(satu pasang sudut berhadapan sama)")
                    list_facts.append("(satu pasang sudut berhadapan tidak sama)")
            else :
                if (list_angles[1] / list_angles[3] >= 0.5) and (list_angles[1] / list_angles[3] <= 1.5) :
                    list_facts.append("(satu pasang sudut berhadapan sama)")
                    list_facts.append("(satu pasang sudut berhadapan tidak sama)")

            if (list_angles[0] / list_angles[1] >= 0.5) and (list_angles[0] / list_angles[1] <= 1.5) :
                if (list_angles[2] / list_angles[3] >= 0.5) and (list_angles[2] / list_angles[3] <= 1.5) :
                    list_facts.append("(dua pasang sudut bersebelahan sama)")
            elif (list_angles[0] / list_angles[3] >= 0.5) and (list_angles[0] / list_angles[3] <= 1.5) :
                if (list_angles[1] / list_angles[2] >= 0.5) and (list_angles[1] / list_angles[2] <= 1.5) :
                    list_facts.append("(dua pasang sudut bersebelahan sama)")

            if (list_angles[0] <= 94.5) and (list_angles[0] >= 85.5) :
                list_facts.append("(dua sudut kiri 90)")
            elif (list_angles[2] <= 94.5) and (list_angles[2] >= 85.5) :
                list_facts.append("(dua sudut kanan 90)")

        ns = 3
        if (list_length[0] / list_length[1]) >= 0.5 and (list_length[0] / list_length[1]) <= 1.5 :
            ns-=1
        if (list_length[0] / list_length[2]) >= 0.5 and (list_length[0] / list_length[2]) <= 1.5 :
            ns-=1
        if (list_length[0] / list_length[3]) >= 0.5 and (list_length[0] / list_length[3]) <= 1.5 :
            ns-=1
        if ns == 0 :
            list_facts.append("(semua sisi sama)")

    elif nAngle == 5 :
        list_facts.append("(total-point 5)")
        n = 5
        for angle in list_angles :
            if angle >= 102.6 and angle <= 113.4 :
                n-=1
        if n == 0 :
            list_facts.append("(semua sudut sama)")
        else :
            list_facts.append("(semua sudut tidak sama)")

    elif nAngle == 6 :
        list_facts.append("(total-point 6)")
        n = 6
        for angle in list_angles :
            if angle >= 144 and angle <= 126 :
                n-=1
        if n == 0 :
            list_facts.append("(semua sudut sama)")
        else :
            list_facts.append("(semua sudut tidak sama)")

#CLIPS
def callCLIPS(list_facts):

    env = Environment()

    #rule
    env.define_function(callRule)
    env.define_function(callFact)
    env.load('rule.txt')

    print(list_facts)
    #fact
    for fact in list_facts :
        env.assert_string(fact)

    env.run()


#Global Variable
#list of activated rule
listRuleActivated = []

#list of used fact
listFactsUsed = []

list_facts = []

def runProgram(image,angle):

    global listRuleActivated
    global listFactsUsed
    global list_facts 

    list_facts = []
    listFacts = []
    
    nAngleCheck = angle
    list_angles = []
    list_length = []
    contour_list = []

    contour_list = detectImage(image, nAngleCheck, list_angles, list_length)

    if (len(contour_list) != 0) :
        nAngle, list_angles, list_length = contour_list[0]
        deter(list_facts, nAngle, list_angles, list_length)
    
        callCLIPS(list_facts)

    return listRuleActivated, listFactsUsed
