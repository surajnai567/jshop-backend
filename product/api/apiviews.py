from .serializer import ProductSerializer
from product.models import Product
from django.http.response import JsonResponse
from rest_framework.views import APIView
import json
from category.models import CategoryModel
import staticdata
from subcategory.models import SubCategory


class GetAllProductApiView(APIView):
	def post(self, request):
		pass


class GetNewProductApiView(APIView):
	def post(self, request):
		# get token for access control
		token = ''
		serialize_products = []
		try:
			products = Product.objects.filter(is_new=True)
			serialize_products = ProductSerializer(products, many=True).data
			for i in serialize_products:
				i['image'] = [i['image'], i['image1'],i['image2']]
		except:
			pass
		return JsonResponse({"code": "200", "status": "success", "products": serialize_products})


class GetHomePageProductApiView(APIView):
	def post(self, request):
		# get token for access control
		token = ''
		serialize_products = []
		try:
			products = Product.objects.filter(homepage=True)
			serialize_products = ProductSerializer(products, many=True).data
			for i in serialize_products:
				i['image'] = [i['image'], i['image1'], i['image2']]
		except:
			pass
		return JsonResponse({"code": "200", "status": "success", "products": serialize_products})


class GetCategoryProductApiView(APIView):
	def post(self, request):
		# get token for access control
		category = json.loads(request.body.decode('utf-8'))
		cat = CategoryModel.objects.filter(categry=category['categry'])[0]
		print(cat)
		token = ''
		serialize_products = []
		try:
			products = Product.objects.filter(category=cat.id)
			serialize_products = ProductSerializer(products, many=True).data
			for i in serialize_products:
				#i['image'] = [i['image'], i['image1'], i['image2']]
				i['image'] = ['https://helpx.adobe.com/content/dam/help/en/stock/how-to/visual-reverse-image-search/jcr_content/main-pars/image/visual-reverse-image-search-v2_intro.jpg',"https://helpx.adobe.com/content/dam/help/en/stock/how-to/visual-reverse-image-search/jcr_content/main-pars/image/visual-reverse-image-search-v2_intro.jpg","https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Gull_portrait_ca_usa.jpg/1200px-Gull_portrait_ca_usa.jpg"]
		except:
			pass
		return JsonResponse({"code": "200", "status": "success", "products": serialize_products})


class GetSearchProductApiView(APIView):
	def get(self, request):
		# get token for access control
		query_string = request.GET.get('s')
		token = ''
		serialize_products = ''
		try:
			products = Product.objects.all()
			serialize_products = ProductSerializer(products, many=True).data
			for i in serialize_products:
				i['image'] = [i['image'], i['image1'], i['image2']]
		except:
			pass
		return JsonResponse({"code": "200", "status": "success", "products": serialize_products})

