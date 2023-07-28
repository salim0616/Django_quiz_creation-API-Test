from django.shortcuts import render
from quiz.authentication import QuizAuthentication
from .models import Exam,Section
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExamSerilizer,SectionSerilizer

# Create your views here.
from rest_framework import generics


server_err={'status':500,'data':'Internal server occured'}

class ExamHandler(generics.ListCreateAPIView):
    authentication_classes=[QuizAuthentication]
    # serializer_class=

    def get(self,request):
        try:
            final_query=Exam.objects.filter(created_by_id=request.user_id).values()

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
            exam_id=request.query_param.get('exam','')
            if exam_id!="":
                final_query=Section.objects.filter(exam_id=exam_id,exam__created_by_id=request.user_id).values()
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
            return Response({"msg":"Successfully Created Exam","status":200},status=status.HTTP_200_OK)
               
        except Exception as e:
            print(e)
            return Response(server_err,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
