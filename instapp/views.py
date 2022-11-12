from django.shortcuts import render
from .models import coursedata, user_course_data
from .models import feedback_data

# Create your views here.

def homepage(request):
   
    return render(request,'instapp/homepage.html')


def contactpage(request):
    if request.method=='GET':
        return render(request,'instapp/contactpage.html')
    else:
        user_course_data(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            course=request.POST.get('course')

        ).save()
        return render(request,'instapp/contactpage.html')



def servicepage(request):
    serve=coursedata.objects.all()
    return render(request,'instapp/servicepage.html',{'serve':serve})


def feedbackpage(request):
    if request.method=='GET':
        feedbk=feedback_data.objects.all().values()
        return render(request,'instapp/feedbackpage.html',{'feedbk':feedbk})
    else:
        feedback_data(
            name=request.POST.get('name'),
            ratings=request.POST.get('ratings'),
            comments=request.POST.get('comments')
        ).save()
        feedbk=feedback_data.objects.all().values()
        return render(request,'instapp/feedbackpage.html',{'feedbk':feedbk})



def gallerypage(request):
   
    return render(request,'instapp/gallerypage.html')




