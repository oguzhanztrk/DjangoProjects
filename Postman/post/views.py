from django.contrib.sites import requests
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import  mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import  Response
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_204_NO_CONTENT,HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Post,Comment
from .serializers import PostSerializer,OwnerSerializer,CommentSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser

User = get_user_model()
import requests

@csrf_exempt
def my_django_view(request):
    if request.method == 'POST':
        r = requests.post("http://127.0.0.1:8000/api/posts/",post.object)
        print(r)
    else:
        r = requests.get("http://127.0.0.1:8000/api/posts/", custom_id=request.GET)
        print(r)

    if r.status_code == 200:
        return HttpResponse('Yay, it worked')
    return HttpResponse('Could not save data')


class PostView(APIView):
    permission_classes = (AllowAny, )

    def get (self,request,*args,**kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        #if serializer.is_valid():
        return redirect("http://127.0.0.1:8000/api/posts/")

        #print(Post.objects.values())
        #r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

        #return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        return redirect("http://127.0.0.1:8000/api/posts/")

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            #return Response({"message":"some message"},status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

    def put(self, request,pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)