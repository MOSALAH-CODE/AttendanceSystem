import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def detectIdInfo(src):
    img = cv2.imread(src)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(pytesseract.image_to_string(img))

    # Detecting Words
    boxes = pytesseract.image_to_data(img)
    data = []
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            # print(b)
            if len(b) == 12:
                if len(b[11]) == 11 and b[11].isdigit():
                    data.append(b[11])
                if len(b[11]) > 25:
                    data.append(b[11])
                # Draw rectangles on detected text
                # x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                # cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 3)
                # print(b[11], len(b[11])) # Print all detected words
                # Write detected words on image
                # cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 50, 50), 1)

    # print(data)
    idInfo = []
    if len(data) == 4:
        tc = data[0]
        name = data[3].split('<', 1)
        lastName = name[0]
        firstName = re.findall("[A-Z]+", name[1])
        year = data[2][0:2]
        month = data[2][2:4]
        day = data[2][4:6]
        if int(year) > 23:
            birthday = day + "-" + month + "-19" + year
        else:
            birthday = day + "-" + month + "-20" + year
        sex = data[2][7]
        idInfo = [tc, firstName, lastName, birthday, sex]

    # Show image
    # cv2.imshow("Result", img)
    # cv2.waitKey(0)

    return idInfo


print(detectIdInfo('Images/12345678901.png'))
print(detectIdInfo('Images/82345678902.png'))
print(detectIdInfo('Images/1.png'))
