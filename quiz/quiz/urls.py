from django.urls import path ,include 
from rest_framework.urlpatterns import format_suffix_patterns
from users.views import probe


urlpatterns = [
    path('',probe,name='probe-check'),
    path("user/",include("users.urls")),
    path("manage/",include("quizmanager.urls")),
    # path('quizz/',include('quiz.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)