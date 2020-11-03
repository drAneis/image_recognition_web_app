
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .car_plate import get_license_plate, find_files
from .models import Allcourses






# Create your views here.
def Courses(request):
    ac=Allcourses.objects.all()
    template=loader.get_template('TechnicalCourses/Courses.html')
    context={
        'ac':ac,

    }
    return HttpResponse(template.render(context, request))

def upload_video(request):
    return render(request,'TechnicalCourses/up_video.html')




def upload_photo(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        print(name) #for debugging
        find_files(name, 'C://DB')

    return render(request, 'TechnicalCourses/detail.html')



