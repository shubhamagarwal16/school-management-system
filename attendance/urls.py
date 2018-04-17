"""attendance_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'attendance'
urlpatterns = [
    url(r'^student_profile/(?P<slug>.*)/$', views.student_profile, name="student_profile"),
    url(r'^add_attendance/$', views.add_attendance, name="add_attendance"),
    url(r'^today_attendance/$', views.today_attendance, name="today_attendance"),
    url(r'^view_attendance/$', views.view_attendance, name="view_attendance"),
    url(r'^day_attendance/(?P<attendance_date>.*)/$', views.day_attendance, name="day_attendance"),
    url(r'^view_messages/$', views.view_messages, name="view_messages"),
    url(r'^new_message/$', views.new_faculty_message, name="new_faculty_message"),
    url(r'^recieved_messages/$', views.recieved_messages, name="recieved_messages"),
    # url(r'^login_check/$', views.login_check, name="login_check"),
]
