from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
    res=HttpResponse("<html> <body bgcolor=pink> <center> <h1> welcome the django test"
                     "</h1>"
                     "<h2>welcome to the my app</h2>"
                     "<h2> konda  sai kiran</h2>"
                     "<h3>it is running</h3></center></body></html>")
    return res