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

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^student_login/$', views.student_login, name="student_login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^dashboard/$', views.dashboard_faculty, name="dashboard"),
    # url(r'^dashboard/$', views.dashboard_student, name="dashboard_student"),
    url(r'^add_student/$', views.add_student, name="add_student"),
    # url(r'^login_check/$', views.login_check, name="login_check"),
]
