from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication 
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from .models import StudentModel
from .serializers import StudentModelSerializer
from rest_framework import mixins
from rest_framework import generics

class StudentList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = StudentModel.objects.all()
    # serializer_class = StudentModelSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)