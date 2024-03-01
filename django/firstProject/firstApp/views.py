from django.shortcuts import render
from firstApp.models import Student
from firstApp.serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def Student_list(request):
    if request.method=='GET':
        students=Student.objects.all()    #creating object of all Student 
        serializer=StudentSerializers(students,many=True)    #here we are getting all objects of student and on that basis 
                                                             #we are creating serializer
        return Response(serializer.data)

    if request.method=='POST':
        serializer=StudentSerializers(data=request.data)    #here we are getting the single data and on that basis 
                                                            #we are creating serializer
        if serializer.is_valid():    #checking the data received from the post request
            serializer.save()        #saving the data received from post method
            return Response(serializer.data,status=status.HTTP_201_CREATED)     #sending data as a response and showing the status accordingly
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def Student_details(request,id):
    try:
        student=Student.objects.get(id=id)      #creating object on the basis of a particular Student id
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=StudentSerializers(student)   #creating serializer on the basis of the id given
        return Response(serializer.data)         #sending back the data of the serializer created above
    elif request.method=='PUT':
        serializer=StudentSerializers(student,data=request.data)
        if serializer.is_valid():     #checking the data received from the post request
            serializer.save()         #saving the data received from post method
            return Response(serializer.data)     #sending data as a response
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)
    elif request.method=='DELETE':
        student.delete()        #deleting the data requested
        return Response(status=status.HTTP_204_NO_CONTENT)