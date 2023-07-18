from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


def home(request):
    return render(request, 'Upload/home.html')


def download(request,uid):
    return render(request, 'Upload/download.html', context={'uid': uid})


class Handle_Upload(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            data = request.data

            file_ser = Filelist_serializer(data=data)

            if file_ser.is_valid():
                file_ser.save()
                return Response({
                    'status': 200,
                    'message': 'files uploaded successfully',
                    'data': file_ser.data
                })

            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data': file_ser.errors
            })
        except Exception as e:
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': str(e)
            })
