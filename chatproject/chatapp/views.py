from django.shortcuts import render
from .models import UserProfileInfo, User
from .forms import UserProfileInfoForm,UserForm
from .serializers import UserprofileSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse
from .forms import SignupForm

def index2(request):
    return render(request,'chatapp/index.html')

# def index(request):
#     return render(request, "build/index.html")
@csrf_exempt
@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index2'))
# Create your views here.

@api_view(["POST"])
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                message = 'Login successfull'
                res = message
                result={
                    'message': message,
                    'username':user.username,
                    'password':user.password,
                    'status code':200

                }
                return JsonResponse({'result':result})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            message = 'Invalid Login details'
            res = message
            result = {
                'message': message,
                'username': user.username,
                'password': user.password,
                'status code': 400

            }
            return JsonResponse({'result': result})

            # print("Someone tried to login and failed.")
            # print("They used username: {} and password: {}".format(username,password))
            # # return HttpResponse("Invalid login details given")

            # return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        # return render(request, 'chatapp/login.html', {})
        return Response(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST'])
def registration_view(request):

    registered= False
    if request.method == 'POST':
        print(request.data)
        form = SignupForm(request.POST)
        user = form
        # username = request.data.get('username')
        # email = request.data.get('email')
        # password = request.data.get('password1','password2')
        # user = authenticate(username=username,email=email, password1=password,password2=password)
        if form.is_valid():
            user = form.save()
            # current_site = get_current_site(request)
            message = 'Registered successfully'
            res = message
            result = {
                'message': message,
                'username': user.username,
                'eamil':user.email,
                'password1': user.password,
                'password2':user.password,
                'status code': 200
            }
            return JsonResponse({'result': result})
            registered = True

        else:
            message = 'Invalid Login details'
            res = message
            result = {
                'message': message,
                'username': user.username,
                'password': user.password,
                'status code': 400

            }
            return JsonResponse({'result': result})
            # print(form.errors)
    else:
        form = SignupForm()

    message = 'Invalid Credentials'
    res = message
    result = {
        'message': message,
        'username': user.username,
        'password': user.password,
        'status code': 400

    }
    return JsonResponse({'result': result})
    # return Response()
    # return render(request, 'chatapp/registration.html',
    #               {'user_form': user_form,
    #                'profile_form': profile_form,
    #                'registered': registered})

# This will return a list of books
# @api_view(["GET"])
# def book(request):
#     books = ["Pro Python", "Fluent Python", "Speaking javascript", "The Go programming language"]
#     return Response(status=status.HTTP_200_OK, data={"data": books})








