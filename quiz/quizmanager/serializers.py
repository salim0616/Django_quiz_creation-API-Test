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


class TopicSerilizer(serializers.ModelSerializer):

    class Meta:
        model=Topic
        fields='__all__'


class QuestionSerializer(serializers.ModelSerializer):
    correct_answer=serializers.CharField(required=True)
    class Meta:
        model=Questions
        fields='__all__'


    def validate(self,data):
        if all(data.get('correct_answer')!=val for val in [data.get('option1'),
                                                           data.get('option2'),
                                                           data.get('option3'),
                                                           data.get('option4')]):
            raise serializers.ValidationError({'correct_answer':'should match with one of the options'})
        return data

    # def to_representation(self, instance):
    #     return super().to_representation(instance)


