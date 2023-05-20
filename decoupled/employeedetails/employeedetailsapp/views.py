from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import json
# from .models import User
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from whizco_auth.serializer import *
from rest_framework.authtoken.models import Token
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from rest_framework import status
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
# from whizcolib.response.response_messages import ApiResponseMessages
# from whizcolib.response.api_response import CustomResponse
# from whizcolib.utility.utility import Email
from rest_framework.generics import GenericAPIView

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from . models import *

# Create your views here.
@permission_classes([AllowAny,])
class EmployeeDetail(APIView):

    def get(self, request):
        print("incoming")
        employee_list = list(Employee.objects.all().values())
        print(employee_list)
        return Response(employee_list)
        """
            This api verifies the newly created user account.

            :param request: ser account id
            :return: returns user account verification status message
        """ 

    def post(self,request):
        data = json.loads(request.body.decode('utf-8'))
        print("><<<<<><><><><><>><good",data)
        name = data["name"]
        age =  data["age"]
        place = data["place"]
        email = data["email"]
        address = data["address"]

        post_data = Employee(name=name,age=age,place=place,email_id=email,address=address)
        post_data.save()
        print("saved")
        return Response('200')

        # serializer = ArticleSerializer(data = request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,status=status.HTTP_201_CREATED)
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
        # try:
        #     user = User.objects.get(id = id)
        #     if user.is_active == False:
        #         user.is_active=True
        #         user.save()
        #         msg = api_msg_obj.activate_account
        #         status_code = status.HTTP_202_ACCEPTED                

        #     else:
        #         msg = api_msg_obj.already_activate
        #         status_code=status.HTTP_208_ALREADY_REPORTED

        # except:
        #     msg = api_msg_obj.not_found
        #     status_code=status.HTTP_401_UNAUTHORIZED

        # resp_json = CustomResponse.default_response(msg, status_code)
        # return redirect(settings.CROS_APP_URL) 


@permission_classes([AllowAny,])
class Employeeop(APIView):
    def get_obj(self,request,id):
        try:
            print("cccccc",request,id)
            return Employee.objects.get(id=id)
            # print('dddddd',article_obj)
        except Employee.DoesNotExist:
            return Response("Error not found",status=status.HTTP_400_BAD_REQUEST)
    # def get(self,request,id):
    #     try:
    #         print("zzzzzzzzz",request)
    #         art_obj = self.get_obj(request,id)
    #         print("art_obj",art_obj)
    #         # serializer = ArticleSerializer(art_obj)
    #         return Response(art_obj)
    #     except:
    #         return Response("Id not found")

    # def put(self,request,id):
    #     art_obj = self.get_obj(request,id)
    #     print(art_obj)
    #     serializer = ArticleSerializer(art_obj,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,id):
        art_obj = self.get_obj(request,id)
        print("delete",art_obj)
        art_obj.delete()
        return Response('200')
    # status=status.HTTP_204_NO_CONTENT


@permission_classes([AllowAny,])
class Employeeupdate(APIView):
    def get_obj(self,request,id):
        try:
            print("cccccc",request,id)
            return Employee.objects.get(id=id)
            # print('dddddd',article_obj)
        except Employee.DoesNotExist:
            return Response("Error not found",status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,id):
        try:
            print("zzzzzzzzz",request)
            art_objs = Employee.objects.filter(id=id).values()
            # art_obj = self.get_obj(request,id)
            print("art_obj",art_objs)
            return Response(art_objs)
        except:
            return Response("Id not found")
    
    def post(self,request):
            data = json.loads(request.body.decode('utf-8'))
            print("><<<<<><><><><><>><good",data)
            id = data["id"]
            name = data["name"]
            age =  data["age"]
            place = data["place"]
            email = data["email"]
            address = data["address"]

            post_data = Employee.objects.filter(id=id).update(name=name,age=age,place=place,email_id=email,address=address)
            print("post_data",post_data)
            # post_data.save()
            print("updated")
            return Response('200')

    # def put(self,request,id):
    #     art_obj = self.get_obj(request,id)
    #     print(art_obj)
    #     serializer = ArticleSerializer(art_obj,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # def delete(self,request,id):
    #     art_obj = self.get_obj(request,id)
    #     print("delete",art_obj)
    #     art_obj.delete()
    #     return Response('200')
    # status=status.HTTP_204_NO_CONTENT



@permission_classes([AllowAny,])
class EmployeeupdateData(APIView):
    def get_obj(self,request,id):
        try:
            print("cccccc",request,id)
            return Employee.objects.get(id=id)
            # print('dddddd',article_obj)
        except Employee.DoesNotExist:
            return Response("Error not found",status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,id):
        try:
            print("zzzzzzzzz",request)
            art_objs = Employee.objects.filter(id=id).values()
            # art_obj = self.get_obj(request,id)
            print("art_obj",art_objs)
            return Response(art_objs)
        except:
            return Response("Id not found")
    
    def post(self,request):
            data = json.loads(request.body.decode('utf-8'))
            print("><<<<<><><><><><>><good",data)
            id = data["id"]
            name = data["name"]
            age =  data["age"]
            place = data["place"]
            email = data["email"]
            address = data["address"]

            post_data = Employee.objects.filter(id=id).update(name=name,age=age,place=place,email_id=email,address=address)
            print("post_data",post_data)
            # post_data.save()
            print("updated")
            return Response('200')

   
