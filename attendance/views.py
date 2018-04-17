from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from home.models import *
from .models import *
from django.contrib import messages
from home.templatetags import *
# Create your views here.

def add_attendance(request):
    # return HttpResponse("shubahm")
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)
    sectn_data = Sections.objects.get(name=faculty_data.section)
    content = { 'data': faculty_data, 'sectn_data': sectn_data }
    return render(request, 'dashboard/add_attendance.html', content)

def today_attendance(request):
    if request.method == 'POST':
        total_students = request.POST['total_studnt']
        student = ','.join(request.POST.getlist('present[]'))
        faculty_data = Facultys.objects.get(pk=request.session['faculty'])
        sectn_data = Sections.objects.get(name=faculty_data.section)
        add_attendance = sectn_data.daily_attendance_set.create(student=student, section=request.POST['section'], faculty=request.session['faculty'])
        add_attendance.save()
        # for student in request.POST.getlist('present[]'):
            # add_attendance = daily_attendance(student = student, section = request.POST['section'], faculty= request.session['faculty'])
            # check = add_attendance.save()
            # content_data = { student : student }
            # content.append(content_data)
        # if check:
        messages.success(request, 'Attendance Added Successfully.')
    return render(request, 'dashboard/add_attendance.html')

def view_attendance(request):
    if 'faculty' in request.session:
        faculty_data = Facultys.objects.get(pk = request.session['faculty'])
        section = Sections.objects.get(name=faculty_data.section)
        attendance_data = daily_attendance.objects.filter(faculty = faculty_data.pk, section = section.pk )
        content = {  'data': faculty_data, 'attendance_data' : attendance_data, 'section_data': section }
        return render(request, 'home/view_attendance.html', content)
    elif 'student' in request.session:
        student_data = Students.objects.get(pk=request.session['student'])
        section = Sections.objects.get(name=student_data.section)
        attendance_data = daily_attendance.objects.filter(section = section.pk )
        content = { 'attendance_data' : attendance_data, 'student_data': student_data, 'data':student_data }
    return render(request, 'home/view_attendance_studnt.html', content)
    # return render(request, 'dashboard/add_attendance.html')

def day_attendance(request, attendance_date):
    # return HttpResponse(attendance_date)
    if 'faculty' in request.session:
        faculty_data = Facultys.objects.get(pk = request.session['faculty'])
        section = Sections.objects.get(name=faculty_data.section)
        attendance_data = daily_attendance.objects.filter(faculty = faculty_data.pk, attendance_date = attendance_date )
        content = {  'data': faculty_data, 'attendance_data' : attendance_data, 'section_data': section }
        return render(request, 'attendance/day_attendance.html', content)
    # elif 'student' in request.session:
    #     student_data = Students.objects.get(pk=request.session['student'])
    #     section = Sections.objects.get(name=student_data.section)
    #     attendance_data = daily_attendance.objects.filter(section = section.pk )
    #     content = { 'attendance_data' : attendance_data }
    return render(request, 'attendance/day_attendance.html', content)

def student_profile(request, slug):
    # return HttpResponse(slug)
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)
    sectn_data = Sections.objects.get(name=faculty_data.section)
    studnt_data = Students.objects.get(slug=slug)
    attendance_data = daily_attendance.objects.filter(faculty=faculty_data.pk, section_id = sectn_data.pk)
    content = {'data': faculty_data, 'studnt_data':studnt_data, 'sectn_data': sectn_data, 'attendance_data':attendance_data}
    return render(request, 'attendance/student_profile.html', content)

def view_messages(request):
    if 'student' in request.session:
        student_data = Students.objects.get(pk=request.session['student'])
        section = Sections.objects.get(pk=student_data.section_id)
        faculty = Facultys.objects.get(section_id = section.pk)
        if request.method == 'POST':
            data = allmessages(message_text = request.POST['msg_txt'], m_from = request.session['student'], m_to = faculty.pk)
            check=data.save()
            messages.success(request, "Message sent Successfully.")
        messages_all = allmessages.objects.filter(m_to = request.session['student'], m_from = faculty.pk )
        content = { 'messages_all':messages_all, 'data':student_data }
        # return HttpResponse(request.POST['editor1'])
    elif 'faculty' in request.session:
        faculty = Facultys.objects.get(pk=request.session['faculty'])
        section = Sections.objects.get(pk=faculty.section_id)
        if request.method == 'POST':
            students = ','.join(request.POST.getlist('send_message[]'))
            data = allmessages(message_text=request.POST['msg_txt'], m_from=request.session['faculty'], m_to=students)
            check = data.save()
            messages.success(request, "Message sent Successfully.")
        messages_all = allmessages.objects.filter(m_from=request.session['faculty'])
        content = { 'messages_all':messages_all, 'data':faculty }
    return render(request, 'attendance/view_messages.html', content)

def recieved_messages(request):
    if 'faculty' in request.session:
        faculty = Facultys.objects.get(pk=request.session['faculty'])
        section = Sections.objects.get(pk=faculty.section_id)
        messages_all = allmessages.objects.filter(m_to=request.session['faculty'])
        content = {'messages_all': messages_all, 'data': faculty}
    return render(request, 'attendance/recieved_messages.html', content)

def new_faculty_message(request):
    if 'faculty' in request.session:
        faculty = Facultys.objects.get(pk=request.session['faculty'])
        section = Sections.objects.get(pk=faculty.section_id)
        student_data = Students.objects.filter(section_id = section.pk)
        # messages_all = allmessages.objects.filter(m_to=request.session['faculty'])
        content = {'data': faculty, 'student_data': student_data}
    return render(request, 'attendance/new_faculty_message.html', content)
