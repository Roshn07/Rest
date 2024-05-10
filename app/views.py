from django.shortcuts import render
# Create your views here.


from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from .models import students
from .serializers import studentsSerializers
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class RecipeViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=students.objects.all()
    serializer_class=studentsSerializers

class StudentListView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        title=request.query_params.get('title')
        print(title)
        if title is not None:
            recipes=students.objects.filter(title_icontains=title)
        else:
            recipes=students.objects.all()
        serializer=studentsSerializers(recipes,many=True)
        return Response(serializer.data)
    

class RecipeDetailView(APIView):
    def get(self,request):
        return Response({})


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def hello(request):
    return Response({
        'data':"Hello World"
    })


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def list_students(request):
    if request.method == "POST":
        print(request.data)
        students_serializer = studentsSerializers(data=request.data)
        if students_serializer.is_valid(raise_exception=True):
            students_serializer.save(user=request.user)
            return Response(students_serializer.data,status=201)
        else:
            print(students_serializer.errors)
            return Response(students_serializer.errors)
       
        
    else:
        studentss = students.objects.all()
        serializer = studentsSerializers(studentss,many=True)
        response_data = serializer.data
        return Response(response_data)


@api_view(['GET','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def students_detail(request,id):

    try:
        student = students.objects.get(id=id)
    except student.DoesNotExist:
        return Response(data={"detail":"Requested students doesn't exist"},status=404)
    
    if request.method == "GET":
        student = students.objects.get(id=id)
        students_serializer = studentsSerializers(student)
        return Response(students_serializer.data)
    
    elif request.method =="PUT":
        student = students.objects.get(id=id)
        students_serializer = studentsSerializers(student,data=request.data)
        if students_serializer.is_valid():
            students_serializer.save(updatedBy=request.user)
            return Response(students_serializer.data)
        else:
            return Response(students_serializer.errors)

    elif request.method == "DELETE" :
        student = students.objects.get(id=id)
        student.delete()
        return Response(status=204)
