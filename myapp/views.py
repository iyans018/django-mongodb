from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import TodosSerializer
from .models import Todos

# Create your views here.
@api_view(['POST'])
def createTodos(request):
  # serializer_context = {
  #   'request': Request(request),
  # }
  serializer = TodosSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  
  return Response(serializer.data)
  # try:
  #   if serializer.is_valid():
  #     serializer.save()
  #     return Response(serializer.data)
  # except:
  #   return JsonResponse({
  #     'message': 'terjadi kesalahan',
  #   })
