from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.contrib import messages
from django.views import generic
import datetime
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

def index(request):
    if request.method == 'POST':
        try:
            faculty_data = Facultys.objects.get(email = request.POST['email'])
            if faculty_data:
                if faculty_data.password == request.POST['password']:
                    request.session['faculty'] = faculty_data.pk
                    content = {
                        'data': faculty_data
                    }
                    # messages.add_message(request, messages.INFO, 'Logged in Successfully')
                    messages.success(request, 'Logged in Successfully')
                    response = HttpResponseRedirect(reverse('home:dashboard'))
                    response.set_cookie('name', "Shubham")
                    return response
                    # return HttpResponseRedirect('/dashboard', content)
        # render(request, 'home/faculty_dashboard.html', content)
                else:
                    content = {
                    'data': faculty_data
                    }
                    # messages.add_message(request, messages.ERROR, 'No match Wrong Password.')
                    messages.error(request, 'Sorry, either of your provided information is wrong.')
                    return render(request, 'home/home.html', content)
        except ObjectDoesNotExist:
            return render(request, 'home/home.html')
    else:
        return render(request, 'home/home.html')

def student_login(request):
    if request.method == 'POST':
        try:
            studnt_data = Students.objects.get(roll_no = request.POST['univ_rlno'])
            if studnt_data:
                if studnt_data.name == request.POST['name']:
                    request.session['student'] = studnt_data.pk
                    # content = {
                    #     'data': faculty_data
                    # }
                    messages.success(request, 'Logged in Successfully')
                    return HttpResponseRedirect(reverse('home:dashboard'))
        # render(request, 'home/faculty_dashboard.html', content)
                else:
                    messages.error(request, 'Sorry, either of your provided information is wrong.')
                    return HttpResponseRedirect(reverse('home:index'))
                    # return render(request, 'home/login.html', content)
        except ObjectDoesNotExist:
            messages.error(request, 'User does not exist.')
            return HttpResponseRedirect(reverse('home:index'))
    else:
        return render(request, 'home/login.html')

def dashboard_faculty(request):
    if 'faculty' in request.session:
        sessn_val = request.session['faculty']
        faculty_data = Facultys.objects.get(pk=sessn_val)
        sectn_data = Sections.objects.get(name=faculty_data.section)
        content = {'data': faculty_data, 'sectn_data': sectn_data}
        return render(request, 'home/view_students.html', content)
    elif 'student' in request.session:
        sessn_val = request.session['student']
        student_data = Students.objects.get(pk=sessn_val)
        sectn_data = Sections.objects.get(name=student_data.section)
        content = {'data': student_data, 'sectn_data': sectn_data}
        return render(request, 'home/student_info.html', content)
        # return HttpResponse(sectn_data)

def add_student(request):
    content={}
    if request.method == 'POST':
        faculty_data = Facultys.objects.get(pk=request.POST['id_faculty'])
        sectn_data = Sections.objects.get(name=faculty_data.section)
        stdnt = sectn_data.students_set.create(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone_no'], gender=request.POST['gender'], mother_name=request.POST['mother_name'])
        chek = stdnt.save()
        today = datetime.datetime.now()
        get_lastid = Students.objects.latest('id')
        set_roll_no = sectn_data.name + str(today.year) + str(get_lastid.id)
        student_data = Students.objects.get(id=get_lastid.id)
        student_data.roll_no = set_roll_no
        check1 = student_data.save()
        if get_lastid:
            messages.success(request, "Student Added Successfully")
        else:
            messages.error(request, "Error in adding student")
    # return HttpResponseRedirect('/dashboard', content)
    return HttpResponseRedirect(reverse('home:dashboard'))

def logout(request):
    try:
        if 'faculty' in request.session:
            del request.session['faculty']
        elif 'student' in request.session:
            del request.session['student']
        # return HttpResponseRedirect(reverse('home:index', {
        #     'error_note': 'Logged out Successfully'
        # }))
        messages.success(request, "Logged Out Successfully")
        return HttpResponseRedirect(reverse('home:index'))

    except:
        messages.error(request, "Error in logging Out")
        return HttpResponseRedirect(reverse('home:index'))