from django.shortcuts import render
from .models import Students

# # Create your views here.
def index(request):
    return render(request,'index.html')


 


def sal(request):
    a=float(request.GET['rvalue'])
    b=float(request.GET['salval'])
    total=0
    if a>=1 and a<=3:
        total=b*0.1
    elif a>=3.1 and a<=4:
        total=b*0.2
    else :
        total=b*0.3

    return render(request,'salary_result.html',{'sal':total,'rate':a,'original':b})

def con(request):
    name=request.POST['name']
    email=request.POST['email']
    subject=request.POST['subject']
    message=request.POST['message']

    return render(request,'contact_info.html',{'name':name,'email':email,'subject':subject,'message':message})


def studentData(request):
    studObj=Students.objects.get(id=1)
    context={
        'studObj':studObj,
            }
    return render(request,'student.html',context)

