from .models import student,subject
from .serializers import studentSerializers



from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.


def welcome(request):
    return Response({
        'data':'welcome'
    })


class studentListView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        title=request.query_params.get('title')
        print(title)
        if title is not None:
            Students=student.objects.filter(name__icontains=title)
        else:
            Students=student.objects.all()
        serializer=studentSerializers(Students,many=True)
        return Response(serializer.data)



