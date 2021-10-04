def face_from_camera():
    import cv2 as cv

    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

    cap = cv.VideoCapture(1)

    while True:
        success, img = cap.read()

        # img = cv.imread('face2.jpeg')
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

        for(x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (0, 255 ,0), 2)

        cv.imshow('Face', img)
        if cv.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()