from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):

	return render(request, "recPub/index.html") 

def search(request):
	search = request.GET.get('search_text')
	return HttpResponse("hello search>>" +search)

def recResult(request, pub_id):
	print "id>>" + str(pub_id)
	return HttpResponse("hello search" + str(pub_id))
