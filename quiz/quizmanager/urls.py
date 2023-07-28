from django.urls import path
from .views import ExamHandler,SectionHandler,TopicHandler,QuestionHandler

urlpatterns=[
    path("exam/",ExamHandler.as_view(),name="exams"),
    path("section/",SectionHandler.as_view(),name="sections"),
    path("topic/",TopicHandler.as_view(),name="topics"),
    path("question/",QuestionHandler.as_view(),name="questions"),




]