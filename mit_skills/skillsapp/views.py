from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Member
from .models import Skillsmatrix
from .models import SkillSet

# Create your views here.

skills_Category=''
skills_Name=''
proficiency=''
Is_Trained=''
total_experience=''
Is_Certified=''
certifications=''
assessment_date=''


def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'index.html')

def login_request(request):
    global username
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                member=Member(
                    username=username
                )
                member.save()
                messages.info(request, "You are now logged in as {username}")
                skill=Skillsmatrix.objects.filter(username=username)
                sklist=SkillSet.objects.all()
                context={ 'skill':skill,
                       'sklist':sklist}
                return render(request,'home.html',context)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form}) 

def home(request):
    global conn
    global username
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            print('pass')
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            skill=Skillsmatrix.objects.filter(username=username)
            sklist=SkillSet.objects.all()
            context={ 'skill':skill,
                      'sklist':sklist }
            return render(request, 'home.html',context)
        else:
            print('fail')
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)
        
    if request.method== 'GET':
        skill=Skillsmatrix.objects.filter(username=username)
        sklist=SkillSet.objects.all()
        context={ 'skill':skill,
                  'sklist':sklist}
        return render(request, 'home.html',context)

    

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")

    return render(request, 'login.html')

def add(request):
    global username
    
    if request.method == 'POST':
        VSkills_Name=request.POST.get('tSkills_Name')
        Skills_Nameobj=SkillSet.objects.get(Skills_Name=VSkills_Name)
        proficiency=request.POST.get('tproficiency')
        Is_Trained=request.POST.get('tIs_Trained')
        Is_Certified=request.POST.get('tIs_Certified')
        total_experience=request.POST.get('ttotal_experience')
        certifications=request.POST.get('tcertifications')
        certified_date=request.POST.get('tcertified_date')
        training_name=request.POST.get('ttraining_name')
        usernameobj=Member.objects.get(username=username)
        skill=Skillsmatrix(
             
            proficiency=proficiency,
            Is_Trained=Is_Trained,
            Is_Certified=Is_Certified,
            total_experience=total_experience,
            certifications=certifications, 
            certified_date=certified_date,
            training_name=training_name,
            username=usernameobj,
            Skills_Name=Skills_Nameobj)
        skill.save()
        return redirect('home')
    return render(request,'home.html')

def edit(request):
    skill=Skillsmatrix.objects.filter(username=username)
    context={
        'skill':skill,
    }
    return render(request,'home.html',context)

def update(request):
    if request.method=="POST":
        id=request.POST.get('tid')
        VSkills_Name=request.POST.get('tSkills_Name')
        Skills_Nameobj=SkillSet.objects.get(Skills_Name=VSkills_Name)
        proficiency=request.POST.get('tproficiency')
        Is_Trained=request.POST.get('tIs_Trained')
        Is_Certified=request.POST.get('tIs_Certified')
        total_experience=request.POST.get('ttotal_experience')
        certifications=request.POST.get('tcertifications')
        certified_date=request.POST.get('tcertified_date')
        training_name=request.POST.get('ttraining_name')
        #created_Date=Skillsmatrix.objects.filter(id=id)
        usernameobj=Member.objects.get(username=username)
        
        

        skill=Skillsmatrix(
            id=id,
            proficiency=proficiency,
            Is_Trained=Is_Trained,
            Is_Certified=Is_Certified,
            total_experience=total_experience,
            certifications=certifications, 
            certified_date=certified_date,
            training_name=training_name,
            username=usernameobj,
            Skills_Name=Skills_Nameobj,
            
            )
        
        skill.save()

        return redirect('home')
    
    return redirect(request,'home.html')

def delete(request):
    if request.method== "GET":
        vid=request.GET.get('tid')
        print(vid)
        skill=Skillsmatrix.objects.filter(id=vid)
        skill.delete()
        return redirect('home')
    
    skill=Skillsmatrix.objects.all()
    context={
       'skill':skill
    }
    return render(request,'home.html',context)
  
# SKILLS LIST AVAILABLE VIEW

def show_skill_Category(request):
    results=SkillSet.objects.all()
    return render(request,"home.html",{"show_skill_cat":results})
