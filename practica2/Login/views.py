from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework import generics

from Login.models import User
from Login.serializer import UserSerializers





class CustonAuthToken(ObtainAuthToken):
    
    def post(self, request, * args, **kwars):
        serializer = self.serializer_class (data = request.data, 
                                            context = {
                                                    'request': request, 
                                                    }
                                            )
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })


class UserList2(APIView):
    #metodo get para solicitud
    def get(self, request, format = None):
        print ("metodo get filter")
        queryset = User.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = UserSerializers(queryset, many= True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = UserSerializers(data = request.data)
        if serializer .is_valid():
            serializer.save()
            data =  serializer.data
            return Response(data)
        return Response(serializer.errors , status = status.Http_400_BAD_REQUEST)

