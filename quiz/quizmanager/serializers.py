from rest_framework import serializers
from users.models import User
from .models import *

class ExamSerilizer(serializers.ModelSerializer):

    class Meta:
        model=Exam
        fields='__all__'


class SectionSerilizer(serializers.ModelSerializer):

    class Meta:
        model=Section
        fields='__all__'

