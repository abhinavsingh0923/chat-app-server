from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

class allstudents(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        student_obj = student.objects.all()
        serializers=StudentSerailizer(student_obj, many=True)
        return Response({'status':status.HTTP_200_OK, 'data':serializers.data})
    

    def post(self,request):
        try:
            data=request.data
            serializer=StudentSerailizer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':status.HTTP_201_CREATED,'message':'blog is successfully created','data':serializer.data})
        except Exception as e :
            return Response({'status':status.HTTP_204_NO_CONTENT,'message':e,})