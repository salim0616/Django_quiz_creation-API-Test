from django.urls import path
from .views import ExamHandler,SectionHandler

urlpatterns=[
    path("exam/",ExamHandler.as_view(),name="exams"),
    path("section/",SectionHandler.as_view(),name="sections"),


]