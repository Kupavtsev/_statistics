from django.contrib.messages.api import success
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

# from django.contrib.messages import constants as messages
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Customer
from .serializers import *
from .forms import CreateUserForm


# Create your views here.

@api_view(['POST',])      # Это открывает внешний доступ!!!!
def registerPageRest(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'success of register'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


def logoutUser(request):
    logout(request)
    return redirect('login')


