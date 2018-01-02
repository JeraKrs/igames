from django.http import HttpResponse
import json

def index(request):
	data = {'name': 'Igames'}
	return HttpResponse(json.dumps(data), content_type="application/json")


def info(request):
	response = {}
	return HttpResponse(json.dumps(response), content_type="application/json")


def search(request):
	response = {}
	return HttpResponse(json.dumps(response), content_type="application/json")


def rank(request):
	response = {}
	return HttpResponse(json.dumps(response), content_type="application/json")
