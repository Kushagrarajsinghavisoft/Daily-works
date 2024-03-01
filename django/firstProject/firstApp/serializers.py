from rest_framework import serializers
from firstApp.models import Student

#created serializer for the Student model
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student      #telling selializer the model is Student
        fields=['id','name','score']   #telling serializer about the fields