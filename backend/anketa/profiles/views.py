from django.shortcuts import render, redirect
from .forms import UserProfileCreationForm
from django.contrib.auth import login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserProfileRegistrationSerializer


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserProfileRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход после регистрации
            return redirect('home')  # Переход на главную страницу
    else:
        form = UserProfileCreationForm()

    return render(request, 'register.html', {'form': form})
