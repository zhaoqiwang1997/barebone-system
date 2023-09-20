from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from datetime import date


# Create your views here.
def isAdult(birthday):
    age = (date.today() - birthday) // 365
    if age < 18:
        return False
    return True
@api_view(['GET', 'POST'])
def newUser(request):
    if 'username' in request.data:
        # check if the user already exists
        if not User.objects.filter(username=request.data['username']).exists():
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                # check age by birthday
                birthday = serializer.validated_data['birthday']
                if not isAdult(birthday):
                    return ("User must be at least 18 years old to register.")
                
                serializer.save()
                return ("User created")
    return Response('Username is required!')

@api_view(['POST'])
def logIn(request):
    if 'username' in request.data:
        user = User.objects.get(username=request.data['username'])
        serializer = UserSerializer(user)
        password = serializer.data['password']
        if password == request.data['password']:
            return ("Logged in successfully")
    return Response('Username is incorrect!')

@api_view(['POST'])
def updateUser(request):
    if 'username' in request.data:
        user = User.objects.get(username=request.data['username'])
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            # check age by birthday
            if 'birthday' in request.data:
                birthday = serializer.validated_data['birthday']
                if not isAdult(birthday):
                    return ("User must be at least 18 years old to register.")
            return ("Update successfully!")
    return ('Username is incorrect!')
