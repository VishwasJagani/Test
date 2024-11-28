
from django.urls import path , include
from .views import *

urlpatterns = [

    path('',student_view , name="student_view"),
    path('detail/<int:id>', detail , name="detail")

]
