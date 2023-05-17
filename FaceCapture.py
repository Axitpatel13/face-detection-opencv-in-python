import cv2

face_classifier = cv2.CascadeClassifier(
    'haarcascade/haarcascade_frontalface_default.xml'
)
def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,3)
    if faces == ():
        return None
    print(faces)
    for x,y,w,h in faces:
        cropped_faces = img[y: y+h, x: x+w]
        print(cropped_faces)
        return cropped_faces
cam = cv2.VideoCapture(0)
count = 0
while True:
    ret, frame = cam.read()
    if count == 100:
        break
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame),(300,300))
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        file_name_path = 'faces/faces' + str(count) + '.jpg'
        cv2.imwrite(file_name_path,face)
        cv2.putText(
            face, str(count),(70,70), cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,0),2
        )
        cv2.imshow('face Crop',face)
    else:
        print('No face found')
        pass
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()