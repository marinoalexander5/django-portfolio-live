from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'jsprojects/main.html')

def bg_color(request):
    return render(request, 'jsprojects/bg-color.html')

def bg_video(request):
    return render(request, 'jsprojects/bg-video.html')