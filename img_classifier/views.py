from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
            prediction_label, prediction_value = classify_image(new_img.image.url)
            Image.objects.filter(pk=pk).update(prediction_label=prediction_label)
            Image.objects.filter(pk=pk).update(prediction_value=prediction_value)

        return redirect(request.path)
    else:
        form = ImageForm()
        image_list = Image.objects.all().order_by('-id')
        context = {'form': form, 'images': images}
    return render(request, 'img_classifier/index.html', context)
