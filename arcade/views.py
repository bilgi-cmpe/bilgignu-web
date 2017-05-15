from django.shortcuts import render

def arcades(request):
    return render(request, 'arcade/arcade.html')
