from django.shortcuts import render
import face_recognition
import cv2
# Create your views here.


def comparefaces(request):
    known_image = face_recognition.load_image_file("biden.png")
    unknown_image = face_recognition.load_image_file("unknown.png")

    try:
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
        print(results)

    except:
        print("Face not detected try again")
   

# comparefaces(request="")

def captureimage(request):
    camera = cv2.VideoCapture(0)
    result, image = camera.read()
    if result:
        cv2.imshow("your image", image)
        cv2.imwrite("unknown.png", image)
        cv2.waitKey(0)
        cv2.destroyWindow("your image")
    else:
        print("No image detected. Please! try again")

# captureimage(request="")    
# 

    

