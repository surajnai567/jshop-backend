from user.models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
import json


class UserRegisterView(APIView):
	def post(self, request):
		# print(request.body.decode('utf-8'))
		post_data = json.loads(request.body.decode('utf-8'))
		data = User.objects.filter(mobile=post_data['mobile'])
		if(len(data)):
			print(len(data))
			return JsonResponse({"code": 403, "status": "User Already Exist"})

		user = User(mobile=post_data['mobile'], fname=post_data['fname'], lname=post_data['lname'], password=post_data['password'])
		print(user)
		user.save()
		response_data = User.objects.get(id=int(user.id))
		serialize_data = UserSerializer(response_data).data
		return JsonResponse({"code": 201, "status": "Registeration Successfull !!", "userData": serialize_data})

	def get(self, request):
		data = User.objects.all()
		pro = UserSerializer(data, many=True).data
		da = {"status": "true", "data": pro}
		return Response(da)


class UserLogin(APIView):
	def post(self, request):
		post_data = json.loads(request.body.decode('utf-8'))
		data = User.objects.filter(mobile=post_data['mobile'], password=post_data['password'])
		if(len(data)):
			print(data)
			serial_data = UserSerializer(data[0]).data
			return JsonResponse({'code': 200, "status": "Login Successfull !!", "userData": serial_data})

			# perform login and return response
		return JsonResponse({"code": 400, "status": "Bad request wrong credential"})


class UpdateUser(APIView):
	def post(self, request):
		post_data = json.loads(request.body.decode('utf-8'))
		user = User.objects.filter(token=post_data['token'])[0]
		serial = UserSerializer(user).data
		return JsonResponse({"code": 200, "status": "success", "userData": serial})