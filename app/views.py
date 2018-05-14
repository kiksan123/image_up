from django.shortcuts import render,redirect
from .forms import PhotoForm
from .models import Photo
# Create your views here.
def index(request):
    context = {'images':Photo.objects.all()}
    return render(request, 'app/index.html', context)


def new(request):
    if request.method == 'GET':
        return render(request, 'app/new.html', {
            'form': PhotoForm(),
        })

def create(req):
    form = PhotoForm(req.POST, req.FILES)
    if not form.is_valid():
        raise ValueError('invalid form')

    photo = Photo()
    photo.image = form.cleaned_data['image']
    photo.save()

    return redirect('index')

def inputfrom(request):
	pass
