from django.shortcuts import render, redirect
from .utils import classify_image
from django.core.files.storage import default_storage
from .forms import ImageForm
from .models import Image
import os

# Create your views here.
def index(request):
    if request.method == "POST":                
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_img = form.save()
            pk = new_img.pk
            #for development, fix for production
            prediction = classify_image(os.path.join('media','img_classifier', os.path.basename(new_img.image.name)))
            Image.objects.filter(pk=pk).update(prediction=prediction)

        return redirect('img_classifier/index.html')
    else:
        form = ImageForm()
        images = Image.objects.all()
        context = {'form': form, 'images': images}
    return render(request, 'img_classifier/index.html', context)

def ImageListView():
    pass