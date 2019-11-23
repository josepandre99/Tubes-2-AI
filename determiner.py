from clips import Environment,Symbol
from shape import ShapeDetector
import imutils
import cv2

def callRule (rule) :
    listRuleActivated.append(rule)

#Deteksi Gambar
image = cv2.imread("trap_rata_kiri.jpeg")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

thresh1,thresh2 = cv2.threshold(blurred, 210, 255, cv2.THRESH_BINARY_INV)

cnts = cv2.findContours(thresh2.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

c = cnts[0]
# for c in cnts:
M = cv2.moments(c)
cX = int((M["m10"] / M["m00"]) * ratio)
cY = int((M["m01"] / M["m00"]) * ratio)


# nAngle = banyak sudut
# list_angles = list besar sudut
# list_length = list panjang sisi
nAngle, list_angles, list_length = sd.detect(c)
#print(nAngle, list_angles, list_length)

list_facts = []

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
    
    ns = 6
    if (list_length[0] / list_length[1]) >= 0.5 and (list_length[0] / list_length[1]) <= 1.5 :
        ns-=1
    if (list_length[0] / list_length[2]) >= 0.5 and (list_length[0] / list_length[2]) <= 1.5 :
        ns-=1
    if (list_length[0] / list_length[3]) >= 0.5 and (list_length[0] / list_length[3]) <= 1.5 :
        ns-=1
    if (list_length[1] / list_length[2]) >= 0.5 and (list_length[1] / list_length[2]) <= 1.5 :
        ns-=1
    if (list_length[1] / list_length[3]) >= 0.5 and (list_length[1] / list_length[3]) <= 1.5 :
        ns-=1
    if (list_length[2] / list_length[3]) >= 0.5 and (list_length[2] / list_length[3]) <= 1.5 :
        ns-=1
    if ns == 0 :
        list_facts.append("(semua sisi sama)")

    if (list_length[0] / list_length[1]) >= 0.5 and (list_length[0] / list_length[1]) <= 1.5 :
        list_facts.append("(sisi 1 sama sisi 2)")    
        if (list_length[2] / list_length[3]) >= 0.5 and (list_length[2] / list_length[3]) <= 1.5 :
            list_facts.append("(sisi 3 sama sisi 4)")
        else:
            list_facts.append("(sisi 3 tidak sama sisi 4)")
    if (list_length[0] / list_length[2]) >= 0.5 and (list_length[0] / list_length[2]) <= 1.5 :
        list_facts.append("(sisi 1 sama sisi 2)")    
        if (list_length[1] / list_length[3]) >= 0.5 and (list_length[1] / list_length[3]) <= 1.5 :
            list_facts.append("(sisi 3 sama sisi 4)")
        else:
            list_facts.append("(sisi 3 tidak sama sisi 4)")
    if (list_length[0] / list_length[3]) >= 0.5 and (list_length[0] / list_length[3]) <= 1.5 :
        list_facts.append("(sisi 1 sama sisi 2)")    
        if (list_length[1] / list_length[2]) >= 0.5 and (list_length[1] / list_length[2]) <= 1.5 :
            list_facts.append("(sisi 3 sama sisi 4)")
        else:
            list_facts.append("(sisi 3 tidak sama sisi 4)")
    if (list_length[1] / list_length[2]) >= 0.5 and (list_length[1] / list_length[2]) <= 1.5 :
        list_facts.append("(sisi 1 sama sisi 2)")    
        if (list_length[0] / list_length[3]) >= 0.5 and (list_length[0] / list_length[3]) <= 1.5 :
            list_facts.append("(sisi 3 sama sisi 4)")
        else:
            list_facts.append("(sisi 3 tidak sama sisi 4)")
    if (list_length[1] / list_length[3]) >= 0.5 and (list_length[1] / list_length[3]) <= 1.5 :
        list_facts.append("(sisi 1 sama sisi 2)")    
        if (list_length[0] / list_length[2]) >= 0.5 and (list_length[0] / list_length[2]) <= 1.5 :
            list_facts.append("(sisi 3 sama sisi 4)")
        else:
            list_facts.append("(sisi 3 tidak sama sisi 4)")
    if (list_length[2] / list_length[3]) >= 0.5 and (list_length[2] / list_length[3]) <= 1.5 :
        list_facts.append("(sisi 1 sama sisi 2)")    
        if (list_length[0] / list_length[1]) >= 0.5 and (list_length[0] / list_length[1]) <= 1.5 :
            list_facts.append("(sisi 3 sama sisi 4)")
        else:
            list_facts.append("(sisi 3 tidak sama sisi 4)")

    if (list_angles[0] / list_angles[1]) >= 0.5 and (list_angles[0] / list_angles[1]) <= 1.5 :
        list_facts.append("(sudut 1 sama sudut 2)")    
        if list_angles[0] >= 85.5 and list_angles[0] <= 94.5 :
            list_facts.append("(sudut 1 sama 90)")    
        if (list_angles[2] / list_angles[3]) >= 0.5 and (list_angles[2] / list_angles[3]) <= 1.5 :
            list_facts.append("(sudut 3 sama sudut 4)")    
            if list_angles[2] >= 85.5 and list_angles[2] <= 94.5 :
                list_facts.append("(sudut 3 sama 90)") 
        else:
            list_facts.append("(sudut 3 tidak sama sudut 4)")
    if (list_angles[0] / list_angles[2]) >= 0.5 and (list_angles[0] / list_angles[2]) <= 1.5 :
        list_facts.append("(sudut 1 sama sudut 2)")    
        if list_angles[0] >= 85.5 and list_angles[0] <= 94.5 :
            list_facts.append("(sudut 1 sama 90)")
        if (list_angles[1] / list_angles[3]) >= 0.5 and (list_angles[1] / list_angles[3]) <= 1.5 :
            list_facts.append("(sudut 3 sama sudut 4)")
            if list_angles[1] >= 85.5 and list_angles[1] <= 94.5 :
                list_facts.append("(sudut 3 sama 90)") 
        else:
            list_facts.append("(sudut 3 tidak sama sudut 4)")
    if (list_angles[0] / list_angles[3]) >= 0.5 and (list_angles[0] / list_angles[3]) <= 1.5 :
        list_facts.append("(sudut 1 sama sudut 2)")    
        if list_angles[0] >= 85.5 and list_angles[0] <= 94.5 :
            list_facts.append("(sudut 1 sama 90)")
        if (list_angles[1] / list_angles[2]) >= 0.5 and (list_angles[1] / list_angles[2]) <= 1.5 :
            list_facts.append("(sudut 3 sama sudut 4)")
            if list_angles[1] >= 85.5 and list_angles[1] <= 94.5 :
                list_facts.append("(sudut 3 sama 90)") 
        else:
            list_facts.append("(sudut 3 tidak sama sudut 4)")
    if (list_angles[1] / list_angles[2]) >= 0.5 and (list_angles[1] / list_angles[2]) <= 1.5 :
        list_facts.append("(sudut 1 sama sudut 2)")    
        if list_angles[1] >= 85.5 and list_angles[1] <= 94.5 :
            list_facts.append("(sudut 1 sama 90)")
        if (list_angles[0] / list_angles[3]) >= 0.5 and (list_angles[0] / list_angles[3]) <= 1.5 :
            list_facts.append("(sudut 3 sama sudut 4)")
            if list_angles[0] >= 85.5 and list_angles[0] <= 94.5 :
                list_facts.append("(sudut 3 sama 90)") 
        else:
            list_facts.append("(sudut 3 tidak sama sudut 4)")
    if (list_angles[1] / list_angles[3]) >= 0.5 and (list_angles[1] / list_angles[3]) <= 1.5 :
        list_facts.append("(sudut 1 sama sudut 2)")
        if list_angles[1] >= 85.5 and list_angles[1] <= 94.5 :
            list_facts.append("(sudut 1 sama 90)")    
        if (list_angles[0] / list_angles[2]) >= 0.5 and (list_angles[0] / list_angles[2]) <= 1.5 :
            list_facts.append("(sudut 3 sama sudut 4)")
            if list_angles[0] >= 85.5 and list_angles[0] <= 94.5 :
                list_facts.append("(sudut 3 sama 90)") 
        else:
            list_facts.append("(sudut 3 tidak sama sudut 4)")
    if (list_angles[2] / list_angles[3]) >= 0.5 and (list_angles[2] / list_angles[3]) <= 1.5 :
        list_facts.append("(sudut 1 sama sudut 2)")
        if list_angles[2] >= 85.5 and list_angles[2] <= 94.5 :
            list_facts.append("(sudut 1 sama 90)")    
        if (list_angles[0] / list_angles[1]) >= 0.5 and (list_angles[0] / list_angles[1]) <= 1.5 :
            list_facts.append("(sudut 3 sama sudut 4)")
            if list_angles[0] >= 85.5 and list_angles[0] <= 94.5 :
                list_facts.append("(sudut 3 sama 90)") 
        else:
            list_facts.append("(sudut 3 tidak sama sudut 4)")

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
env = Environment()

#rule
env.load('rule.txt')
env.define_function(callRule)

#list of activated rule
listRuleActivated = []

#list of used fact
listFactsUsed = []

#fact
for fact in list_facts :
    #print(fact)
    facts = env.assert_string(fact)
    
env.run()

for f in env.facts() :
    listFactsUsed.append(f)

file.close()
