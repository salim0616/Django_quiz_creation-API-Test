from django.shortcuts import render
import time, uuid,jwt,hashlib
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer


def auth(username,password):
    hashedpass=hashlib.md5(password.encode()).hexdigest()
    if User.objects.filter(username=username,password=hashedpass).exists():
        return User.objects.filter(username=username,password=hashedpass).first()
    else:
        return False

class Login(APIView):
    
    def get_expiry_time(self):
        current_time = int(time.time())   
        updated_time = current_time + 30*60 
        return updated_time

    def generateToken(self,userobj):
        key=settings.SECRET_KEY
        expiry_time=self.get_expiry_time()
        encoded_token = jwt.encode({"uid": str(userobj.uid), "exp":expiry_time}, key, algorithm="HS256")
        return encoded_token
    
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        userobj=auth(username,password)
        if userobj:
            access_token=self.generateToken(userobj)
            return JsonResponse({'access_key':access_token},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'msg':"Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED)

@api_view(["POST"])
def register(request):
    try:
        required_fields=["username","name","password","usertype"]
        if any(request.data.get(key)==None or request.data.get(key)=="" for key in required_fields):
            return Response({"msg":"Mandatory parametrs are missing","status":400},status=status.HTTP_400_BAD_REQUEST)


        # password=hashlib.md5(.encode()).hexdigest()
        data={
            "username":request.data.get("username"),
            "name":request.data.get("name"),
            "email":request.data.get("email"),
            "uid":uuid.uuid4(),
            "password":request.data.get("password"),
            "usertype":request.data.get("usertype"),
        }
        userserializer=UserRegisterSerializer(data=data)
        print(repr(userserializer))
        if not userserializer.is_valid():
            return Response(userserializer.errors,status=status.HTTP_400_BAD_REQUEST)

        userserializer.save() 
        return Response({"msg":"Successfully Registered","status":200},status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"msg":"Registration Failed","status":500},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['get'])
def probe(request):
    return Response(data={'status':'Server is Reachable'},status=status.HTTP_200_OK)