from django.shortcuts import render
from quiz.authentication import QuizAuthentication
from .models import Exam,Section,Topic,Questions
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExamSerilizer,SectionSerilizer,TopicSerilizer,QuestionSerializer
from rest_framework import generics


server_err={'status':500,'data':'Internal server occured'}

class ExamHandler(generics.ListCreateAPIView):
    authentication_classes=[QuizAuthentication]
    # serializer_class=

    def get(self,request):
        try:
            if request.is_admin:

                final_query=Exam.objects.filter(created_by_id=request.user_id).values()
            else:
                final_query=Exam.objects.all().values()

            return Response({'data':final_query},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(server_err,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def post(self,request):
        try:
            exam_serilizer=ExamSerilizer(data=request.data)
            request.data['created_by']=request.user_id

            if not exam_serilizer.is_valid():
                return Response(exam_serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
            exam_serilizer.save()
            return Response({"msg":"Successfully Created Exam","status":200},status=status.HTTP_200_OK)
               
        except Exception as e:
            print(e)
            return Response(server_err,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class SectionHandler(generics.ListCreateAPIView):
    authentication_classes=[QuizAuthentication]
    # serializer_class=

    def get(self,request):
        try:
            exam_id=request.query_params.get('exam','')
            if exam_id!="":
                if request.is_admin:
                    final_query=Section.objects.filter(exam_id=exam_id,exam__created_by_id=request.user_id).values()
                else:
                    final_query=Section.objects.filter(exam_id=exam_id).values()

            else:
                return Response({"msg":"Invalid Request"},status=status.HTTP_400_BAD_REQUEST)

            return Response({'data':final_query},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(server_err,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def post(self,request):
        try:
            section_serilizer=SectionSerilizer(data=request.data)
            # request.data['created_by']=request.user_id

            if not section_serilizer.is_valid():
                return Response(section_serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
            section_serilizer.save()
            return Response({"msg":"Successfully Created Section","status":200},status=status.HTTP_200_OK)
               
        except Exception as e:
            print(e)
            return Response(server_err,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class TopicHandler(generics.ListCreateAPIView):
    authentication_classes=[QuizAuthentication]
    # serializer_class=

    def get(self,request):
        try:
            section_id=request.query_params.get('section','')
            if section_id!="":
                if request.is_admin:
                    final_query=Topic.objects.filter(section_id=section_id,section__exam__created_by_id=request.user_id).values()
                else:
                    final_query=Topic.objects.filter(section_id=section_id).values()

            else:
                return Response({"msg":"Invalid Request"},status=status.HTTP_400_BAD_REQUEST)

            return Response({'data':final_query},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(server_err,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def post(self,request):
        try:
            topic_serilizer=TopicSerilizer(data=request.data)
            # request.data['created_by']=request.user_id

            if not topic_serilizer.is_valid():
                return Response(topic_serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
            topic_serilizer.save()
            return Response({"msg":"Successfully Created Topic","status":200},status=status.HTTP_200_OK)
               
        except Exception as e:
            print(e)
            return Response(server_err,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class QuestionHandler(generics.ListAPIView):
    authentication_classes=[QuizAuthentication]

    def get(self,request):
        try:
            topic_id=request.query_params.get('topic','')
            if topic_id!="":
                if request.is_admin:
                    final_query=Questions.objects.filter(topic_id=topic_id,topic__section__exam__created_by_id=request.user_id).values()
                else:
                    # for normal user
                    final_query=Questions.objects.filter(topic_id=topic_id).values('id','topic','question','photo','option1','option2',
                                                                                   'option3','option4')


            else:
                return Response({"msg":"Invalid Request"},status=status.HTTP_400_BAD_REQUEST)

            return Response({'data':final_query},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(server_err,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def post(self,request):
        try:
            question_serilizer=QuestionSerializer(data=request.data)
            if not question_serilizer.is_valid():
                return Response(question_serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
            question_serilizer.save()
            return Response({"msg":"Successfully Created Question","status":200},status=status.HTTP_200_OK)
               
        except Exception as e:
            print(e)
            return Response(server_err,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class UserSubmitQuiz(generics.ListAPIView):
    authentication_classes=[QuizAuthentication]

    '''
    sample payload:
    {
    "topic": 1,
    "q_a": [
        {
            "q_no": 1,
            "u_a": "rth"
        }
    ]
}
    '''

    def get(self,request):
        topic=request.data.get('topic')
        total_correct=0
        final_query=Questions.objects.filter(topic_id=topic).values('id','correct_answer')
        # if 


        