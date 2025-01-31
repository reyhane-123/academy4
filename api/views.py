from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

list1=[
    {"name":"html and css", "teacher":"ahamadi","price":4000000},
    {"name":"c#", "teacher":"moslemi","price":5000000},
    {"name":"python", "teacher":"asksri","price":6000000}
]
def show(request):
    data=""
    for item in list1:
        data=data+f"name :{item['name']}, teacher :{item['teacher']} , price :{item['price']}"
    return HttpResponse(data)
