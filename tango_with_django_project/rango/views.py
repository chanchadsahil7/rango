from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page


def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by("-views")[:5]
	context_dict = {'categories': category_list, 'pages' : page_list}
	return render(request,'rango/index.html',context=context_dict)
	#context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	#return render(request,'rango/index.html',context=context_dict)
def about(request):
	return render(request, 'rango/about.html')

def show_category(request):
	context_dict = {}

	try:
		context_dict['category'] = Category.objects.order_by('-likes')[:5]
	except Category.DoesNotExist:
		context_dict['pages'] = None
		context_dict['category'] = None
	return render(request,'rango/category.html',context=context_dict)

def contact(request):
	return render(request, 'rango/contact.html')
