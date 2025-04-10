from django.shortcuts import render
from .models import Students,Contacts1

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
    
    saveObj=Contacts1(Name=name,Email=email,Subject=subject,Message=message)
    saveObj.save()

    return render(request,'contact_info.html',{'name':name,'email':email,'subject':subject,'message':message})


# def studentData(request):
#     studObj=Students.objects.get(id=1)
#     context={
#         'studObj':studObj,
#             }
#     return render(request,'student.html',context)
def studentData(request):
    studObj=Students.objects.all()
    context={
        'studObj':studObj,
            }
    return render(request,'student.html',context)

# def examData(request):
#     examObj=Exam1.objects.all()
#     context={
#         'examObj':examObj,
#             }
#     return render(request,'exam_result.html',context)

#--------------********************************-------------------******************----------------------------*********************---------------

def studentData(request):
    student_objects = Students.objects.all()

    # Add extra data to each student object (can use a list of dicts)
    processed_students = []

    for s in student_objects:
        total = s.physics + s.chemistry + s.math
        percent = total / 3
        # status = "Pass" if percent >= 40 else "Fail"
        if percent>=40:
            status="Pass"
        else:
            status="Fail"
        processed_students.append({
            'id': s.id,
            'name': s.studentName,
            'physics': s.physics,
            'chemistry': s.chemistry,
            'math': s.math,
            'total': total,
            'percent': round(percent, 2),
            'status': status
        })

    context = {
        'studObj': processed_students,
    }
    return render(request, 'Student.html', context)

#----------------------*************************------------------------***************************----------------------********************


def arithematicPage(request):
    return render(request,'arithematic.html')

def saveExamData(request):
    if request.method=="POST":
        rollNo=request.POST['rollno']
        name=request.POST['name']
        physics=request.POST['physics']
        chemistry=request.POST['chemistry']
        math=request.POST['maths']

        saveObj=Students(Roll_no=rollNo,studentName=name,physics=physics,chemistry=chemistry,math=math)
        saveObj.save()
        context={'msg':'Data saved Successfully'}
        return render(request,'arithematic.html',context)