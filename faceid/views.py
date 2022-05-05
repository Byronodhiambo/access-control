from django.shortcuts import render
from .models import Image
from .serializer import Imageserializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import face_recognition
import cv2
# Create your views here.


class users(APIView):
    def get(self, request, format=None):
        image = Image.objects.all()
        serializer = Imageserializer(image, many=True)
        return Response(serializer.data)

    def get_object(self, request, pk, format=None):
        image = Image.object(pk)
        serializer = Imageserializer(image, many=True)
        return Response(serializer.data)   
    
    def post(self, request, format=None):
        serializer = Imageserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        Image = self.get_object(pk)
        serializer = Imageserializer(Image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Image = self.get_object(pk)
        Image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def captureimage():
    camera = cv2.VideoCapture(0)
    result, image = camera.read()
    if result:
        # cv2.imshow("your image", image)
        cv2.imwrite("unknown.png", image)
        # cv2.waitKey(0)
        # cv2.destroyWindow("your image")
        return 'unknown.png'
    else:
        print("No image detected. Please! try again")


def comparefaces():
    images = Image.objects.all()
    for image in images:
        known_image = face_recognition.load_image_file(image.photo)
        unknown_image = face_recognition.load_image_file(captureimage())

        try:
            biden_encoding = face_recognition.face_encodings(known_image)[0]
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
            print(results) 

        except:
            print("Face not detected try again")

# comparefaces(request="")



# captureimage(request="")    
# 

    

